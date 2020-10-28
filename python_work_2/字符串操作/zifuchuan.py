#coding=utf-8
#双引号字符串
a="bahbhasja"

#原始字符串
#在引号前面加个r，
print(r"aaaaaa")

#三引号的多行字符串
print('''我叫王力
今年22岁了
我的爱好是学习python！
''')

#多行注释

#字符串索引和切片表示
a="wangli"
print(len(a))
print(a[-1])
print(a[0])
print(a[:])
print(a[0:2])

#字符串的in not in 操作符
if 'w' in a:
    print("w在字符串'wangli'中")
else:
    print("w不在字符串'wangli'中")

#字符串方法
#upper()全部大写
#lower()全部小写
#title()首字母大写
#isupper()判断一个字符串中是否全部为i大写，大写则返回true，否则false
#islower()判断一个字符串中是否全部为小写，小写则返回true，否则false

a='TAKS'
print(a.isupper())
print(a.islower())

b="asdfss"
print(b.islower())
print(b.isupper())

#还有几个is xx的字符串方法
#isalpha()如果字符串只包含字母且非空
#isalnum（）如果字符串只包含字母和数字且非空
#isdecimal()只包含数字字符且非空
#isspace 如果字符只包含空格，制表符，换行符且非空
#istitle(),如果字符串仅包含以大写字母开头后面都是小写字母的单词，返回TRUE
#两个有用的字符串方法
#startswith('xx')判断字符串的开头是否为xx，如果是返回true
#endswith('xxx')判断字符串的结尾是否为xxx，如果是，返回true
a='wangli'
print(a.startswith("w"))#返回true
print(a.endswith("i"))

#join()将列表中的元素连接起来,将a字符串添加到列表的每个元素的中间
a='a'
lis_1=['1','2','3','4','5']
print(a.join(lis_1))#结果为：1a2a3a4a5

#split()的参数为一个字符串，用字符串调用，然后返回一个以参数分割的列表
#不带参数的情况下默认以各种空白字符分割（空格，制表符，换行符）
print("my name is wangli".split())#不添加参数的情况下
print('woaxiahuanadearenashiani'.split('a'))#加了参数a，以a分割字符串并生成一个列表

#左对齐，右对齐，居中
print('hello'.ljust(10,'#'))#第一个参数为将hello放入长度为10的字符串中,hello的长度为5，所以在后面填充'#'实现左对齐
print('hello'.rjust(10,'*'))#右对齐，同上
print('hello'.center(11,'$'))#居中，填充'$'

#strip()删除两边的空白，lstrip()删除左边的空白，rstrip()删除右边的空白
print('          wang             '.strip())
print('   wang'.lstrip())
print('wang                          '.rstrip())

#使用pyperclip模块拷贝粘贴字符
import pyperclip

pyperclip.copy("my name is wnagli")#复制
print(pyperclip.paste())#粘贴并打印出来
