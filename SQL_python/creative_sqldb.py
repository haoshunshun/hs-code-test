#!/usr/bin/python
#!-*- coding: utf-8 -*-

import MySQLdb
connect = MySQLdb.connect(host="host ip",user="user name",passwd="pass word",db="db name")
cursor = connect.cursor()
cursor.execute("drop table if exists table_name")
sql = """create table table_name (
index_name index_type NOT NULL,
index_name index_type NOT NULL,
bids int) """
#default charset = utf8
cursor.execute(sql)
cursor.close()
connect.close()
