#coding=utf-8

import socket

#一个客户端的实例

#创建socket对象
s=socket.socket()

#获取本地主机名
host=socket.gethostname()

#设置端口号
prot=1111

#连接服务端
s.connect((host,prot))

#读取1024bit的数据
print(s.recv(101))

#关闭连接
s.close()