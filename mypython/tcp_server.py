#!/usr/bin/env python
#coding:utf-8
import sys
import SocketServer
import os
import time

dst_path = sys.argv[1]
class myserver(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = os.path.join(dst_path)
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        conn = self.request
        print('connected...')
        recv_buf = 32*1024
        while True:
            pre_data = conn.recv(128)
            if not pre_data:
                return
            file_name,file_size_str = pre_data.split('|')
            file_size =(int)(file_size_str)
            recv_size = 0
            file_dir = os.path.join(base_path,file_name+'.bak')
            conn.sendall('send file please.')
            f = open(file_dir,'wb')
            while True:
                if file_size > recv_size:
                    max_recv_size = min(recv_buf,file_size-recv_size)
                    data = conn.recv(max_recv_size)
                    recv_size += len(data)
                else:
                    break
                f.write(data)
            print(file_name+' received')
            f.close()

if __name__ == '__main__':
    #SocketServer.ThreadingTCPServer.allow_reuse_address = True
    #print SocketServer.ThreadingTCPServer.timeout
    #instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9000),myserver)
    
    SocketServer.ForkingTCPServer.allow_reuse_address = True
    print SocketServer.ForkingTCPServer.timeout
    SocketServer.ForkingTCPServer.timeout = 60
    instance = SocketServer.ForkingTCPServer(('127.0.0.1',9000),myserver)

    instance.serve_forever()
 
