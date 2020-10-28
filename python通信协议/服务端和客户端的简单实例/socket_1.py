#coding=utf-8
import socket

#套接字，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。
#一个简单的服务端的实例

#创建一个socket对象
s=socket.socket()

#host,获取本地主机名
host=socket.gethostname()

#设置端口
port=1111

#绑定端口
s.bind((host,port))

#等待客户端连接
s.listen(5)

while True:
    c,addr=s.accept() #建立客户端连接
    print('连接地址：'+str(addr))
    c.send(b'user:123456')
    c.send(b'psw:abcdefg')
    c.close()


