#!/bin/usr/python
# -*- coding: utf-8 -*-
import MySQLdb
import time
import logging
import os
import sys

logger = logging.getLogger('bridge.bidrate')
fh = logging.FileHandler('logger/bidrate.log')
fh.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(fh)

if __name__ == "__main__":
    if (len(sys.argv) >= 2) and (sys.argv[1] != ""):
        last_hour_string = sys.argv[1]
    else:
        last_hour_string = time.strftime("%Y-%m-%d_%H", time.localtime(time.time()-3600))

    last_hour_timestamp = int(time.mktime(time.strptime(last_hour_string,'%Y-%m-%d_%H')))
    last_24_hour_timestamp=last_hour_timestamp-3600*24

    last_hour_dict={}
    last_24_hour_dict={}
    adspot_nameDict={}
    connect = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport',charset='utf8')
    cursor = connect.cursor()

    cursor.execute('SELECT id,adspot_name FROM jupiterdb.ssp_adspot')
    adspot_rlt = cursor.fetchall()
    for line_adspot_rlt in adspot_rlt:
        ads_id = str(line_adspot_rlt[0])
        adspot_name = line_adspot_rlt[1]
        adspot_nameDict[ads_id] = [adspot_name]
		
    last_hour_sql = 'SELECT adspot_id,pvs,sum(bids) FROM jupiterreport.ssp_report_hourly where timestamp='+str(last_hour_timestamp)+' group by adspot_id'
    cursor.execute(last_hour_sql)
    last_rlt = cursor.fetchall()
    for line_last_rlt in last_rlt:
        if last_hour_dict.has_key(line_last_rlt[0]):
            last_hour_val = last_hour_dict[line_last_rlt[0]]
            last_hour_val[0] = line_last_rlt[1]
            last_hour_val[1] = line_last_rlt[2]
            if last_hour_val[0]>0:
                last_hour_val[2] = round(last_hour_val[1]/float(last_hour_val[0]),4)
            else:
                last_hour_val[2] = 0.0000
        else:
            last_hour_val = [0,0,0.0000]
            last_hour_val[0] = int(line_last_rlt[1])
            last_hour_val[1] = int(line_last_rlt[2])
            if last_hour_val[0]>0:
                last_hour_val[2] = round(last_hour_val[1]/float(last_hour_val[0]),4)
            else:
                last_hour_val[2] = 0.0000
        last_hour_dict[line_last_rlt[0]] = last_hour_val

    last_24_hour_sql = 'SELECT adspot_id,pvs,sum(bids) FROM jupiterreport.ssp_report_hourly where timestamp='+str(last_24_hour_timestamp)+' group by adspot_id'
    cursor.execute(last_24_hour_sql)
    last_24_rlt = cursor.fetchall()
    for line_last_24 in last_24_rlt:
        if last_24_hour_dict.has_key(line_last_24[0]):
            last_24_val = last_24_hour_dict[line_last_24[0]]
            last_24_val[0] = line_last_rlt[1]
            last_24_val[1] = line_last_rlt[2]
            if last_24_val[0]>0:
                last_24_val[2] = round(last_24_val[2]/float(last_24_val[1]),4)
            else:
                last_24_val[2] = 0.0000
        else:
            last_24_val = [0,0,0.0000]
            last_24_val[0] = int(line_last_24[1])
            last_24_val[1] = int(line_last_24[2])
            if last_24_val[0]>0:
                last_24_val[2] = round(last_24_val[1]/float(last_24_val[0]),4)
            else:
                last_24_val[2] = 0.0000
        last_24_hour_dict[line_last_24[0]] = last_24_val
    connect.commit()
    cursor.close()
    connect.close()
    drop_list=[]
    drop_rates=[]
    rise_list=[]
    rise_rates=[]
    low_list=[]
    low_rates=[]
    drop_ormes='['
    rise_ormes='['
    low_ormes='['
    for k,v in last_hour_dict.items():
        if adspot_nameDict.has_key(k) and last_24_hour_dict.has_key(k) and last_hour_dict[k][0]>300 and last_hour_dict[k][2]<last_24_hour_dict[k][2]-0.2:
            adspot_new_name = adspot_nameDict[k][0].encode("utf8")
            drop_list.append(adspot_new_name)
            drop_rates.append(str(last_hour_dict[k][2]*100) +'%:'+ str(last_24_hour_dict[k][2]*100) +'%')
        elif adspot_nameDict.has_key(k) and last_24_hour_dict.has_key(k) and last_hour_dict[k][0]>300 and last_hour_dict[k][2]>last_24_hour_dict[k][2]+0.2:
            adspot_new_name = adspot_nameDict[k][0].encode("utf8")
            rise_list.append(adspot_new_name)
            rise_rates.append(str(last_hour_dict[k][2]*100) +'%:'+ str(last_24_hour_dict[k][2]*100) +'%')
        elif adspot_nameDict.has_key(k) and last_hour_dict[k][0]>300 and last_hour_dict[k][2]<0.3:
            adspot_new_name = adspot_nameDict[k][0].encode("utf8")
            low_list.append(adspot_new_name)
            low_rates.append(str(last_hour_dict[k][2]*100)+'%')
        else:
            continue
    for i in range(0,len(drop_list)):
        drop_ormes += str(drop_list[i]) +','
    drop_mes = '[BRIDGE][BIDRATE][' + last_hour_string + ']广告位列表' + drop_ormes + '] bidrate降低超过20%。竞价率明细：' + str(drop_rates)
    logger.error(drop_mes)
    os.popen('/usr/bin/python /home/work/run_env/DEPLOY/statistic/notification/operate_notifier.py %s' % (drop_mes))
    
    for i in range(0,len(rise_list)):
        rise_ormes += str(rise_list[i]) +','
    rise_mes = '[BRIDGE][BIDRATE][' + last_hour_string + ']广告位列表' + rise_ormes + '] bidrate上升超过20%。竞价率明细：' + str(rise_rates)
    logger.error(rise_mes)
    os.popen('/usr/bin/python /home/work/run_env/DEPLOY/statistic/notification/operate_notifier.py %s' % (rise_mes))
 
    for i in range(0,len(low_list)):
        low_ormes += str(low_list[i]) + ','
    low_mes = '[BRIDGE][BIDRATE][' + last_hour_string + ']广告位列表' + low_ormes + '] bidrate不超过30%。竞价率明细：' + str(low_rates)
    logger.error(low_mes)
    os.popen('/usr/bin/python /home/work/run_env/DEPLOY/statistic/notification/operate_notifier.py %s' % (low_mes))
