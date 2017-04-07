#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
import hashlib
import MySQLdb
last_hour = time.strftime("%Y-%m-%d_%H",time.localtime(time.time()-3600))
bidDict={}
staDict={}
time_tuple = time.strptime(last_hour,"%Y-%m-%d_%H")
lastTimeBlockStamp = int(time.mktime(time_tuple))
bid_path = '/home/work/run_env/DEPLOY/ssp-report/input/bid.'+last_hour+'.log'
for bid_line in open(bid_path):
    try:
        if "SUCCESS" in bid_line:
			if "impnative" in bid_line:
				bid_jsonObj = json.loads(bid_line)
				adspot_id = bid_jsonObj['adspot_id']
				app_id = bid_jsonObj["app_id"]
				auction_id = bid_jsonObj['auction_id']
				supplier = bid_jsonObj['supplier_id']
				adsimp = bid_jsonObj['rsp']['adsimp'][0]
				image = adsimp['impnative']['adslot']['image'][0]
				iurl = image['iurl']
				word = adsimp['impnative']['adslot']['word'][0]
				cnt = word['cnt']
				m = hashlib.md5()
				m.update(iurl)
				iurlMd5 = m.hexdigest()
				m.update(cnt.encode("utf8"))
				cntMd5 = m.hexdigest()
			else:
				bid_jsonObj = json.loads(bid_line)
				adspot_id = bid_jsonObj['adspot_id']
				app_id = bid_jsonObj["app_id"]
				auction_id = bid_jsonObj['auction_id']
				supplier = bid_jsonObj['supplier_id']
				adsimp = bid_jsonObj['rsp']['adsimp'][0]
				iurl = adsimp['impbanner']['iurl']
				cnt = "banner_no_word"
				m = hashlib.md5()
				m.update(iurl)
				iurlMd5 = m.hexdigest()
				m.update(cnt)
				cntMd5 = m.hexdigest()
			pk = "%s\t%s\t%s\t%s\t%s" % (app_id,adspot_id,iurlMd5,cntMd5,supplier)
			if bidDict.get(pk,None)==None:
				bidDict[pk]={"iurl":iurl,"cnt":cnt,"bids":1}
			else:
				bidDict[pk]["iurl"]=iurl
				bidDict[pk]["cnt"]=cnt
				bidDict[pk]["bids"]+=1
        else:
			continue
    except Exception ,e:
		continue
for k,v in bidDict.items():
    kspl = k.strip().split("\t")
    app_id = kspl[0]
    adspot_id = kspl[1]
    iurlMd5 = kspl[2]
    cntMd5 = kspl[3]
    supplier = kspl[4]
    iurl = v["iurl"]
    cnt = v["cnt"]
    bids = v["bids"]
    db = MySQLdb.connect(host='192.168.3.38',user='report',passwd='Bayescomrpt100w',db='statisticreport',charset='utf8')
    cursor = db.cursor()
    cursor.execute("insert into bid_iurl_rlt values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",[lastTimeBlockStamp,app_id,adspot_id,iurlMd5,cntMd5,supplier,bids,iurl,cnt])
    db.commit()
    cursor.close()
    db.close()
