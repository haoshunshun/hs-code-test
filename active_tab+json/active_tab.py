#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
last_hour = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600))
print last_hour
last_Hour = time.strftime("%Y-%m-%d %H",time.localtime(time.time()-3600))
#2016-10-28 03:56:20>58d3093f4e01cbdc>---active>-3_001_error
activePath = '/home/work/hs/active_log/active.'+last_hour+'.log'
nf = open('/home/work/hs/active_log/nactive.'+last_hour+'.log','w+')
for line in open(activePath):
    line_str = line.strip("\r\n").split("\t")
    time = line_str[0]
    if last_Hour in time:
        nf.write("%s\t%s\t%s\t%s\n" % (line_str[0],line_str[1],line_str[2],line_str[3]))
    else:
        continue
        

