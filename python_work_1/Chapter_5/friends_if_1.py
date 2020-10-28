#if语句


friends=['zhang3','li4','wang5','zhao6']
for friends_1 in friends:#循环，将friends列表的值赋值给临时变量friends_1
    if friends_1=='wang5':#如果临时变量的值是wang5，则输出为全部大写
        print(friends_1.upper())
    else:
        print(friends_1.title())#否则大写首字母输出



#两个等于号==为判断变量与特定值是否相等
a=1
if a==1:
    print("T")#如果a等于1，则输出T，否则输出F
else:
    print("F")

#对比时会区分大小写
a='A123'
if a=='a123':
    print('T')
else:
    print('F')

if a.lower()=='a123':#转化为小写后再比对
    print('T')
else:
    print('F')

#使用!=比对两个值是否不相等,不相等则输出T，否则输出F
a='1'
if a!='2':
    print('T')
else:
    print('F')

#比较数字 
age=22
if age<23:
    print("wo 21 sui")#可以使用< > <= >=
else:
    print("wo da yu deng yu 23 sui")


#检查多个条件，用and语句（需要同时满足两个条件才输出TRUE，否则输出F）
a=1
b=2
if a==1 and b==2:
    print("T")
else:
    print("F")

if a<=1 and b<=2:
    print("t")
else:
    print("F")

#使用or语句检测两个条件，至少有一个满足输出为T，一个条件都不满足，输出F
a=2
b=3
if a==2 or b==5:#至少有一个满足，所以输出T
    print("T")
else:
    print("F")
    
#判断特定值是否在列表中，使用in
a=['1','2','3','4']
if '1' in a:
    print("元素1在列表中")
else:
    print('元素1不在列表中')

#检查特定值是否不包含在列表中，使用 not in，如果不包含特定元素，则输出为TRUE，如果包含特定元素，则输出F
user=['wangli','zhang3','zhao4']
if 'xuezhiqian' not in user:
    print('TURE,xuezhiqian 不在列表中') 
else:
    print('F,xuezhiqian在列表中')

#布尔表达式，它的结果要么为True，要么为False


#if语句，if-else语句，if-elif-else结构
#重点举例if-elif-else
age=11#会依次测试每一个条件，有一个条件符合就会跳过下一个条件
if age <18:
    print("你还没有18岁不能谈恋爱！")
elif age <22:
    print("你还没有22岁，还没到法定结婚年龄")
else:
    print("你打年龄太老了，找不到对象了！")

#使用多个elif代码块，阶梯水电费，并不要求if-elif-else结构中一定要有else，也可以使用多个elif
water=20
if water <5:
    print("你用的水小于5吨，要出10元钱")
elif water <15:
    print("你用的水小于15吨，要出20元钱")
elif water <30:
    print("你用的水小于30吨，要出100块钱")
else:
    print("你他娘的用的水超过了30吨，收你一万块钱")

#Test 1
#外星人颜色
alien_color="green"

if alien_color =="yellow":
    print("你获得5分")
else:
    print("你获得了10分")


#if-elif-else
alien_color="red"
if alien_color=="green":
    print("获得5分")
elif alien_color=="yellow":
    print("你获得10分")
elif alien_color=="red":
    print("你获得15分")
#age,不同年龄段的人
age=22
if age<2:
    print("你不足两岁，还是个孩子")
elif age>=2 and age<4:
    print("你还在学走路")
elif age>=4 and age<13:
    print("你是个儿童")
elif age>=13 and age<20:
    print("你是个青少年")
elif age>=20 and age<65:
    print("你是个成年人")
else:
    print("你是个老年人。")


#水果是否在列表中
fruits=["apple","chengzi","xiangjiao"]
if "apple" in fruits:
    print('苹果在列表中')
else:
    print("苹果不在列表中")

#判断是否为空列表,if后面加列表名，至少有一个元素时为true，没有元素时返回false
a=["1","2","3"]
if a:
    for b in a:
        print(b)
else:
    print("列表是空的，无法开始循环")


#使用多个列表
