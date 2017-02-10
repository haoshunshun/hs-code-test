#!/usr/bin/python
#!-*- coding:utf-8 -*-

import os
import re
import string
import sys
import json
import time
from datetime import datetime
from operator import itemgetter

def calLogFileMapper(lineNum,formatStr):
 

#BID>2016-Jul-25 10:00:00.06066>-3bbd93874fc758aa^A648424289712834755^A   >-  
#WIN>2016-Jul-25 10:00:00.94186>-1b6a76454758f84d>---8852597722868189411>35540CNY/1M>38370582
#CLICK>--2016-Jul-25 10:00:12.53868>-cbbb8d3a4638add9>---9439330309166329090>1_70001_19_daily
#2016-08-09 00:02:38,836>6a57c6824694bebc>---active>-cellphone:18786869192 
    for raw_line in sys.stdin:
        line = raw_line.rstrip("\r\n").strip().split("\t")
        if line[0] == "BID":
            logType = 'bid'
            if len(line)>=4:
                message = "%s\001%s" % (line[2],line[3])
                auction = message.split("\001")[0]
                logTime = line[1]
                value = (message)
            else:
                auction = line[2].split("\001")[0]
                logTime = line[1]
                message = line[2]
                value = (message)
        elif line[0]=="WIN":
            logType = 'win'
            if len(line)<6:
                continue
            else:
                auction = line[2]
                price = line[4]
                logTime = line[1]
                value = (price)
        elif line[0]=="CLICK":
            if len(line)<5:
                continue
            else:  
                auction = line[2]
                click_time = line[1]
                logType = 'click'
                value = (click_time)
                logTime = line[1]
        else:
            if len(line)<4:
                continue
            else:
                auction = line[1]
                phone = line[3]
                logType = 'active'
                Time = line[0]
                TimeArray = time.strptime(Time,"%Y-%m-%d %H:%M:%S,%f")
                logTime = time.strftime("%Y-%b-%d %H:%M:%S",TimeArray)
                value = (phone)

        key = (auction)
        seprate =('\t')
        valueSeq = (logTime,logType,value)  
        val = seprate.join(valueSeq)

        print '%s\t%s' % (key,val)

if __name__ == '__main__' :
   calLogFileMapper(14,"%Y-%b-%d %H")

   
