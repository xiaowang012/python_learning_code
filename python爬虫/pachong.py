
#coding=utf-8
import re
import urllib.request
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
 
 
def getlink(url):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url).read()
    file = file.decode('utf-8')
    pattern = '(https?://[^\s)";]+(\.(\w|/)*))'
    link = re.compile(pattern).findall(file)
    #去重
    #link = list(set(link))
    return link
 

wenjian='wenben.txt'
url = "http://iqianhai.sznews.com/"
liebiao_web=[]
linklist = getlink(url)
for link in linklist:
    liebiao_web.append(link[0])

print(liebiao_web)   
print('网址数量：'+str(len(linklist)))

for x in liebiao_web:
    try:
       response=requests.get(x)
    except:
        pass
    else:    
        try:
            a=response.text.encode('iso-8859-1').decode('utf-8')
        except:
            pass
        else:
            with open (wenjian,'a+',encoding='utf-8') as fobj:
                fobj.write(a)






    


