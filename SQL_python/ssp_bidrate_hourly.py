#!/bin/usr/python
#!-*- coding: utf-8 -*-
import MySQLdb
import time
import logging
import os

logger = logging.getLogger()
fh = logging.FileHandler('bidrate_log')
fh.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(fh)


last_hour_timestamp=int(time.time())-(int(time.time())%3600)-3600
last_24_hour_timestamp=int(time.time())-(int(time.time())%3600)-3600*25
last_hour_dict={}
last_24_hour_dict={}

connect = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport',charset='utf8')
cursor=connect.cursor()
last_hour_sql = 'SELECT adspot_id,pvs,sum(bids) FROM jupiterreport.ssp_report_hourly where timestamp='+str(last_hour_timestamp)+' group by adspot_id'
cursor.execute(last_hour_sql)
last_rlt=cursor.fetchall()
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
for k,v in last_hour_dict.items():
	if last_24_hour_dict.has_key(k) and last_hour_dict[k][0]>300 and last_hour_dict[k][2]<last_24_hour_dict[k][2]-0.2:
		warning_mes = '[BRIDGE][BIDRATE] ' + k + ' bidrate drop more than 20% (last_hour:last_25_hour=' + str(last_hour_dict[k][2]) + ':' + str(last_24_hour_dict[k][2]) + ')'
		logger.error(warning_mes)
		os.popen('/usr/bin/python /home/work/run_env/DEPLOY/statistic/notification/operate_notifier.py %s' % (warning_mes))
	else:
		continue
