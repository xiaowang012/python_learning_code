#coding=utf-8
import imaplib
import email
import re


#imap收件服务器获取邮件，并找出其中的验证码
def email_1(email_id,password_2,host_qq):
    '''imap server '''
    #create object
    imapobj=imaplib.IMAP4_SSL(host_qq,993)

    #login
    imapobj.login(email_id,password_2)

    #收邮件选择文件夹(默认参数为INBOX，可填可不填，邮箱的默认文件夹也是这个)
    imapobj.select('INBOX')
    #print(INBOX)

    #全部邮件，返回一个[1 2 3 4 5...],为邮件的编号，按时间升序排列，中间有空格
    typ,data=imapobj.search(None,'ALL')
    # print(typ,data)

    #邮件列表，将上面的带空格的数据表中的空格去掉然后放到新列表newlist中，这个即为邮件列表
    newlist=data[0].split()
    print(len(newlist))

    #最后一封邮件
    # lastemail=messagelist[len(messagelist)-1]
    # print(lastemail)

    # #取最后一封邮件并写入txt
    
    # typ, datas = imapobj.fetch(lastemail, '(RFC822)')
    # #把取回来的邮件写入txt文档
    # with open('email.txt','w')as f:
    #     f.write(datas[0][1].decode('gbk'))
    
    #读取第一封邮件,最近的邮件是-1，（这里是第四封邮件）
    first_email=newlist[len(newlist)-4]
    print(first_email)

    #用fetch函数取回第一封邮件
    typ,datas=imapobj.fetch(first_email,'(RFC822)')

    #email库处理邮件
    message=email.message_from_string(datas[0][1].decode('utf-8'))
    # with open('email.txt','w') as fo:
    #     fo.write(datas[0][1].decode('gbk'))
    
    #解析邮件
    #取出标题信息
    sub=message.get('subject')
    subdecode=email.header.decode_header(sub)[0][0]
    print(subdecode)

    #正文,遍历整个邮件
    for file_part in message.walk():
        if not file_part.is_multipart():            
            youjian=file_part.get_payload(decode='True').decode('UTF-8')
            #print(youjian)
            # 解码出文本内容，直接输出来就可以了。
    
    #利用正则表达式找出验证码，注意(: 2131)为中文字符的冒号
    yanzhengmaRegex=re.compile(r'\：\d\d\d\d')
    mo1=yanzhengmaRegex.findall(youjian)
    yanzhengmaRegex_2=re.compile(r'\d\d\d\d')
    if len(mo1)==1:
        #print('验证码：'+str(mo1[0]))
        wenben=str(mo1[0])
        mo2=yanzhengmaRegex_2.findall(wenben)
        if len(mo2)==1:
            yanzhengma=str(mo2[0])
            #print('验证码：'+yanzhengma)
            return yanzhengma
        else:
            print('ERROR!')
    else:
        print('ERROR')


    


print(email_1('carlos.wang@feisu.com','Ww1300202481','imap.exmail.qq.com'))
