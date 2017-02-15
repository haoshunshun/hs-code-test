#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import time

last_24_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600*24))
for line in open("/home/work/disk/nhs/dingxiang/log/test_conType_result_"+last_24_hour):
    lineStr=line.split("\t")
    if len(lineStr)>7:
        time=lineStr[0]
        adspotId=lineStr[1]
#        creativeId=lineStr[2]
    #    conTy=lineStr[3]
        bids=lineStr[4]
     #   wins=lineStr[5]
      #  clicks=lineStr[6]
      #  actives=lineStr[7]
    else:
        continue
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport')
    cursor=db.cursor()
    cursor.execute("insert into sqlTest values (%s,%s,%s)",[time,adspotId,bids])
    db.commit()
    cursor.close()
    db.close()
