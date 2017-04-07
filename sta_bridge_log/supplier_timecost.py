#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import time
import MySQLdb
staDict={}
k = 0
last_hour=time.strftime("%Y-%m-%d_%H",time.localtime(time.time()-3600))
db_time = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600))
for file in open("/home/work/run_env/DEPLOY/ssp-report/input/bid."+last_hour+".log"):
	try:
		lineStr = file.rstrip()
		jsonObj = json.loads(lineStr)
		adspot_id = jsonObj["adspot_id"]
		reqhis = jsonObj["reqhis"]
		reqhisListlen = int(len(reqhis))
		for i in range(0,reqhisListlen):
			k += 1
			reqhis_one = reqhis[i]
			name = reqhis_one["name"]
			time = reqhis_one["timecost"]
			pk = "%s\t%s" % (adspot_id,name)
			if staDict.get(pk,None)==None:
				staDict[pk]={"time":time,"times":k}
			else:
				staDict[pk]["time"]+=time
				staDict[pk]["times"]=k
	except:
		continue
for key,val in staDict.items():
	adspot_id = key.split("\t")[0]
	sup_name = key.split("\t")[1]
	tal_time = val["time"]
	times = val["times"]
	means_time = round(tal_time/float(times),4)
	connect = MySQLdb.connect(host="192.168.3.38",user="report",passwd="Bayescomrpt100w",db="statisticreport")
	cursor = connect.cursor()
	cursor.execute("insert into sup_timecost_rlt values (%s,%s,%s,%s,%s,%s)",[db_time,adspot_id,sup_name,tal_time,times,means_time])
	connect.commit()
	cursor.close()
	connect.close()
