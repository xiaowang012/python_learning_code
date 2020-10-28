
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import imaplib
import email
import re
import json
import sys
import keyboard
#coding=UTF-8

# def start_1(url,username,password):
#      '''Browser for firefox'''
#      browser=webdriver.Firefox()
#      browser.maximize_window()
   
#      #login
#      browser.get(url)
#      sleep(3)
#      window=browser.current_window_handle
#      print('old_handle:'+str(window))
#      ele=browser.find_element_by_id('username')
#      ele.clear()
#      ele.send_keys(username)
#      ele_1=browser.find_element_by_id('password')
#      ele_1.clear()
#      ele_1.send_keys(password)
#      ele_1.submit()
#      sleep(10)
#      try:
#          ele_2=browser.find_element_by_id('code')
#      except:
#          pass
#      else:
#          try:
#              sleep(7)
#              yanzhengma=email_1(email_id,password_2,host_qq)
#          except:
#              print('return error')
#              sys.exit()
#          else:
#              ele_2.clear()
#              ele_2.send_keys(yanzhengma)
#              ele_2.submit()
#      sleep(5)
#      #click erp use JS language
#      js = "document.getElementsByClassName('icon iconfont')[1].click();"
#      browser.execute_script(js)
#      sleep(5)

#      #window handles
#      handles=browser.window_handles
#      print(handles)
#      if len(handles)==2:
#          browser.switch_to_window(handles[-1])
#      else:
#          print('Error!')
     
        

#      #click the Quality center 
#      ele_4=browser.find_element_by_id('p_menu_50')
#      ele_4.click()
#      sleep(1)

#      #click the order 
#      ele_5=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/ul/li[1]/a')
#      ele_5.click()

def start_2(url,username,password):
     '''Browser for chrome'''
     chrome_options = webdriver.ChromeOptions(); 
     chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
     browser = webdriver.Chrome(options=chrome_options)
     browser.maximize_window()
     
     #login
     browser.get(url)
     window=browser.current_window_handle
     print('old_handle:'+str(window))
     ele=browser.find_element_by_id('username')
     ele.clear()
     ele.send_keys(username)
     ele_1=browser.find_element_by_id('password')
     ele_1.clear()
     ele_1.send_keys(password)
     ele_1.submit()
     sleep(10)
     try:
         ele_2=browser.find_element_by_id('code')
     except:
         pass
     else:
         try:
             sleep(15)
             yanzhengma=email_1(email_id,password_2,host_qq)
         except:
             print('can not find the code from email！')
             sys.exit()
         else:
             ele_2.clear()
             ele_2.send_keys(yanzhengma)
             ele_2.submit()
     sleep(5)
     #click erp system and use the JS laguage
     js = "document.getElementsByClassName('icon iconfont')[1].click();"
     browser.execute_script(js)
     sleep(5)

     #window handles
     handles=browser.window_handles
     print(handles)
     if len(handles)==2:
         browser.switch_to_window(handles[-1])
     else:
         print('Error!')
     
        

     #click Quality center
     sleep(5)
     ele_4=browser.find_element_by_id('p_menu_50')
     ele_4.click()
     sleep(2)

     #click the order 
     ele_5=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/ul/li[1]/a')
     ele_5.click()

def email_1(email_id,password_2,host_qq):
    '''imap server '''
    #create object
    imapobj=imaplib.IMAP4_SSL(host_qq,993)

    #login
    imapobj.login(email_id,password_2)

    #the file named 'INBOX'
    imapobj.select('INBOX')
    #print(INBOX)

    #the list have space
    typ,data=imapobj.search(None,'ALL')
    # print(typ,data)

    #the new list without space
    newlist=data[0].split()
    print(len(newlist))

    #the new email is the last of list
    first_email=newlist[len(newlist)-1]
    print(first_email)

    #use fetch hunction to get email
    typ,datas=imapobj.fetch(first_email,'(RFC822)')

    #jie xi youjian
    message=email.message_from_string(datas[0][1].decode('UTF-8'))
    # with open('email.txt','w') as fo:
    #     fo.write(datas[0][1].decode('gbk'))
    
    #get the title of email
    sub=message.get('subject')
    subdecode=email.header.decode_header(sub)[0][0]
    print(subdecode)

    #the part of email 
    for file_part in message.walk():
        if not file_part.is_multipart():            
            youjian=file_part.get_payload(decode='True').decode('UTF-8')
            #print(youjian)
            
    
    # with open('email.txt','w') as fobj:
    #     fobj.write(youjian)
    #     fobj.close()

    # with open('email.txt','r') as fo:
    #     a=fo.read()
    #     fo.close()
    
    #this is chinese '：'
    yanzhengRegex=re.compile(r'\：\d\d\d\d')
    mo1=yanzhengRegex.findall(youjian)
    if mo1:
        wenben=mo1[0]
        shuziRegex=re.compile(r'\d\d\d\d')
        mo2=shuziRegex.findall(wenben)
        if len(mo2)==1:
            yanzhengma=mo2[0]
            #print(yanzhengma)
            return yanzhengma
        else:
            print('can not find the code of email!')        
    else:
        print('error!')
try:
    wenjian='psd.json'
    with open(wenjian,'r') as obj:
        list_userset=json.load(obj)
except FileNotFoundError:
    print('missing profile!')
else:
    email_id,password_2,host_qq,url,username,password=list_userset
    start_2(url,username,password)
    # print('press ESC to close')
    # keyboard.wait('ESC')
    # sys.exit()
    sleep(43200)
