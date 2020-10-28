import imaplib
import re
import email
#coding=UTF-8

def email_1(email_id,password_2,host_qq):
    '''imap server '''
    #create object
    imapobj=imaplib.IMAP4_SSL(host_qq,993)

    #login
    imapobj.login(email_id,password_2)

    #check file(INBOX) email 
    imapobj.select('INBOX')
    #print(INBOX)

    #all email a list have space 
    typ,data=imapobj.search(None,'ALL')
    # print(typ,data)

    #a new list without space
    newlist=data[0].split()
    print(len(newlist))

    #the first email is -1 of list
    # lastemail=messagelist[len(messagelist)-1]
    # print(lastemail)

    # #ȡ���һ���ʼ���д��txt
    
    # typ, datas = imapobj.fetch(lastemail, '(RFC822)')
    # #��ȡ�������ʼ�д��txt�ĵ�
    # with open('email.txt','w')as f:
    #     f.write(datas[0][1].decode('gbk'))
    
    #the first email is last of list
    first_email=newlist[len(newlist)-4]
    print(first_email)

    #use fetch function to get email
    typ,datas=imapobj.fetch(first_email,'(RFC822)')

    # jie xi email use UTF-8
    message=email.message_from_string(datas[0][1].decode('utf-8'))
    # with open('email.txt','w') as fo:
    #     fo.write(datas[0][1].decode('gbk'))
    
    #get the title 
    sub=message.get('subject')
    subdecode=email.header.decode_header(sub)[0][0]
    print(subdecode)

    #for the part of email  
    for file_part in message.walk():
        if not file_part.is_multipart():            
            youjian=file_part.get_payload(decode='True').decode('UTF-8')
            
    
    with open('email.txt','w') as fobj:
        fobj.write(youjian)
        fobj.close()

    with open('email.txt','r') as fo:
        a=fo.read()
        fo.close()
    
    yanzhengRegex=re.compile(r'\:\s\d\d\d\d')
    mo1=yanzhengRegex.findall(a)
    if mo1:
        wenben=mo1[0]
        shuziRegex=re.compile(r'\d\d\d\d')
        mo2=shuziRegex.findall(wenben)
        if len(mo2)==1:
            yanzhengma=mo2[0]
            print(yanzhengma)
            return yanzhengma
        else:
            print('lost file')        
    else:
        print('error!')


print(email_1("carlos.wang@feisu.com", "Ww1300202481", "imap.exmail.qq.com"))
    