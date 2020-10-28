#coding=utf-8
import poplib
import email
from time import sleep

'''
pop3收件服务器
接收邮件服务器：pop.exmail.qq.com ，使用SSL，端口号995'''

def pop3_rec_email(username,password,server_email):
    '''一个使用pop3收件服务器接收邮件'''
    #修改最大长度限制
    poplib._MAXLINE=20480
    #连接pop3收件服务器
    popobj=poplib.POP3_SSL(server_email,port=995)
    sleep(2)

    #设置调试级别（可看到与服务器的交互信息）
    #popobj.set_debuglevel(1)

    #输入账户和密码
    popobj.user(username)
    popobj.pass_(password)

    #获取pop3服务器的欢迎信息,并打印出来
    print(popobj.getwelcome())

    #获取所有的邮件信息，返回一个列表，第一个参数是邮件数量，第二个参数为邮件大小（bytes）
    list_email=popobj.stat()
    #print(list_email)
    
    #取出所有信件的头部，信件ID从1开始
    for x in range(1,list_email[0]+1):
        new_list=popobj.top(x,1)
        #print(len(new_list[1]))
    
    #列出服务器上的邮件信息，对每一封邮件输出ID和大小
    message_email=popobj.list()
    #print(message_email)

    #获取第一封邮件的完整信息
    #在返回值中，是按行储存在down[1]列表里
    #down[0]是状态信息
    down=popobj.retr(1)
    #print('长度：'+str(len(down)))

    #输出邮件信息
    for line in down[1]:
        print(line)
    
    #推出邮箱
    popobj.quit()

# # 需要取出所有信件的头部，信件id是从1开始的。
# for i in range(1, ret[0]+1):
#     # 取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行，
#     # 其实是返回头部信息，取1行其实是返回头部信息之外再多1行。
#     mlist = pp.top(i, 0)
#     print 'line: ', len(mlist[1])
# # 列出服务器上邮件信息，这个会对每一封邮件都输出id和大小。不象stat输出的是总的统计信息
# ret = pp.list()
# print ret
# # 取第一封邮件完整信息，在返回值里，是按行存储在down[1]的列表里的。down[0]是返回的状态信息
# down = pp.retr(1)
# print 'lines:', len(down)
# # 输出邮件
# for line in down[1]:
#     print line
# # 退出
# pp.quit()

pop3_rec_email('carlos.wang@feisu.com','Ww1300202481','pop.exmail.qq.com')

