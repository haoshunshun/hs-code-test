#!/usr/bin/python
#!-*- coding: utf-8 -*-
import json
import sys
import time
import hashlib
reload(sys)
sys.setdefaultencoding('utf8')
bidDict={}
for bid_line in sys.stdin:
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
for key,val in bidDict.items():
    print "%s\t%s\t%s\t%s" % (key,val['iurl'],val['cnt'],val['bids'])
