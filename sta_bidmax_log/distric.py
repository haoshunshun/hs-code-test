#!/usr/bin/python
# -*- coding: utf-8 -*-
dis_rlt = open('district_file','w+')
for line in open("location.txt"):
    if "dsp_id" or "name" in line:
        dis_rlt.write("%s\n" % (line))

