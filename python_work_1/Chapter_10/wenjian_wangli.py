#从文件中读取数据
#可以读取一个文本文件的内容，重新设置数据格式，然后写入文件，使之可以在浏览器中显示

#读取整个文件，和当前程序在同一个目录的文件
with open("wenjian.txt") as file_object:
    a=file_object.read()
    print(a)
#方法read（）将读取这个文件的全部内容并将其作为一个长字符串储存在变量a中

#打开指定文件路径的文件
lujing='D:\python123\ma123.txt'#这里是绝对路径
with open(lujing) as file_object:

    wen_1=file_object.read()
    print(wen_1)

#逐行读取文件,由于文件的每一行都有一个看不见的换行符，
#print语句也有换行符，所以会有很多空行，用rstrip语句删除空行
wenj="D:\python123\ma123.txt"
with open(wenj) as file_object:
    for hang_wenjian in file_object:
        print(hang_wenjian.rstrip())

#创建一个包含文件各行内容的列表
wenjian2="D:\python123\ma123.txt"
with open(wenjian2) as file_object:
    lines=file_object.readlines()#将读取的文件的每一行当成列表的元素，readlines（）
for lines_1 in lines:
    print(lines_1.rstrip())#

#使用文件的内容
#将文件读取到内存中后就可以随意使用了,把文件转化为列表后加个字符串“1”
wenjian3="D:\python123\we222.txt"
with open(wenjian3) as file_object:
    line3=file_object.readlines()
for line4 in line3:
    line4+="1"
    print(line4) 

#包含一百万位的大型文件


#写入文件
#调用open需要另一个实参，open(文件名，'w')表示写入模式
#open(文件名，'r')读取模式；'a'附加模式，‘r+’读取和写入模式，如果不提供这个实参，那么默认只读模式
wenjian5='xieru.txt'
with open(wenjian5,'w') as file_object:
    file_object.write("I love G"+"!")#使用write函数

#写入多行文件，write函数不会在末尾添加换行符\n，需要自己添加
wenjian6='xie.txt'
with open(wenjian6,'w') as file_object:
    file_object.write("我喜欢的人很可爱，\n")
    file_object.write("她的名字叫：？\n")


#附加到文件，不会覆盖原文件，添加的内容会在末尾，使用附加模式打开文件
with open(wenjian6,'a') as file_object:
    file_object.write("G!")




