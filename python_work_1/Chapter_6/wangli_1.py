#设计一个字典，它包含了wangli的姓，名，年龄，性别，所在的城市
wangli_1={}
wangli_1["first_name"]="wang"
wangli_1["last_name"]="li"
wangli_1["age"]="22"
wangli_1["sex"]="male"
wangli_1["city"]="WuHan"
print(wangli_1)
print("I am"+" "+wangli_1["first_name"].title()+wangli_1["last_name"].title())
print("My age is"+" "+wangli_1["age"]+".")
print("I am "+wangli_1["sex"]+".")
print("My favourite city is"+" "+wangli_1["city"]+".")

#遍历字典中的所有键-值对
#使用wangli_1.items():可以返回键和值的对应列表，然后声明两个变量来储存
for a,b in wangli_1.items():
    print("\na:"+a)
    print("b:"+b)

#使用.keys（）可以遍历字典中的所有键
for a_1 in wangli_1.keys():
    print("字典中的所有键为："+a_1)

#第二种方法是，在只声明一个变量的情况下，python会默认遍历所有的键，若果有两个变量，则遍历键——值对
for a_2 in wangli_1:
    print("所有的键为："+a_2)

#方法1和方法2的输出时一致的
#用if xxx in xxx字典可以判断是否在字典中。 

#按照字母的顺序对字典的所有键进行排序，可以使用sorted（）进行排序
#在正常排序的时候调用sorted（）函数
for a_2 in sorted(wangli_1.keys()):
    print(a_2.title())

#遍历字典中的所有的值
#使用.values（）可以遍历字典中的所有值
for a_11 in wangli_1.values():
    print("字典中的所有的值为："+" "+a_11)

#剔除重复的值，使用set()函数可以实现
ab_1={"wang":"1","zhang":"1","li":"2","zhao":"3"}
print(ab_1)
for ab_2 in set(ab_1.values()):
    print("剔除字典中的重复值之后的值的集合为："+ab_2)#输出这个不重复的列表

#test 1
#创建一个字典，其中包含了长江黄河黄浦江以及他们流经的省份作为值储存在字典中
#rivers={"changjiang":"hubei","huanghe":"henan","huangpujiang":"shanghai"}
rivers={}
rivers["changjiang"]="hubei"
rivers["huanghe"]="henan"
rivers["huangpujiang"]="shanghai"
print(rivers)
for a in rivers.keys():
    print("l love "+a.title())
for b in rivers.keys():
    print("河流的名称为（键）："+b.title())
for c in rivers.values():
    print("河流流经的省份为（值）："+c.title())


#嵌套，将字典储存在列表中或者将列表储存在字典中，或者将字典储存在字典中，称之为嵌套。是一款强大的功能。
#我们首先创建一个外星人列表，里面包含3个具体外星人的信息，将字典储存在列表中
alien_1={"color":"green","fractions":3}#注：fractions为分数，是外星人的参数之一
alien_2={"color":"yellow","fractions":5}
alien_3={"color":"red","fractions":7}
aliens=[alien_1,alien_2,alien_3]#注：将外星人具体参数的字典添加到列表中
for abc in aliens:
    #print("具体的外星人参数为："+str(abc))#如果此时需要添加前面的文本，那么需要用str定义类型（输出字符串），此时可能不是列表，如果需要
#输出为列表，可能需要不加文本直接为print（abc）
    print(abc)

#我们可以使用range（）创建多个外星人(外星人的参数相同)，首先定义一个外星人的空列表，
alien_new_1=[]
for alien_number in range(30):#range（）定义外星人的数量（循环几次）
    new_alien={"color":"green","points":5,"speed":"slow"}#设置外星人的属性并赋值给临时变量
    alien_new_1.append(new_alien)#将临时变量new_alien的外星人值添加到列表alien_new_1中
for a in alien_new_1[:3]:#遍历前3个外星人
    print(a)

#为了判断外星人数量是否生成了30个，可以使用len（）来获取列表的长度加以验证
print("外星人的数量为："+" "+str(len(alien_new_1)))

#修改独立的每一个外星人的属性，外星人aoteman
aoteman=[]
for aoteman_1 in range(0,30):
    aoteman_1={"color":"green","points":19,"speed":50}
    aoteman.append(aoteman_1)
print("aoteman的总数为："+str(len(aoteman)))#验证奥特曼的总数是否为30可以可以用len（）获取列表的长度
#接下来开始修改奥特曼的参数
for b in aoteman[0:4]:#前4个奥特曼(修改他的参数)
   if b["color"]=="green":
       b["color"]="red"
       b["points"]="20"
       b["speed"]="55"
for n in aoteman[0:8]:#显示前8个外星人以核对前面的4个奥特曼的属性发生改变了没有
    print(n)
print("#")
print("#")

#如果外星人中含有不同属性的，比如黄色的，绿色的，我们将黄色的改为蓝色；同时把绿色改为红色
#只需要使用if——elif代码块即可实现
#sunwukong_1={"color":"yellow","speed":"40","points":20}
#sunwukong_2={"color":"green","speed":"40","points":20}
#sunwukong=[sunwukong_1,sunwukong_2]
#for s in sunwukong:
  #  print(s)
#for m in sunwukong:
  #  if m["color"]=="yellow":
  #      m["color"]="blue"
  ###
#把列表储存在字典中
favourite_fruits={"apple":"apple_8","putao":["green putao","red putao"]}
print("我喜欢吃得苹果种类为："+favourite_fruits["apple"])
for favo_putao in favourite_fruits["putao"]:
    print("我最喜欢吃的葡萄是："+" "+favo_putao.title())#字典里的列表需要用个for循环访问，首字母大写

#定义一个字典，里面包含了不同的人（键），以及他们喜欢的明星（不止一个）
stars={
    "wangli":["xuezhiqian","zhangxueyou","chenli"],
    "hujiahuan":["chenli","jiaomaiqi"],
    "liaoduyin":["xiaozhan","wangyibo"],
    "liubei":["guanyunchang","zhangyide"]
}
for name,star_1 in stars.items():
    print("\n"+name.title()+"'s favourite star are:")
    for star_2 in star_1:
        print("\t"+star_2.title())

#在字典中储存字典
#定义一个用户(users)的字典，里面包含两个用户名（键）admin，和wangli，这两个用户名也是两个字典
#小字典里面的两个键为全称和简称，全称为adminstrator，wangli's admin，简称为adm，wang's
users={
    "admin":{"full_name":"adminstrator",
    "easy_name":"adm",
    },
    "wangli":{"full_name":"wangli's admin",
    "easy_name":"wang's"
    #大字典users，小字典为admin和wangli

    }

    }
    #定义两个变量访问大字典
    
    
for a,b in users.items():
     print("大字典的键为："+a)
     full_name_1=b["full_name"]
     easy_name_1=b["easy_name"]
     print("全名为："+" "+full_name_1)
     print("简称为："+" "+easy_name_1)#第一次循环针对小字典里面的第一个值，可以适当理解一下，第二次循环提取字典的第二个元素

#test 1
#创建一个城市的字典（city），键为wuhan，shenzhen，yichang，并分别以此创建这几个城市的人口（people），房价
#（house_price）,和大学数量（number）
city={"wuhan":{"people":"10 million",
              "house_price":"30000",
              "number":"90"},
     "shenzhen":{"people":"20 million",
              "house_price":"60000",
              "number":"50"},
     "yichang":{"people":"4 million",
              "house_price":"9000",
              "number":"3"},

}
for b_1,c_1 in city.items():
    print("\n各个城市为："+b_1.title())
    p=c_1["people"]
    h=c_1["house_price"]
    n=c_1["number"]
    print("这个城市的人口数为："+" "+p)
    print("这个城市房价为："+" "+h)
    print("这个城市的大学数量为："+" "+n)

    










    

