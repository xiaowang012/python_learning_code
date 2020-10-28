#coding=utf-8
#使用sort（）方法将列表元素的顺序按字母排序（永久性排序）（a，b，c，d。。。）
cars=["baoma","aodi","jili","qirui"]
print(cars)#打印出还未排序的列表
cars.sort()#将列表元素按字母顺序排列
print(cars)#打印出排序好的列表，元素的顺序已经发生改变
#可以将元素按照字母顺序排列的方式反过来排序，只需要在sort（）方法中增加参数reverse=True
#比如sort（reverse=True）
cars.sort(reverse=True)#按照字母排序的相反顺序排序（永久性排序）
print(cars)#并打印出来


#使用sorted（）对列表进行临时性排序
friend=["wangli","zhangxiaoyin","guanjunkai","lujiahui"]
print(friend)#原始列表
print(sorted(friend))#临时性按照字母顺序排列的列表
print(friend)#不改变原来列表中元素的顺序
print(sorted(friend,reverse=True))#按照字母排序的反方向排序（临时性），传递参数reverse=True实现


#倒着打印列表，使用reverse（）可以将列表元素倒着打印出来，注意：这种不是按照字母顺序的反方向排列，只是反转列表的元素的顺序。
#如果需要恢复到原来的顺序，再使用一次reverse（）即可。
shuzi=["001","002","003","004"]
print(shuzi)
shuzi.reverse()#将列表元素倒过来打印
print(shuzi)
shuzi.reverse()#恢复原状
print(shuzi)

#确定列表的长度，使用len（）可以获取列表的长度，列表有几个元素，长度为几
friend=["a","b","c","d","e"]
#len(friend)#此句为获取friend列表的长度，因为有5个元素，所以长度为5，由于要打印出来，所以此句放在print（）中
print(len(friend))
