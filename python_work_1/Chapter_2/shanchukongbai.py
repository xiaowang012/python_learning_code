#coding=utf-8
#删除字符串前后的空白
#message=“ zhang ”，前后均有一个空白
#删除末尾，message.rstrip（）
#删除开头，message.lstrip（）
#删除两端空白，message.strip()
#例子
message=" zhang "
print(message)
message=message.lstrip()#删除后需要存回变量message
print(message)
