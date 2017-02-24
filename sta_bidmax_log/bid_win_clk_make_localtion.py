#!/usr/python
#-*- coding: utf-8 -*-

import time
import sys
file_rlt = open("rlt_finall","w+")
#last_hour = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600)
file2 = '/Users/haoshun/hs-code-test/sta_bidmax_log/damaojiakao/bid.damao.log'
file3 = '/Users/haoshun/hs-code-test/sta_bidmax_log/damaojiakao/win.damao.log'
file4 = '/Users/haoshun/hs-code-test/sta_bidmax_log/damaojiakao/click.damao.log'
clkDict={}
winDict={}
bidDict={}
staDict={}
rltDict={}
for raw_line in open(file4):
    clk_line = raw_line.strip().split('\t')
    auction = clk_line[2]
    clkDict[auction]={"clk"}
for raw_line in open(file3):
    win_line = raw_line.strip().split('\t')
    auction = win_line[2]
    winDict[auction]={"win"}
for raw_line in open(file2):
    bid_line = raw_line.strip().split('\t')
    bid_mes = bid_line[2].split("\001")
    auction = bid_mes[0]
    make = bid_mes[22].split(":")[3]
    pro = bid_mes[23].split(":")[1]
    city = bid_mes[23].split(":")[2]
    bidDict[auction]={"make":make,"pro":pro,"city":city}
for k,v in bidDict.items():
    make = v['make']
    pro = v['pro']
    city = v['city']
    if winDict.get(k,None)!=None and clkDict.get(k,None)!=None:
        staDict[k]={"make":make,"pro":pro,"city":city,"wins":1,"clks":1}
    elif winDict.get(k,None)==None and clkDict.get(k,None)!=None:
        staDict[k]={"make":make,"pro":pro,"city":city,"wins":0,"clks":1}
    elif winDict.get(k,None)!=None and clkDict.get(k,None)==None:
        staDict[k]={"make":make,"pro":pro,"city":city,"wins":1,"clks":0}
    else:
        staDict[k]={"make":make,"pro":pro,"city":city,"wins":0,"clks":0}
for k,v in staDict.items():
    make = v["make"]
    pro = v["pro"]
    city = v["city"]
    wins = v["wins"]
    clks = v["clks"]
    pk = "%s\t%s\t%s" % (make,pro,city)
    if rltDict.get(pk,None)==None:
        rltDict[pk]={"wins":wins,"clks":clks}
    else:
        rltDict[pk]['wins']+=wins
        rltDict[pk]['clks']+=clks
for k,v in rltDict.items():
    wins = v["wins"]
    clks = v["clks"]
    file_rlt.write("%s\t%s\t%s\n" % (k,wins,clks))
