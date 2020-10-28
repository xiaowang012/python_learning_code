#定义函数，函数即为执行具体任务的代码块
#可反复调用
#示例，def开头表明要定义函数
def greet_user(user_name):
    """打印出hello world"""#注释
    print("hello world"+" "+user_name.title())#代码

#运行这个函数只需要
greet_user("wangli")
#也可以向他传递参数
#实参，形参,其中实参为“wangli”，形参为name，实参为调用函数时传递给函数的信息；形参为函数完成工作时所需要的信息
def hello(name):
    print("hello"+name)

hello("wangli")

#传递实参
# 其中包含位置实参
#实参的顺序应该一一对应，叫作位置实参
def people(sex,name_1):
    print('ta的性别是：'+sex)
    print("它的性别是："+sex+" "+"他叫："+name_1.title())

people("男","wanglao5")

#位置实参的顺序非常重要，必须跟所用的形参一一对应

#关键字实参
def a(m,n):
    print("好好好"+m)
    print("heheihei"+m+n)

a(m="wangli",n="zhang3")
#上面演示了关键字实参，不用管顺序，只需在调用函数时把形参名和实参一一对应即可

#默认值，在调用函数时，如果没有给某个形参提供实参，那么将会是用默认值
def a(m,n="L"):
    print("hello"+m)
    print("nihao"+m+n)

a(m="W")#这里并未给n传递实参，由于n的默认值为“L”，所以python使用了默认值。
a(m="2",n="3")#由于这一行代码给n传递了实参，python将忽略默认值使用新的实参“3”

#可以混合使用位置实参，关键字实参和默认值
#避免实参错误，


#返回值，返回一个值或者一组值等
def name_2(first_name,last_name):
    full_name=first_name+last_name
    return full_name.upper()


wa=name_2(first_name="zhang",last_name="fei")
print(wa)


#可选实参，给其中一个实参（可选）设定默认值为空字符串a=“”
def a(first_name,last_name,a_name=""):
    if a_name:
        full_name=first_name+last_name+a_name
    else:
        full_name=first_name+last_name
    return full_name

k=a(first_name="wang",last_name="li",a_name="hong")
print(k)
k=a(first_name="wang",last_name="li")
print(k)
#上面的代码为可选实参，a_name,如果不给他传递参数，那么它会使用默认值“”空字符串

#返回字典，return可以返回任何类型的值，字典，列表，等
def liebiao_chuangjian(first_name,last_name):
    liebiao={'fir':first_name,"las":last_name}
    return liebiao

mmm=liebiao_chuangjian("wang222","li3333")
print(mmm)#返回值为字典

#向函数传递列表
def message(liebiao):
    for a in liebiao:
        wenhou="hello!"+""+a
        print(wenhou)

m=["wangli",'zhang3',"li4"]
message(m)#向函数传递一个列表m



#在函数中修改列表，将一个列表复制到另一个空列表中，并清空第一个列表
#禁止函数修改列表，可以用切片表示法（复制一个列表的副本进行处理）list_name[:]

#传递任意数量的实参
def city(*citys_name):#形参里面的*表示创建一个citys_name的空元组，并将收到的所有的值都封装到这个元组中
    print(citys_name)

city("wuhan")
city("wuhan","shenzhen","yichang","dangyang")
#输入一个或者几个实参均可

#可以结合位置实参和任意数量的实参
#
#使用任意数量的关键字实参



#将函数储存在模块中，有很多优点，
#导入整个模块
#模块是扩展名为.py的文件
#创建一个hello_wangli()的模块
def hello_wangli(name):
    print("hello,这是一个模块"+name)
#另一个文件调用hello_wangli这个模块
#import hello_wangli
#hello_wangli.hello_wangli("参数")这里是需要调用的模块文件的名字.函数名字+参数
#模块名.函数名（参数）

#导入特定的函数，
from 模块名 import 函数名#可以导入模块文件中特定的函数
#用逗号隔开，可以导入任意数量的函数，只需指出函数名
from 模块名 import 函数1，函数2，函数3

函数1（"参数"）即可执行

#在导入函数或模块时，它的名称可能与现有函数或模块冲突，可以指定别名
from 模块名 import 函数名 as 别名#给函数指定别名
别名（）

import 模块名 as 别名
#给模块指定别名。

#导入模块中的所有函数
#使用*号
from 模块名 import *
#星号会将模块中所有的函数复制过来，在遇到不是自己写的大型模块时，最好不要使用这种方法。
#可能名称会冲突从而覆盖原有的函数

#函数编写指南
#给形参指定默认值时等于号两边不要有空格
#关键字实参也适用
#代码行的长度最好不要超过79字符，大小适中
#如果程序或模块包含多个函数，可以使用两个空行隔开
#所有的import函数都应该放在文件开头，唯一例外的是，文件开头使用了注释描述整个程序。



