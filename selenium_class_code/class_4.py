# #一个web自动化的实例
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

# def set(url):
#     driver=webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     driver.get(url)
#     sleep(10)


# set('http://baidu.com')

import re

with open('email.txt','r') as f_o:
    a=f_o.read()

print(a)

aaaregex=re.compile(r'\：\d\d\d\d')
mo1=aaaregex.findall(a)
if mo1:
    print(mo1)