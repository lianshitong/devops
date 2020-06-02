#!/usr/bin/env python
#coding:utf-8

import socket


def net_is_used(port,ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        s.shutdown(2)
        print('{}:{} is used'.format(ip,port))
        return True
    except:
        print('{}:{} is unused'.format(ip,port))
        return False


if __name__ == '__main__':
    # ip_list = []
    ip_list = input('Please input ip:')
    print(ip_list)
    for i in ip_list:
        net_is_used(22,i)
        print(i)
