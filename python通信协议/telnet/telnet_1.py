#coding=utf-8

from telnetlib import Telnet
from time import sleep

'''一个简单得telnet 协议的实例
tn对象的方法:

tn.read_until(b'xxx',timeout=x)直到阅读到指定的字符串，或者超时
tn.read_all() 读取所有数据直到EOF
tn.read_some() 至少读取一个数据
tn.read_very_eager() 阅读所有可以在I / O（热切）中不受阻塞的内容。
tn.read_eager() 读取随时可用的数据
tn.read_lazy() 处理并返回队列中已有的数据
tn.read_very_lazy()  返回已熟练队列中的任何数据（very lazy）
tn.read_sb_data() 返回SB / SE对之间收集的数据（子选项开始/结束）
tn.set_debuglevel(level) 设置调试级别，level值越高，获得的调试输出就越多
tn.close() 关闭连接
tn.get_socket() 返回内部使用的套接字对象
tn.fileno() 返回内部使用的套接字对象的文件描述符
tn.write(buffer) 将字符串写入套接字
'''



def tel_2(host,user,passw,port,timoout):
    '''telnet'''
    try:
        tn=Telnet(host)
        tn.open(user,passw,port,timeout)
    except:
        print('error1!')
    else:
        sleep(2)
        try:  
            tn.read_until(b'username',timeout=5)
            tn.write(user.encode('ascii')+b'\n')
            tn.read_until(b'password',timeout=5)
            tn.write(passw.encode('ascii')+b'\n')
        except:
            print('user or psw error!')
        else:
            
            try:
                tn.read_until(b'switch#',timeout=5)
            except:
                print('login error')
            else:
                return True

tel_2('192.168.1.1','admin','admin',23,10)