#!/bin/bash
#!-*- coding: utf-8 -*-
last_hour=`date +"%Y%m%d%H" -d "-1 hour"` 
echo ${last_hour}
#limit speed scp from bidmax005 to nhs@bj-rd
scp -l 200000 work@192.168.13.177:/home/work/run_env/DEPLOY/BidMax/Logger/log/bid.${last_hour}.log /home/work/disk/nhs/dingxiang/
scp -l 200000 work@192.168.13.177:/home/work/run_env/DEPLOY/BidMax/Logger/log/win.${last_hour}.log /home/work/disk/nhs/dingxiang/
scp -l 200000 work@192.168.13.177:/home/work/run_env/DEPLOY/BidMax/Logger/log/click.${last_hour}.log /home/work/disk/nhs/dingxiang/
