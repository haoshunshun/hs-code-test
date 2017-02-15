#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
db = MySQLdb.connect(host="192.168.3.38",user="report",passwd="Bayescomrpt100w",db="statisticreport")
cursor = db.cursor()
#cursor.execute('drop table if exists bid_iurl_rlt')
sql = """CREATE TABLE sql_test (
    timeStamp text NOT NULL,
    app_id text NOT NULL,
    adspot_id text NOT NULL,
    iurlMd5 text NOT NULL,
    cntMd5 text NOT NULL,
    supplier INT NOT NULL,
    bids INT,
    iurl text,
    word text) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
cursor.execute(sql)
cursor.close()
db.close()
