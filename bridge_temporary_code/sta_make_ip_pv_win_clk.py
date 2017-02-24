#!/usr/bin/python
#!-*- coding: utf-8 -*-
from ipip import IP
import json
import os
pvDict={}
clkDict={}
winDict={}
staDict={}
rltDict={}
# statistic every crid's ctr
f = open("ip_make_rlt","w+")
IP.load(os.path.abspath('/Users/haoshun/hs-code-test/sta_bridge_log/ip_sta/ip_location.dat'))
for line in open("/Users/haoshun/hs-code-test/bridge_temporary_code/hs_win_21_head"):
    try:
        line = line.strip()
        jsonObj = json.loads(line)
        auction = jsonObj['auction']
        winDict[auction]={"win"}
    except:
        continue
for line in open("/Users/haoshun/hs-code-test/bridge_temporary_code/hs_clk_21_head"):
    try:
        line = line.strip()
        jsonObj = json.loads(line)
        auction = jsonObj['auction']
        clkDict[auction]={"clk"}
    except:
        continue
for line in open("/Users/haoshun/hs-code-test/bridge_temporary_code/hs_pv_21_head"):
    try:
        line = line.strip()
        jsonObj = json.loads(line)
        auction = jsonObj['auction_id']
        make = jsonObj['input']['device']['make']
        ip = jsonObj['input']['device']['ip']
        pvDict[auction]={"make":make,"ip":ip}
    except:
        continue
for k,v in pvDict.items():
    try:
        make = v['make']
        ip = v['ip']
        ippro = IP.find(ip).split("\t")[1]
        ipcity = IP.find(ip).split("\t")[2]
        if clkDict.get(k,None)!=None and winDict.get(k,None)!=None:
            staDict[k]={"make":make,"pro":ippro,"city":ipcity,"wins":1,"clks":1}
        elif clkDict.get(k,None)==None and winDict.get(k,None)!=None:
            staDict[k]={"make":make,"pro":ippro,"city":ipcity,"wins":1,"clks":0}
        elif clkDict.get(k,None)!=None and winDict.get(k,None)==None:
            staDict[k]={"make":make,"pro":ippro,"city":ipcit,"wins":0,"clks":1}
        else:
            staDict[k]={"make":make,"pro":ippro,"city":ipcity,"wins":0,"clks":0}
    except:
        continue
for key,val in staDict.items():
    make = val['make']
    pro = val['pro']
    city = val['city']
    wins = val['wins']
    clks = val['clks']
    pk = "%s\t%s\t%s" % (make,pro,city)
    if rltDict.get(pk,None)==None:
        rltDict[pk]={"wins":wins,"clks":clks}
    else:
        rltDict[pk]['wins']+=wins
        rltDict[pk]['clks']+=clks
for ke,va in rltDict.items():
    ke_line = ke.split("\t")
    make = ke_line[0].encode('utf-8')
    pro = ke_line[1].encode('utf-8')
    city = ke_line[2].encode('utf-8')
    f.write("%s\t%s\t%s\t%s\t%s\n" % (make,pro,city,va['wins'],va['clks']))
