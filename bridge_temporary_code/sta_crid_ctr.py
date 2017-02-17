#!/usr/bin/python
#!-*- coding: utf-8 -*-

import json
clkcridDict={}
wincridDict={}
# statistic every crid's ctr
file_name = open("hs_rlt_file","w+")
for line in open("/Users/haoshun/hs-code-test/bridge_win"):
    try:
        line = line.strip()
        jsonObj = json.loads(line)
        supplier = jsonObj['supplier']
        crid = jsonObj['crid']
        if wincridDict.get(crid,None)==None:
            wins=1
            wincridDict[crid]={"wins":wins}
        else:
            wincridDict[crid]["wins"]+=1
    except:
        continue
for line in open("/Users/haoshun/hs-code-test/bridge_click"):
    try:
        line = line.strip()
        jsonObj = json.loads(line)
        supplier = jsonObj['supplier']
        crid = jsonObj['crid']
        if clkcridDict.get(crid,None)==None:
            clks=1
            clkcridDict[crid]={"clks":clks}
        else:
            clkcridDict[crid]["clks"]+=1
    except:
        continue
for key,v in wincridDict.items():
    crid = key
    wins = v["wins"]
    if clkcridDict.get(key,None)!=None:
        clks = clkcridDict[key]["clks"]
        file_name.write("%s\t%s\t%s\t%s\n" % (key,v["wins"],clks,float(clks)/v["wins"]))
    else:
        clks = 0
        file_name.write("%s\t%s\t%s\t%s\n" % (key,v["wins"],0,0.00))
