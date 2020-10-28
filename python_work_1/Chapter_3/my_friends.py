#coding=utf-8
my_friends=["wangli","zhangfei","guanyu","liubei"]
message_1=my_friends[0].title()+" "+"likes to drink beer"+"."
message_2=my_friends[1].upper()+" "+"is my brother"+"!"
print(message_1)
print(message_2)
my_friends[0]="zhaogou"#修改列表对应的元素，0为索引
print(my_friends)
#在列表末尾添加元素
my_friends.append("wanglaoji")#append()为添加列表元素到末尾，append（添加结尾）
print(my_friends)
#建立列表的另一种方式，首先建立一个空列表，再添加元素
my_friends=[]
my_friends.append("001")
my_friends.append("002")
my_friends.append("003")
print(my_friends)
#在列表的任何位置添加元素，insert（），需要索引和元素值
my_friends=["zhangjike","wanglaoji","xuezhiqian"]
#my_friends.insert(0,"dazhangwei")#在索引0处添加大张伟
#my_friends.insert(1,"zhouheiya")#在索引1处添加周黑鸭
my_friends.insert(-1,"hanbaobao")#在索引-1（最后一个元素）处添加hanbaobao，右移一个位置
print(my_friends)
#在列表中删除元素方法1，用del语句
my_friends=["1","2","3","4"]
print(my_friends)
del my_friends[0]#删除第一个元素1
print(my_friends)
#在列表中删除元素方法2，用pop（）方法，将删除（列表末尾）的值储存在popped_friends中，虽然在列表friends中被删除，依然可以使用它的值
friends=["zhang3","li4","wang5"]
print(friends)
popped_friends=friends.pop()
print(friends)#打印出删除（列表末尾）后的值
print(popped_friends)#打印出，被删除的值（仍然可以使用）
#使用pop（）也可以删除任意位置的值，只需要加索引
friends=["zhang3","li4","wang5","zhao8"]
message_5=friends.pop(0)#删除friends列表中的第一个元素值并储存，仍然可以使用
print(friends)#打印出删除后的列表值
print(message_5.title())#访问被删除的元素值并打印出来,大写首字母

#根据元素值删除元素，前面都是利用索引删除元素，使用remove（）方法
#例子1
#motorcycles=["honda","yamaha","suzuki","ducati"]
#print(motorcycles)
#motorcycles.remove("honda")
#print(motorcycles)

#例子2
friend=["zhangxiaoyin","wangli","lujiahui","lixing","guanjunkai"]
print(friend)
friend.remove("zhangxiaoyin")#根据元素值xhangxiaoyin删除zhangxiaoyin
print(friend)








