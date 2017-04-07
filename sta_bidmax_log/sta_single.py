#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import json
osDict={}
carrierDict={}
cityDict={}
conTypeDict={}
makeDict={}
modelDict={}
last_24_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600*24))
rlt_path = '/home/work/disk/nhs/dingxiang/log/test_result_' + last_24_hour
car_path = open('/home/work/disk/nhs/dingxiang/log/test_carrier_result_' +last_24_hour,'w+')
os_path = open('/home/work/disk/nhs/dingxiang/log/test_os_result_' + last_24_hour,'w+')
city_path = open('/home/work/disk/nhs/dingxiang/log/test_city_result_' + last_24_hour,'w+') 
conType_path = open('/home/work/disk/nhs/dingxiang/log/test_conType_result_'+last_24_hour,'w+')
make_path = open('/home/work/disk/nhs/dingxiang/log/test_make_result_'+last_24_hour,'w+')
model_path = open('/home/work/disk/nhs/dingxiang/log/test_model_result_'+last_24_hour,'w+')
for rlt_line in open(rlt_path):
    rlt_str = rlt_line.rstrip("\r\n")
    jsonObj = json.loads(rlt_str)
    time = jsonObj['time']
    activetag=int(jsonObj['active'])
    clicktag = int(jsonObj['clicks'])
    wintag = int(jsonObj['wins'])
    bidtag = int(jsonObj['bids'])
    adspotid = jsonObj['adspotid']
    creative_id = jsonObj['creativeid']
    os = jsonObj['os']
    connectType = jsonObj['connectType']
    osv = jsonObj['osv']
    carrier = jsonObj['carrier']
    model = jsonObj['model']
    make = jsonObj['make']
    province = jsonObj['province']
    city = jsonObj['city']
    #costs = float("%.2f" % float(jsonObj['costs']))
    costs = float(jsonObj['costs'])
    os_osv="%s_%s" % (os,osv)
    os_pk = "%s\t%s\t%s\t%s" % (time,adspotid,creative_id,os_osv)
    car_pk = "%s\t%s\t%s\t%s" % (time,adspotid,creative_id,carrier)
    city_pk = "%s\t%s\t%s\t%s" % (time,adspotid,creative_id,city)
    conType_pk ="%s\t%s\t%s\t%s" % (time,adspotid,creative_id,connectType)
    make_pk = "%s\t%s\t%s\t%s" % (time,adspotid,creative_id,make)
    model_pk="%s\t%s\t%s\t%s" % (time,adspotid,creative_id,model)
    if osDict.get(os_pk,None)==None:
        osDict[os_pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"costs":costs}
    else:
        osDict[os_pk]["bid"]+=bidtag
        osDict[os_pk]["win"]+=wintag
        osDict[os_pk]["click"]+=clicktag
        osDict[os_pk]["active"]+=activetag
        osDict[os_pk]["costs"]+=costs
    if carrierDict.get(car_pk,None)==None:
        carrierDict[car_pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"costs":costs}
    else:
        carrierDict[car_pk]["bid"]+=bidtag
        carrierDict[car_pk]["win"]+=wintag
        carrierDict[car_pk]["click"]+=clicktag
        carrierDict[car_pk]["active"]+=activetag
        carrierDict[car_pk]["costs"]+=costs
    if cityDict.get(city_pk,None)==None:
        cityDict[city_pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"costs":costs}
    else:
        cityDict[city_pk]["bid"]+=bidtag
        cityDict[city_pk]["win"]+=wintag
        cityDict[city_pk]["click"]+=clicktag
        cityDict[city_pk]["active"]+=activetag
        cityDict[city_pk]["costs"]+=costs
    if conTypeDict.get(conType_pk,None)==None:
        conTypeDict[conType_pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"costs":costs}
    else:
        conTypeDict[conType_pk]["bid"]+=bidtag
        conTypeDict[conType_pk]["win"]+=wintag
        conTypeDict[conType_pk]["click"]+=clicktag
        conTypeDict[conType_pk]["active"]+=activetag
        conTypeDict[conType_pk]["costs"]+=costs
    if makeDict.get(make_pk,None)==None:
        makeDict[make_pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"costs":costs}
    else:
        makeDict[make_pk]["bid"]+=bidtag
        makeDict[make_pk]["win"]+=wintag
        makeDict[make_pk]["click"]+=clicktag
        makeDict[make_pk]["active"]+=activetag
        makeDict[make_pk]["costs"]+=costs
    if modelDict.get(model_pk,None)==None:
        modelDict[model_pk]={"bid":bidtag,"win":wintag,"click":clicktag,"active":activetag,"costs":costs}
    else:
        modelDict[model_pk]["bid"]+=bidtag
        modelDict[model_pk]["win"]+=wintag
        modelDict[model_pk]["click"]+=clicktag
        modelDict[model_pk]["active"]+=activetag
        modelDict[model_pk]["costs"]+=costs
for key,v in osDict.items():
    if v["bid"]!=0:
        key_str = key.split("\t")
        two_costs = "%.4f" % (v["costs"])
        os_path.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (key_str[0],key_str[1],key_str[2],key_str[3],v["bid"],v["win"],v["click"],v["active"],two_costs));
os_path.close()
for k,val in carrierDict.items():
    k_str = k.split("\t")
    two_costs = "%.4f" % (v["costs"])
    car_path.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (k_str[0],k_str[1],k_str[2],k_str[3],val["bid"],val["win"],val["click"],val["active"],two_costs));
car_path.close()
for k,v in cityDict.items():
    k_str = k.split("\t")
    two_costs = "%.4f" % (v["costs"])
    city_path.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %  (k_str[0],k_str[1],k_str[2],k_str[3],v["bid"],v["win"],v["click"],v["active"],two_costs));
city_path.close()
for k,v in conTypeDict.items():
    k_str = k.split("\t")
    two_costs = "%.4f" % (v["costs"])
    conType_path.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (k_str[0],k_str[1],k_str[2],k_str[3],v["bid"],v["win"],v["click"],v["active"],two_costs));
conType_path.close()
for k,v in makeDict.items():
    k_str = k.split("\t")
    two_costs = "%.4f" % (v["costs"])
    make_path.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (k_str[0],k_str[1],k_str[2],k_str[3],v["bid"],v["win"],v["click"],v["active"],two_costs));
make_path.close()
for k,v in modelDict.items():
    k_str = k.split("\t")
    two_costs = "%.4f" % (v["costs"])
    model_path.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (k_str[0],k_str[1],k_str[2],k_str[3],v["bid"],v["win"],v["click"],v["active"],two_costs));
model_path.close()
