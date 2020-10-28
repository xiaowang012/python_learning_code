#字典使用大括号{},
#外星人参数，颜色：color，green；点数：points，5分
alien_0={"color":'green',"points":5}
print(alien_0["color"])
print(alien_0["points"])
#添加键-值对
alien_0["wang"]=39#添加wang：39
alien_0["li"]=66#添加li：66
print(alien_0)

#可以创建一个空字典，然后在添加键-值对
age={}#添加一个不同人年龄的字典，包含名字和年龄
age["carlos.wang"]=22
age["john_1"]=16
age["galatea.liao"]=25
age["liuding"]=23
age["zhangxueyou"]=50
print(age)
print("She may be"+" "+str(age["galatea.liao"])+" "+"years old"+" "+",but she still doesn't have a boyfriend.")

#修改字典中的值
age_1={"galatea.liao_2019_age":24,"galatea_liao_2020":25}#一个字典:galatea在指定年份的年龄
print("galatea.liao was"+' '+str(age_1["galatea.liao_2019_age"])+" "+"in 2019.")
#现在需要改变galatea的年龄，改为20岁
age_1["galatea.liao_2019_age"]=20#将galatea的键值改为20
print("She is very girlish. Her mental age is only "+str(age_1["galatea.liao_2019_age"])+"!")
#删除键值对，用del语句
a_1={"wang":"1","li":"2"}
print(a_1)
del a_1["wang"]#删除wang以及对应的键值
print(a_1)

#由类似对象组成的字典，假设将不同的人喜欢的水果组成一个字典
favorite_fruit={}
favorite_fruit["willard.zeng"]="banana"
favorite_fruit["carry.zhang"]="apple"
favorite_fruit["sherry.liu"]="grapes"
favorite_fruit["galatea.liao"]="chervil"
favorite_fruit["00_ZHANG"]="durian and stinky tofu"
print(favorite_fruit)
print("My name is 00_zhang,"+"I like to eat "+str(favorite_fruit["00_ZHANG"]))

