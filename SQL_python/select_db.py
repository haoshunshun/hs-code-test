#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb
#创建新文件
file_name = open("/home/work/disk/nhs/dingxiang/scripts/sql_test","w+")
# 打开数据库连接
connect = MySQLdb.connect(host="192.168.3.38",user="report",passwd="Bayescomrpt100w",db="statisticreport")
#获取操作游标
cursor = connect.cursor()
#获取当前时间的时间戳
time_stamp_now=int(time.time())
print time_stamp_now
#获取上一小时的时间戳
time_stamp_hour = time_stamp_now - (time_stamp_now%3600) - 3600
print time_stamp_hour
#执行sql查询操作
cursor.execute("SELECT timestamp,app_id,sum(bids) FROM sqlTest where timestamp=2017021510 group by app_id order by bids desc limit 20")
#获取所有记录列表
result = cursor.fetchall()
for row in result:
    time = row[0]
    app_id = row[1]
    bids = row[2]
    #打印结果
    #print "%s,%s,%s" % (time,app_id,bids)
    #写入新文件
    file_name.write("%s,%s,%s\n" % (time,app_id,bids))    
cursor.close()
connect.close()
