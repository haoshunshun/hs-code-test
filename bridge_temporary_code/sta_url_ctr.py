#!/usr/bin/python
#!-*- coding: utf-8 -*-
import json
bidDict={}
winDict={}
clkDict={}
staDict={}
#bid message
bid_path = '/Users/haoshun/hs-code-test/sample_data/bridge_bid'
for bid_line in open(bid_path):
	if "SUCCESS" in bid_line:
		try:
			bid_jsonObj = json.loads(bid_line)
			auction_id = bid_jsonObj['auction_id']
			if "impnative" in bid_line:
				iurl = bid_jsonObj['rsp']['adsimp'][0]['impnative']['adslot']['image'][0]['iurl']
			else:
				iurl = bid_jsonObj['rsp']['adsimp'][0]['impbanner']['iurl']
				bidDict[auction_id]={"iurl":iurl}
		except:
			continue
	else:
		continue
#win message
win_path = '/Users/haoshun/hs-code-test/sample_data/bridge_win'
for win_line in open(win_path):
	win_jsonObj = json.loads(win_line)
	auction_id = win_jsonObj['auction']
	winDict[auction_id]={"wins":"win"}
#click message
clk_path = '/Users/haoshun/hs-code-test/sample_data/bridge_click'
for clk_line in open(clk_path):
	clk_jsonObj = json.loads(clk_line)
	auction = clk_jsonObj['auction']
	clkDict[auction]={"clks":"clk"}
#join bid win click and statistic
clks = 0
wins = 0
for k,v in bidDict.items():
	iurl = v["iurl"]
	if winDict.get(k,None)!=None:
		wins += 1
		if clkDict.get(k,None)!=None:
			clks += 1
		else:
			clks += 0
	else:
		wins += 0
	staDict[iurl]={"wins":wins,"clks":clks}
#read staDict
for key,val in staDict.items():
	print "%s\t%s\t%s" % (key,val["wins"],val["clks"])
