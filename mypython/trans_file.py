#!/usr/bin/env os
#coding:utf-8

import sys
import pdb

reload(sys)
sys.setdefaultencoding('utf-8')

src_file = sys.argv[1]
dst_file = 'new_' + src_file

width = 30

with open(src_file) as rf,open(dst_file,'wb+') as wf:
    for line in rf:
        dline = line.decode('utf-8').strip()
        length = len(dline)
        full_line = length / width
        left_content = length % width
        begin = 0
        end = width

        for i in range(full_line):  
            wf.write(dline[begin:end] + '\r\n\r\n')
            begin += width
            end += width


        if full_line == 0:
            end = 0
        wf.write(dline[end:] + '\r\n\r\n')




