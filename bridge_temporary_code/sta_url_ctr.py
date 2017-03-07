#!/usr/bin/python
#!-*- coding: utf-8 -*-
import json
bidDict={}
winDict={}
clkDict={}
staDict={}
rltDict={}
#bid message
bid_path = '/home/work/log/bridge/pv/hs_bid_head'
for bid_line in open(bid_path):
    if "SUCCESS" in bid_line:
        bid_jsonObj = json.loads(bid_line)
        auction_id = bid_jsonObj['auction_id']
        if "impnative" in bid_line:
            iurl = bid_jsonObj['rsp']['adsimp'][0]['impnative']['adslot']['image'][0]['iurl']
            bidDict[auction_id]={"iurl":iurl}
        else:
            continue
    else:
        continue
#win message
win_path = '/home/work/log/bridge/pv/hs_win_head'
for win_line in open(win_path):
    win_jsonObj = json.loads(win_line)
    auction_id = win_jsonObj['auction']
    winDict[auction_id]={"wins":"win"}
#click message
clk_path = '/home/work/log/bridge/pv/hs_click_head'
for clk_line in open(clk_path):
    clk_jsonObj = json.loads(clk_line)
    auction = clk_jsonObj['auction']
    clkDict[auction]={"clks":"clk"}
#join bid win click and statistic
for k,v in bidDict.items():
    iurl = v["iurl"]
    if winDict.get(k,None)!=None and clkDict.get(k,None)!=None:
        staDict[k]={"iurl":iurl,"bids":1,"wins":1,"clks":1}
    elif winDict.get(k,None)!=None and clkDict.get(k,None)==None:
        staDict[k]={"iurl":iurl,"bids":1,"wins":1,"clks":0}
    elif winDict.get(k,None)==None and clkDict.get(k,None)!=None:
        staDict[k]={"iurl":iurl,"bids":1,"wins":0,"clks":1}
    else:
        staDict[k]={"iurl":iurl,"bids":1,"wins":0,"clks":0}
#read staDict
for key,val in staDict.items():
    auction = key
    iurl = val["iurl"]
    bids = val["bids"]
    wins = val["wins"]
    clks = val["clks"]
    if rltDict.get(iurl,None)==None:
        rltDict[iurl]={"bids":bids,"wins":wins,"clks":clks}
    else:
        rltDict[iurl]["bids"]+=bids
        rltDict[iurl]["wins"]+=wins
        rltDict[iurl]["clks"]+=clks
for ke,va in rltDict.items():
    iurl = ke
    bids  = va["bids"]
    wins = val["wins"]
    clks = val["clks"]
#    print "%s\t%s\t%s" % (iurl,bids,wins)
    print "%s\t%s\t%s\t%s" % (key,val["bids"],val["wins"],val["clks"])
