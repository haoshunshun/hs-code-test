#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import sys
import json
bidDict={}
winDict={}
clickDict={}
click2Dict={}
activeDict={}
active24Dict={}
MIN_BID_LENGTH = 37
last_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600))
last_23_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600*23))
last_24_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600*24))
last_day = last_24_hour[0:8]
last_24_HOUR = str(last_day)+'23'
bid_path = '/home/work/disk/nhs/dingxiang/bid.'+last_24_hour+'.log'
for bid_line in open(bid_path):
    bid_str = bid_line.rstrip("\r\n").strip().split("\t")
    if len(bid_str)>=3:
        val = bid_str[2].split("\001")
        if len(val)>= MIN_BID_LENGTH:
            auction=val[0]
            adspotid = val[1]
            os = val[17]
            connect = val[20]
            device = val[21]
            location = val[22]
            creativeid=val[33]
            value = "%s\t%s\t%s\t%s\t%s\t%s" % (adspotid,creativeid,os,connect,device,location)
            bidDict[auction]=value
win_path = '/home/work/disk/nhs/dingxiang/win.'+last_24_hour+'.log'
for win_line in open(win_path):
    win_str = win_line.rstrip("\r\n").strip().split("\t")
    if len(win_str)>=5:
        auction=win_str[2]
        price=win_str[4]
        winDict[auction]=price
click_path = '/home/work/disk/nhs/dingxiang/click.'+last_24_hour+'.log'
for click_line in open(click_path):
    click_str = click_line.rstrip("\r\n").strip().split("\t")
    if len(click_str)>=4:
        auction = click_str[2]
        clickDict[auction]="click"
click_last_hour_path = '/home/work/disk/nhs/dingxiang/click.'+last_23_hour+'.log'
for click_last_hour_line in open(click_last_hour_path):
    click_last_hour_str = click_last_hour_line.rstrip("\r\n").strip().split("\t")
    if len(click_last_hour_str)>=4:
        auction = click_last_hour_str[2]
        click2Dict[auction]="click"
active_last_day_path = '/home/work/disk/nhs/dingxiang/active.'+last_24_HOUR+'.log'
for active_last_day_line in open(active_last_day_path):
    active_last_day_str = active_last_day_line.rstrip("\r\n").strip().split("\t")
    if len(active_last_day_str)>=3:
        if "talking_data" in active_last_day_str[3] or "3_001_active_cellphone" in active_last_day_str[3]:
            auction = active_last_day_str[1]
            activeDict[auction] = "active"
active_now_path= '/home/work/disk/nhs/dingxiang/active.'+last_hour+'.log'
for active_now_line in open(active_now_path):
    active_now_str = active_now_line.rstrip("\r\n").strip().split("\t")
    if len(active_now_str)>=3:
        if "talking_data" in active_now_str[3] or "3_001_active_cellphone" in active_now_str[3]:
            auction = active_now_str[1]
            active24Dict[auction] = "active"
f = open('/home/work/disk/nhs/dingxiang/log/test_join_'+last_24_hour,'w+')
print '/home/work/disk/nhs/dingxiang/log/test_join_'+last_24_hour
for key,v in bidDict.items():
#(adspotid,creativeid,os,connect,device,location)
    logCatbid="1"
    auction = key
    vec= v.split("\t")
    adspotid = vec[0]
    creativeid = vec[1]
    os = vec[2]
    connect = vec[3]
    device = vec[4]
    location = vec[5]
    if winDict.get(key,None)!=None:
        logCatwin="1"
        price = winDict[key]
        if clickDict.get(key,None)!=None or click2Dict.get(key,None)!=None:
            logCatclick="1"
            if activeDict.get(key,None)!=None or active24Dict.get(key,None)!=None:
                logCatactive="1"
            else:
                logCatactive="0"
        else:
            logCatclick="0"
            if activeDict.get(key,None)!=None or active24Dict.get(key,None)!=None:
                logCatactive="1"
            else:
                logCatactive="0"
    else:
        logCatwin = "0"
        price = 9999
        if clickDict.get(key,None)!=None or click2Dict.get(key,None)!=None:
            logCatclick="1"
            if activeDict.get(key,None)!=None or active24Dict.get(key,None)!=None:
                logCatactive="1"
            else:
                logCatactive="0"
        else:
            logCatclick="0"
            if activeDict.get(key,None)!=None or active24Dict.get(key,None)!=None:
                logCatactive="1"
            else:
                logCatactive="0"
    f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (last_24_hour,logCatactive,logCatclick,logCatwin,logCatbid,adspotid,creativeid,os,connect,device,location,price));
f.close()
