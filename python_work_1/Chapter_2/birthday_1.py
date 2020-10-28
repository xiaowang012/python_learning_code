#coding=utf-8
#使用str（）将非字符串的值表示为字符串

age=22
message="happy"+age+"birthday!"
print(message)
#按上述这种，python会报错，因为它不确定age的类型
#使用str（）
age=22
message=“happy”+str(age)+"birthday!"#这样就明确了age的类型，以字符串输出
print(message)
