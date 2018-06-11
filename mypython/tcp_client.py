#!/usr/bin/env python
#coding:utf-8

import socket
import sys
import os
import time

ip_port = ('127.0.0.1',9000)
src_path = sys.argv[1]
time_now = (int)(time.time())
scan_path = '/tmp/%s' %time_now

os.system('cp -ar %s %s' %(src_path,scan_path))
print scan_path
while True:
    try:
        sk = socket.socket()
        sk.connect(ip_port)
        socket_buf = 32*1024
        while True:
            try:
                for root,_,files in os.walk(scan_path):
                    cur = time.time()
                    for name in files:
                        if name[0] == '.':
                            continue
                        file_name = os.path.join(root,name)
                        file_size = os.stat(file_name).st_size
                        print file_name
                        sk.sendall(name + '|' + str(file_size))
                        data = sk.recv(128)
                        with open(file_name,'rb') as f:
                            while True:
                                data = f.read(socket_buf)
                                sk.send(data)
                                if len(data) == 0:
                                    break
                        os.unlink(file_name)
                        print time.time()-cur
                        cur = time.time()
            except Exception as e:
                print '11111111:',e
                sk.close()
                break
    except Exception as e:
        print e
        time.sleep(1)
