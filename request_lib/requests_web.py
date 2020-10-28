#coding=UTF-8
import requests
import json


# requests库是个简单易用的http库

#最基本的get请求
url='http://httpbin.org/get'
response=requests.get(url)
#print(response.text)

#带参数的get方法,将name和age参数传递进去，并用&符号隔开
url='http://httpbin.org/get?name=germey&age=22'
response=requests.get(url)
#print(response.text)

#或者使用params方法以达到同样的效果
data={'name':'wangli','age':28}
response=requests.get('http://httpbin.org/get',params=data)
#print(response.text)

#解析json
#将返回值以json的形式返回
url='http://httpbin.org/get'
response=requests.get(url)
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

#获取二进制数据,加.content
url='https://github.com/favicon.ico'
response=requests.get(url)
print(type(response.text))
print(type(response.content))
print(response.text)
print(response.content)
print('##########################################')

#添加headers,有的网站访问必须带有浏览器信息，不传入headers会报错,
#explore为浏览器信息
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url='https://www.zhihu.com/explore'
response=requests.get(url,headers=headers)
print(response.text)

#基本的post请求（带参数）
data={'name':'wangli','age':'28'}
url='http://httpbin.org/post'
response=requests.post(url,data=data)
print(response.text)

#响应
#response的属性
# response=requests.get('http://baidu.com')
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history)


#高级操作
#1.文件的上传
files={'file':open('cookie.txt','rb')}
response=requests.post('http://httpbin.org/post',files=files)
print(response.text)

#2.获取cookie
#直接调用response.cookie（response对象为请求之后的返回值）
response=requests.get('https://baidu.com')
print(response.cookies)

for key,value in response.cookies.items():
    print('键:'+key+' '+'值:'+value)

#3.会话维持，模拟登录，如果某个相应中包含一些cookies，可以快速访问它们
# r=requests.get('https://www.baidu.com/')
# print(r.cookies['NID'])
# print(tuple(r.cookies))

#发送cookies到服务器
url='http://httpbin.org/cookies'
cookies={'testCookies_1':'hello_py3','testCookies_2':'hello_requests'}

#在Cookie Version中，规定了空格，方括号，圆括号，等于号，逗号，双引号，斜杠，问号，@符号
#冒号，分号等特殊字符都不能作为cookie的内容
r=requests.get(url,cookies=cookies)
print(r.json())

#4.证书验证
#有的网站需要证书验证,直接访问会报错
response=requests.get('http://www.12306.cn')
print(response.status_code)

#消除警告信息(证书错误),将verify设置为false
from requests.packages import urllib3
#消除警告信息
urllib3.disable_warnings()
#访问
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

#5.代理设置,做爬虫时可以设置代理ip去访问
#代理ip的字典
# proxies={'http':'http://127.0.0.1:9743',
# 'https':'https://127.0.0.1:9743',
# }
# url='http://www.taobao.com'
# response=requests.get(url,proxies=proxies)
# print(response.status_code)

#如果代理需要设置账户名和密码,只需要将字典更改为如下：
# proxies = {
# "http":"http://user:password@127.0.0.1:9999"
# }
# #如果你的代理是通过sokces这种方式则需要pip install "requests[socks]"
# proxies= {
# "http":"socks5://127.0.0.1:9999",
# "https":"sockes5://127.0.0.1:8888"
# }

#6.超时设置
#设置一个超时的参数,.timeout,正常访问状态码返回200
# from requests.exceptions import ReadTimeout

# try:
#     response=requests.get('http://192.168.1.1/get',timeout=1)
# except TimeoutError:
#     print('Time out!')
# else:
#     print(response.status_code)

#7.认证设置
#如果碰到需要认证的网站可以通过requests.auth模块实现 
from requests.auth import HTTPBasicAuth
 
response = requests.get("http://192.168.1.1/",auth=HTTPBasicAuth("admin","admin"))
print('访问交换机web的状态码:'+str(response.status_code))
#当然这里还有一种方式
response = requests.get("http://192.168.1.1/",auth=("admin","123"))
print('第二种方式:'+str(response.status_code))





