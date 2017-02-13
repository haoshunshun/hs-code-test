#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import time
last_24_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600*24))
#/home/work/disk/nhs/dingxiang/log/test_carrier_result_2016112015  2016112015^I10000033^I100000493^I46001^I228^I133^I2^I0^I4.1373
for line in open("/home/work/disk/nhs/dingxiang/log/test_make_result_"+last_24_hour):
    lineStr=line.split("\t")
    if len(lineStr)>7:
        time = lineStr[0]
        adspotId=lineStr[1]
        creativeId=lineStr[2]
        make=lineStr[3]
        bids=lineStr[4]
        wins=lineStr[5]
        clicks=lineStr[6]
#        actives=lineStr[7]
    else:
        continue
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor = db.cursor()
    cursor.execute("insert into make_sta_result values (%s,%s,%s,%s,%s,%s,%s)",[time,adspotId,creativeId,make,bids,wins,clicks])
    db.commit()
for line in open("/home/work/disk/nhs/dingxiang/log/test_model_result_"+last_24_hour):
    lineStr=line.split("\t")
    if len(lineStr)>7:
        time = lineStr[0]
        adspotId = lineStr[1]
        creativeId = lineStr[2]
        model = lineStr[3]
        bids = lineStr[4]
        wins = lineStr[5]
        clicks = lineStr[6]
#        actives = lineStr[7]
    else:
        continue
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor=db.cursor()
    cursor.execute("insert into model_sta_result values (%s,%s,%s,%s,%s,%s,%s)",[time,adspotId,creativeId,model,bids,wins,clicks])
    db.commit()
for line in open("/home/work/disk/nhs/dingxiang/log/test_os_result_"+last_24_hour):
    lineStr=line.split("\t")
    if len(lineStr)>7:
        time=lineStr[0]
        adspotId=lineStr[1]
        creativeId=lineStr[2]
        os=lineStr[3]
        bids=lineStr[4]
        wins=lineStr[5]
        clicks=lineStr[6]
       # actives=lineStr[7]
    else:
        continue
    db=MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor=db.cursor()
    cursor.execute("insert into osv_sta_result values (%s,%s,%s,%s,%s,%s,%s)",[time,adspotId,creativeId,os,bids,wins,clicks])
    db.commit()
for line in open("/home/work/disk/nhs/dingxiang/log/test_carrier_result_"+last_24_hour):
    lineStr =line.split("\t")
    if len(lineStr)>7:
        time=lineStr[0]
        adspotId=lineStr[1]
        creativeId=lineStr[2]
        carrier=lineStr[3]
        bids=lineStr[4]
        wins=lineStr[5]
        clicks=lineStr[6]
#        actives=lineStr[7]
    else:
        continue
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor=db.cursor()
    cursor.execute("insert into carrier_sta_result values (%s,%s,%s,%s,%s,%s,%s)",[time,adspotId,creativeId,carrier,bids,wins,clicks])
    db.commit()
for line in open("/home/work/disk/nhs/dingxiang/log/test_city_result_"+last_24_hour):
    lineStr=line.split("\t")
    if len(lineStr)>7:
        time=lineStr[0]
        adspotId=lineStr[1]
        creativeId=lineStr[2]
        city=lineStr[3]
        bids=lineStr[4]
        wins=lineStr[5]
        clicks=lineStr[6]
#        actives=lineStr[7]
    else:
        continue
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor=db.cursor()
    cursor.execute("insert into city_sta_result values (%s,%s,%s,%s,%s,%s,%s)",[time,adspotId,creativeId,city,bids,wins,clicks])
    db.commit()
for line in open("/home/work/disk/nhs/dingxiang/log/test_conType_result_"+last_24_hour):
    lineStr=line.split("\t")
    if len(lineStr)>7:
        time=lineStr[0]
        adspotId=lineStr[1]
        creativeId=lineStr[2]
        conTy=lineStr[3]
        bids=lineStr[4]
        wins=lineStr[5]
        clicks=lineStr[6]
      #  actives=lineStr[7]
    else:
        continue
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor=db.cursor()
    cursor.execute("insert into conTy_sta_result values (%s,%s,%s,%s,%s,%s,%s)",[time,adspotId,creativeId,conTy,bids,wins,clicks])
    db.commit()
    cursor.close()
    db.close()
