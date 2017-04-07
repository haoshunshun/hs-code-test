#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import json
staDict={}
proDict={}
last_24_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600*24))
join_path = '/home/work/disk/nhs/dingxiang/log/test_join_' + last_24_hour
f_rlt = open('/home/work/disk/nhs/dingxiang/log/test_result_'+last_24_hour,'w+')
for join_line in open(join_path):
    join_str = join_line.rstrip("\r\n").strip().split("\t")
    time = join_str[0]
    activetag=int(join_str[1])
    clicktag = int(join_str[2])
    wintag = int(join_str[3])
    bidtag = int(join_str[4])
    adspotid = join_str[5]
    creative_id = join_str[6]
    os = join_str[7]
    connectType = join_str[8]
    device = join_str[9].split(":")
    osv = device[0]
    carrier = device[1]
    model = device[2]
    make = device[3]
    location = join_str[10].split(":")
    province = location[1]
    city = location[2]
    price = join_str[11]
    if price=="9999":
        real_price = 0
    else:
        real_price = int(price.split("CNY")[0])
    pk = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (time,adspotid,creative_id,province,city,model,make,os,osv,connectType,carrier)
    if staDict.get(pk,None)==None:
        staDict[pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"price":real_price}
    else:
        staDict[pk]["bid"]+=bidtag
        staDict[pk]["win"]+=wintag
        staDict[pk]["click"]+=clicktag
        staDict[pk]["active"]+=activetag
        staDict[pk]["price"]+=real_price
for key,v in staDict.items():
    if v["bid"]!=0:
        key_str = key.split("\t")
        jsonRlt = {'time':key_str[0],'adspotid':key_str[1],'creativeid':key_str[2],'province':key_str[3],'city':key_str[4],'model':key_str[5],'make':key_str[6],'os':key_str[7],'osv':key_str[8],'connectType':key_str[9],'carrier':key_str[10],'bids':v["bid"],'wins':v["win"],'clicks':v["click"],'active':v["active"],'costs':v["price"]/1000000.0}
        json_result = json.dumps(jsonRlt,sort_keys=True)
        f_rlt.write("%s\n" % (json_result));
f_rlt.close()
