#coding=utf-8
#正则表达式，查找文本是否符合匹配模式
#需要用re模块,它包含了所有的正则表达式
import re

#正则表达式的表示，re.compile()的参数为字符串，这样就表示一个正则表达式
#\d表示一个数字字符
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#创建正则表达式对象，模式
mo=phoneNumRegex.search('my phone number is 415-555-2421.')#如果设置好的模式在字符串中被找到，则返回一个match对象，他有一个group方法
print('寻找到字符串中的电话号码是：'+mo.group())#没找到则返回none，第三步可以直接在mo变量()调用group()方法

#实例，我们在在一堆字符串中找出qq号码，

qq_number=re.compile(r'\d\d\d.\d\d\d.\d.\d')
mo=qq_number.search("this computer's ip address is 192.168.1.1")
print("ip地址为："+mo.group())

#用括号分组，比如说加区号的电话号码(0717)15623874066想把他们分开
phone_number=re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d\d\d\d\d\d)')
mo=phone_number.search("我的电话号码是0717-15623874066！！！！！")
print(mo.group())
print(mo.group(1))#
print(mo.group(2))

#如果需要匹配括号，则在需要加 \(xxxx\)前面是撇加前括号，后面是撇加后括号
phone_number_1=re.compile(r'(\(\d\d\d\d\))(\d\d\d\d\d\d\d\d\d\d\d)')
mo=phone_number_1.search("我的电话号码是a(0717)15623874066")
print("利用括号分组后的第一组："+mo.group(1))
print("利用括号分组后的第二组："+mo.group(2))
print("整个组的数据(所有数据)："+mo.group())


#正则表达式_用管道匹配多个分组
#字符 | 称为管道，在希望匹配多个正则表达式中的一个时可以使用(它会默认查找第一个出现的字符串作为Match对象返回，即查找第一个)
colorRegex=re.compile(r"red|blue")
mo=colorRegex.search("我喜欢的颜色时red和blue。。。")
print("查找到的颜色为："+mo.group())

mo2=colorRegex.search("我喜欢的颜色是blue和red")
print("第二次查找到的颜色是："+mo2.group())

#也可以使用管道|来匹配多个模式中的一个，作为正则表达式的一部分，例如
#希望匹配adminuser，adminwang，adminzhang，adminli中的任意一个，这些都以admin开头，可以通过括号实现
adminRegex=re.compile(r'admin(user|wang|zhang|li)')
mo=adminRegex.search("我的用户名是adminwang，adminzhang")
print("查找到的用户名ID为："+mo.group())#也是查找第一个匹配的字符

mo2=adminRegex.search("我的用户名是adminzhang，adminwang，adminli")
print("查找到的用户名是："+mo2.group())

#用?实现可选的匹配
#问号之前括号里的字符，不论它存不存在，正则表达式都认为是匹配的
sexRegex=re.compile(r"(wo)?man")
mo1=sexRegex.search('sex is woman')
print("查找的性别为："+mo1.group())

mo2=sexRegex.search("sex is man")
print("查找到的性别为："+mo2.group())#(wo)?表示可选（可有可无），既可以匹配woman又可以匹配man

#正则表达式
#用星号*匹配0次或者多次
#也就是说*前面的分组(需要用括号括起来)可以出现任意次数
peopleRegex=re.compile(r"woaini(xxx)*doyouknow")
mo1=peopleRegex.search("woainidoyouknow，你好")
print("星号前面的分组出现0次的匹配为："+mo1.group())

mo2=peopleRegex.search("woainixxxdoyouknow,nihao")
print("星号前面的分组出现1次的匹配为："+mo2.group())

mo3=peopleRegex.search("woainixxxxxxxxxxxxxxxdoyouknow,你的名字叫啥？")
print("星号前面的分组出现任意次数时的匹配为："+mo3.group())

#用加号匹配一次或者多次(任意次)与上面不同的是，匹配的字符中必须有一次符合>=1,不然就会匹配失败
peopleRegex=re.compile(r"woaini(xxx)+doyouknow")
#mo1=peopleRegex.search("woainidoyouknow，你好")
#print("星号前面的分组出现0次的匹配为："+mo1.group())#这一段代码是匹配不了的。因为匹配的字符里面没有xxx

mo2=peopleRegex.search("woainixxxdoyouknow,nihao")
print("星号前面的分组出现1次的匹配为："+mo2.group())#用加号表示至少有一次符合

mo3=peopleRegex.search("woainixxxxxxxxxxxxxxxdoyouknow,你的名字叫啥？")
print("星号前面的分组出现任意次数时的匹配为："+mo3.group())#任意次


#用花括号匹配特定次数，在正则表达式后面加上{次数}，或者定义起点和终点{1，5}，只定义起点加逗号{3，}表示匹配3次及以上
#只定义终点{，5}前面加逗号表示匹配0到5次。
hhhhRegex=re.compile(r"hhhh{1}")#
mo1=hhhhRegex.search("fffffffhhhhwasasdas")
print("仅仅匹配一次hhhh的结果为："+mo1.group())

#hhhhRegex=re.compile(r"hhhh{0,5}")#匹配0到5次hhhh，
#hhhhRegex=re.compile(r"hhhh{1,}")#一次及以上任意次
#hhhhRegex=re.compile(r"hhhh{,7}")#0到7次


#贪心匹配和非贪心匹配
#首先在正则表达式xxx{3,5}中，由于默认是贪心匹配模式，在存在二义的情况下，匹配最长的字符串，
xRegex=re.compile(r'x{3,5}')
mo1=xRegex.search("xxxxx")#这里会默认匹配5个x而不是3个x
print("默认为贪心模式下的匹配5个x的结果是："+mo1.group())

#非贪心模式只需要在花括号后面加一个问号？就会匹配最少的字符串，3个x
xRegex=re.compile(r'x{3,5}?')
mo2=xRegex.search("xxxxx")
print("非贪心模式下匹配最短的字符串（3个x）的结果为："+mo2.group())

#注意在正则表达式中，问号？表示两种含义，一种是申明非贪心模式，一种是表示可选的分组：两种含义完全无关。

#正则表达式findall方法，除了search方法以外还有这个方法
#search()返回的是一个match对象，包含被查找的第一次匹配的文本，
#而findall()是包含所有符合的匹配
#注意：如果正则表达式是没有分组的情况下，将返回一个符合的所有匹配的列表
#如果正则表达式是有分组的情况下，将返回一个符合的字符串元组的列表
numberRegex=re.compile(r"\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d")
mo1=numberRegex.findall("我的电话号码是071015623874066，和071713977667777")
print(mo1)#正则表达式中为分组，将返回一个列表

numberRegex=re.compile(r"(\d\d\d\d)(\d\d\d\d\d\d\d\d\d\d\d)")
mo2=numberRegex.findall("我的电话是071715623874066，和071713977778888")
print(mo2)#由于是有分组的，将返回一个字符串的元组的列表


#正则表达式中的字符分类
# \d表示0到9的任何数字
# \D除0-9之外的任何字符
# \w 任何字母，数字和下划线字符（可以认为是匹配单词字符）
# \W 除字母，下划线，数字以外的任何字符
# \s 空格，制表符，换行符（可以认为是空白字符）
# \S 除了空格，制表符，换行符以外的任何字符

#插入字符^和美元字符$
# ^表示匹配必须发生在被查找的文本开始处，$美元字符表示该字符串必须以这个正则表达式的模式结束
aRegex=re.compile(r"^hello")
mo1=aRegex.search("hello world")
print("以hello开始，可以匹配匹配出来:"+" "+mo1.group())

#尝试不以hello开头的字符串查找
#mo2=aRegex.search("你好hello world")#匹配不出来
#print("这一句匹配不出来，因为"+mo2.group())

# $美元字符表明结束必须以正则表达式的模式结束
aRegex=re.compile(r"hello$")
mo3=aRegex.search("nihaohello")#如果结尾不是hello模式，就匹配失败，返回none
print(mo3.group())

#二者可以一起用
aRegex=re.compile(r"^\d\d\d$")#必须以数字开头且结尾必须为3个数字的模式
mo4=aRegex.search("456")#仅匹配3个数字连续的
print(mo4.group())


#通配字符句点.   没看懂
#它可以匹配除了换行符以外的所有字符
#通配符之后跟着的字符，仅匹配一个（这个）字符
atRegex=re.compile(r".at")#匹配了c,h,s,l,m
mo6=atRegex.findall("The cat in the hat sat on  the flat mat.")
print(mo6)

#用点-星号匹配所有字符
aRegex=re.compile(r"username:(.*)admin:(.*)")#.*表示任意内容（除去换行符）
mo7=aRegex.search("username:aaa admin:gdw7tdw7qtqt78wq7wq")
print(mo7.group())

#用句点字符匹配换行符
#点-星号是匹配除了换行符以外的所有字符
#通过传入re.DOTALL作为re.compile()的第二个参数，可以让句点.匹配所有字符包括换行符
newRegex=re.compile(".*",re.DOTALL)
mo8=newRegex.search("my name is wang\nli")#print函数显示了换行符，说明用句点成功的匹配了换行符
print(mo8.group())

#正则表达式复习

#不区分大小写的匹配，默认的正则表达式是区分大小写的，
#如果不需要区分大小写，只需要给re.compile()传入第二个参数为re.IGNORECASE或者re.I
aBcRegex=re.compile(r"abc",re.IGNORECASE)
mo1=aBcRegex.search("ABC是三个简单的字母")
print("不区分大小写匹配到的字母的结果是："+mo1.group())
mo2=aBcRegex.search("abCshijiandan1de1zimu")
print("不区分大小写的匹配字母为："+mo2.group())


#用sub()方法替换字符串
nameRegex=re.compile(r"wang")#匹配wang加一个单词至少一次
mo11=nameRegex.sub('zhang','wang li is my teacher，wang zi is good')
print('用zhang替换wang之后的结果为：'+mo11)


# 管理复杂的正则表达式，
# 不必使用复杂的正则表达式，可以在re.compile()的第二个参数传入re.VERBOSE,将正则表达式放在多行中，并加上注释
# phoneRegex=re.compile(r'''(\d{3}|\(\d{3}\))?#注释
# xxxx#注释
# xxxxx#注释
# )''',re.VERBOSE)


# 组合使用re.IGNORECASE,re.DOTALL,re.VERBOSE
# 可以用|组合在一起
# re.compile("regex_xxx",re.IGNORECASE|re.DOTALL|re.VERBOSE)#组合使用


