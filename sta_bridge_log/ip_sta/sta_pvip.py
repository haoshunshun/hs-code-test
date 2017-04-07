#!/usr/bin/python
#!-*- coding: utf -8 -*-
import json
import os
from ipip import IP
pv_ip_rlt=open('head_rlt','w+')
IP.load(os.path.abspath('/Users/haoshun/hs-code-test/sta_bridge_log/ip_sta/ip_location.dat'))
try:
    for file in open("hs_tmp_0301"):
        jsonObj = json.loads(file)
        ip = jsonObj['input']['device']['ip']
        iprlt = IP.find(ip)
        pv_ip_rlt.write("%s\n" % (iprlt.encode('utf-8')))
except Exception as ex:
    print ex.message
