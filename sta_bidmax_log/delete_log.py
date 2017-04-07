#!/usr/python 
#!-*- coding: utf-8 -*-
import os
import time
last_49_hour = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600*49))
print last_49_hour
bwc_path='/home/work/disk/nhs/dingxiang/'
sta_path='/home/work/disk/nhs/dingxiang/log/'

cmd_bwc = 'rm -rf ' + bwc_path +'*'+last_49_hour+'.log'
print cmd_bwc
os.system(cmd_bwc)
cmd_sta = 'rm -rf ' + sta_path +'*'+last_49_hour
print cmd_sta
os.system(cmd_sta)
