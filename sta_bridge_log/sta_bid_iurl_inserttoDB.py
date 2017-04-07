#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb
import os
last_hour = time.strftime("%Y-%m-%d_%H",time.localtime(time.time()-3600))
bosAddress = 'bos:/hs-test/dataLog_2.0/ssp/Sta/bid_iurl'+last_hour+'/part-00000'
cpAddress = '/home/work/run_env/hs/'+last_hour+'_iurl_rlt'
copyBOSFileCommand='/usr/local/bin/bce bos cp '+bosAddress +' '+cpAddress
os.system(copyBOSFileCommand)
time_tuple = time.strptime(last_hour,"%Y-%m-%d_%H")
lastTimeBlockStamp = int(time.mktime(time_tuple))
print lastTimeBlockStamp
for line in open(cpAddress):
   lineStr = line.split("\t")
   if len(lineStr)>7:
       app_id = lineStr[0]
       adspot_id = lineStr[1]
       iurlMd5 = lineStr[2]
       cntMd5 = lineStr[3]
       supplier = lineStr[4]
       iurl = lineStr[5]
       word = lineStr[6]
       bids = lineStr[7]
   else:
       continue
   db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport',charset='utf8')
   cursor = db.cursor()
   cursor.execute("insert into bid_iurl_rlt values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",[lastTimeBlockStamp,app_id,adspot_id,iurlMd5,cntMd5,supplier,bids,iurl,word])
   db.commit()
   cursor.close()
   db.close()
