#异常


#储存数据,json模块将数据结构存储在文件中
#使用json.dump()和json.load() 
#json.dump()需要两个实参，要储存的数据和用于储存数据的文件对象
#使用这个函数储存数字列表
import json
number_list='SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}\\0003'
wenjian='C:\\Users\\Administrator\\Desktop\\python_work_1\\center\\reg_wangli.json'
with open(wenjian,'w') as file_object:
    json.dump(number_list,file_object)
    #将列表存储在json文件中

#使用json.load读取json文件
#import json
#wenjian2='number.json'
#with open(wenjian2) as file_object:
 #   number_list=json.load(file_object)
#print(number_list)

#保存和读取用户生成的数据
#首先储存用户的名字
import json
username=input("请输入你的名字？")
wenjian3='username.json'
with open(wenjian3,'w') as file_object:
    json.dump(username,file_object)
    print("如果你再次回来，我会记住你的名字的"+username+"!")

#然后用json.load读取用户（事先储存）的名字
import json
wenjian4='username.json'
with open(wenjian4) as file_object:
    username=json.load(file_object)
    print("欢迎回来，我还记得你，你叫"+username+"!")


#将上述两个程序合成一个程序,先尝试获取文件中的用户名，如果有，就将用户名读取到内存中；如果没有，将会引发异常，然后执行expect代码块
import json

wenjian3='username.json'
try:
    with open(wenjian3) as file_object:
         username=json.load(file_object)
    
   
except FileNotFoundError:
    username=input("请输入你的名字？")
    with open(wenjian3,'w') as file_object:
        json.dump(username,file_object)
        print("如果你再次回来，我会记住你的名字的"+username+"!")
else:
    print("欢迎回来！"+username+'!')






#重构
#将代码分为一系列完成具体工作的函数，这个过程叫做重构，它可以使代码更清晰，更易于理解，更容易扩展
#可以将大部分逻辑放到一个或者几个函数中
#具体不演示
