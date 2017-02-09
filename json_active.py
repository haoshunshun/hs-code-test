#!/usr/bin/python
#!-*- coding: utf-8 -*-

import json 
import time
#{"_time":"2016-10-25 10:00:12,164","account":"1000056","account_list":["1000056"],"action":"click","adgroup":"-","adid":"1000056","adspot":"10000073","aduser":"100007","appid":"100019","auction":"bbcc80a09a5611e69864fa163ee4a5fe","click_auction":"bbcc80a09a5611e69864fa163ee4a5fe","company":"3","crid":"100000338","dest":"dest_1000056","deviceString":"356009070138830","exchange":"bridge","host":"hig_001","impid":"2fe62341f491474f8e81431f8c07f028","ip":"112.225.134.167","os":"2","price":983,"strategy":"1","supplier":"1","time":1477360799023,"vdacct":"70008","vendor":"70008"}
#2016-10-24 07:11:45>9b3072af4ceae498>---active>-3_001_load
#active.2016102419.log 
last_hour = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600))
last_Hour = time.strftime("%Y-%m-%d %H",time.localtime(time.time()-3600))
file_active = open('/home/work/hs/active_log/active.'+last_hour+'.log')
json_file=open('/home/work/hs/active_log/json_active.'+last_hour+'.log','w+')
for line in file_active:
    line_str = line.strip("\r\n").split("\t")
    activetime=line_str[0]
    if activetime.split(":")[0] in last_Hour:
        auctionid = line_str[1]
        logcat = line_str[2]
        mes = line_str[3]
        active_rlt = {'click_auction':auctionid,'_time':activetime,'action':logcat,'crid':mes}
        active_json = json.dumps(active_rlt)
        json_file.write("%s\n" % (active_json));
json_file.close()
