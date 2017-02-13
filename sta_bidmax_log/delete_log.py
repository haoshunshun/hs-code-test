#!/usr/python 
#!-*- coding: utf-8 -*-
import os
import time
last_49_hour = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600*49))
#last__hour = time.strftime("%Y%m%d%H",time.localtime(time.time()-3600*169))
print last_49_hour
bwc_path='/home/work/disk/nhs/dingxiang/'
#bid_path='/home/work/disk/nhs/dingxiang/bid.'+last_25_hour+'.log'
#win_path='/home/work/disk/nhs/dingxiang/win.'+last_25_hour+'.log'
#click_path='/home/work/disk/nhs/dingxiang/click.'+last_25_hour+'.log'
#active_path='/home/work/disk/nhs/dingxiang/active.'+last_25_hour+'.log'
sta_path='/home/work/disk/nhs/dingxiang/log/'
#dingxiang_path='/home/work/disk/nhs/dingxiang/log/join_'+last_25_hour
#result_path='/home/work/disk/nhs/dingxiang/log/result_'+last_25_hour

cmd_bwc = 'rm -rf ' + bwc_path +'*'+last_49_hour+'.log'
print cmd_bwc
os.system(cmd_bwc)
cmd_sta = 'rm -rf ' + sta_path +'*'+last_49_hour
print cmd_sta
os.system(cmd_sta)
