import smtplib
from email.mime.text import MIMEText
from email.header import Header
import re

# -*- coding: utf-8 -*-
#smtp发件服务器发送邮件
#smtp邮件服务器为smtp.exmail.qq.com(使用SSL，端口号465)

def smtp_send_email(username,password,server_email,recive_email):  
    '''一个smtp发件服务器发送邮件的实例'''
    #发送的邮箱
    sender=username
    #接收的邮箱
    receivers=[recive_email]
    
    #发送的邮件正文
    message=MIMEText('邮件标题xxxxx','plain','utf-8')

    #发件人
    message['From']=Header('wangli','utf-8')

    #收件人
    message['To']=Header('hhhhhh','utf-8')
    
    #标题
    subject='this is a title.'
    message['Subject']=Header(subject,'utf-8')

    #发送，一个对象
    try:
        sendemail_obj=smtplib.SMTP()
        sendemail_obj.connect(server_email,25)
        sendemail_obj.login(username,password)
        sendemail_obj.sendmail(sender,receivers,message.as_string())
    except smtplib.SMTPException:
        print('ERROER!')
        
smtp_send_email('carlos.wang@feisu.com','Ww1300202481','smtp.exmail.qq.com','3007665895@qq.com')
