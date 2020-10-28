#! usr/bin/python
#coding=utf-8
#一种简单得错误，ZeroDivisionError
try:
     print(5/0)#这一句没问题则执行，有问题报异常ZeroDivisionError，告诉python遇到这种错误怎么处理，print('xxx')
except ZeroDivisionError:
    print('你不能除以0！！')

#在要求用户输入得过程中处理无效输入，
#只执行除法运算得简单计算器

print('输入两个数字，除法运算')
print('输入q结束')

while True:
    first_num=input('\n请输入第一个数:')
    if first_num=='q':
        break
    second_num=input('\n请输入第二个数:')
    if second_num=='q':
        break
    try:
         result=int(first_num)/int(second_num)
    except ZeroDivisionError:
        print('你不能输入0作为分母！')
    else:
        print(result)

#上述程序没有任何得处理错误得措施，当第二个数为0时，将引发ZeroDivisionError异常，崩溃
#添加try/except

#一种找不到文件得异常
#FileNotFoundError
file_name='wang.txt'
try:
    with open(file_name,'r',encoding='utf-8') as f_obj:#文本文档默认用gbk编码，指定编码方式为utf-8
        a=f_obj.read()
except FileNotFoundError:
    print('错误:找不到该文件！！')
else:
    print(a)

#也可以使用try/except pass 选择不报告错误信息，失败时一声不吭
try:
    print(5/0)#这一句出错时，pass(一声不吭)，不出错时，执行print(5),和print('第二条命令')
except ZeroDivisionError:
    pass
else:
    print('第二条命令')

#练习
#一个加法计算器，当用户输入得值不为数字时，用int(x)将引发typeError错误，捕获这种错误，并友好提示
print('这是加法计算器')
while True:
    first_number=input('\n请输入第一个数字。按q退出:')
    if first_number=='q':
        break
    second_number=input('\n请输入第二个数字，按q退出:')
    if second_number=='q':
        break
    try:
        result_1=int(first_number)+int(second_number)
    except ValueError:
        print('错误:无效输入！')
    else:

        print(result_1)