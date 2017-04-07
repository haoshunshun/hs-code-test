#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
pvDict={}
winDict={}
clkDict={}
for line in open("/home/work/log/bridge/pv/hs"):
    jsonObj = json.loads(line)
    action = jsonObj["action"]
    if action == "pv":
        pv_time = jsonObj["_time"]
        pv_auction = jsonObj["auction_id"]
        pvDict[pv_auction]={"time":pv_time}
    elif action == "win":
        win_time = jsonObj["_time"]
        win_auction = jsonObj["auction"]
        winDict[win_auction]={"time":win_time}
    else:
        clk_time = jsonObj["_time"]
        clk_auction = jsonObj["click_auction"]        
        clkDict[clk_auction]={"time":clk_time}
for k,v in clkDict.items():
    if k in winDict and k in pvDict:
        print "%s\t%s\t%s\t%s" % (k,pvDict[k]["time"],winDict[k]["time"],clkDict[k]["time"])
    else:
        continue
