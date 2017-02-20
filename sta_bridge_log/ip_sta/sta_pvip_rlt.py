#!/usr/bin/python 
#!-*- coding: utf-8 -*-

staDict={}
f_rlt = open('ip_result_finnal','w+')
for line in open('head_rlt'):
    lineStr = line.rstrip("\r\n").split("\t")
    if len(lineStr)>=3:
        con = lineStr[0]
        pro = lineStr[1]
        city = lineStr[2]
        pk = "%s\t%s\t%s" % (con,pro,city)
    else:
        continue
    if staDict.get(pk,None)==None:
        staDict[pk]={"ip":1}
    else:
        staDict[pk]["ip"]+=1
for k,v in staDict.items():
    f_rlt.write("%s\t%s\n" % (k,v["ip"]))
f_rlt.close()

