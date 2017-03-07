#!/usr/bin/python
#!-*- coding: utf-8 -*-
import json
staDict={}
pvList=[]
winList=[]
for line in open("/home/work/log/bridge/pv/hs"):
    jsonObj = json.loads(line)
    action = jsonObj["action"]
    if action == "pv":
        pv_time = jsonObj["_time"]
        pv_auction = jsonObj["auction_id"]
        pvList.append(pv_auction)
    elif action == "win":
        win_time = jsonObj["_time"]
        win_auction = jsonObj["auction"]
        winList.append(win_auction)
    else:
        clk_time = jsonObj["_time"]
        clk_auction = jsonObj["click_auction"]        
        if clk_auction in winList and clk_auction in pvList:
            print "%s\t%s\t%s\t%s" % (clk_auction,pv_time,win_time,clk_time)
        else:
            continue
