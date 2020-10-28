#用户输入（input）和while循环
#示例I1
#message=input("请输入您的姓名：")
#print("你好，"+" "+message+"!")
#如果字符串太长可以使用运算符+=创建多行的字符串
#name=input(message)
#print("\n你是最漂亮的！"+name+" "+"!")

#使用input（）函数时，python将用户的输入默认解读为字符串的形式
#age=input("请输入您的年龄！")
#print(age)
#if age>=10:
 #   print("true")

#由于input（）默认是字符串，字符串和数值无法进行比较
#这里要用到int（）他可以将数字字符串转换为数值

##age=int(age)#将字符串转换为数值
#if age>=22:
  #  print("你的年龄超过22岁了，你可以去工作了")
#else:
  #  print("你的年龄小于22岁，还可以在家里玩耍！")

#示例，加减乘除的简单计算器
a=input("请输入第一个数值:")
a=int(a)
b=input('请输入第二个数值：')
b=int(b)
c=input("加法：1；减法：2；乘法：3；除法：4，请选择对应的方式：")
result_1=a+b
result_4=a/b
result_3=a*b
result_2=a-b
c=int(c)
if c==1:
    print("相加的结果为："+" "+str(result_1))
elif c==2:
    print("相减的结果为："+" "+str(result_2))
elif c==3:
    print("相乘的结果为："+" "+str(result_3))
elif c==4:
    print("除以的结果为："+" "+str(result_4))
else:
    print("我他娘的只会加减乘除！！！")  


#print("相加的结果为："+str(result))#相加的结果为数值型，需要使用str（）转化成字符串

#求模运算符%（他将两个数相处并返回余数）
#如果余数为0，则可以被整除，利用这个我们可以判断奇数偶数
a_1=input("请输入一个数值，我判断出是奇数还是偶数：")
a_1=int(a_1)
if a_1%2==0:
    print("这个数是偶数哦。")
else:
    print("这个数是奇数哦。")

# while循环
age=1#age设置为1
while age <= 22:#只要age不大于22，就一直循环
    print("年龄为："+" "+str(age))
    age=age+1#也可以简写为下一行的代码，age每次加1
    #age+=1

#可以选择何时退出
#a="\n请输入数值:"
#message=""
#while message!= "2":
  #  message=input(a)
   # print(message)
#这个程序当你按输入2的时候停止循环，如果不等于2，则会将用户输入的值打印出来，不停止。

#使用标志进行循环的控制()
#a="\n请输入："#这一段循环的条件仅判断active的是否为true，为true继续循环，为false则退出循环。

#active=True
#while active:
 #   message_1=input(a)
  #  if message_1=="1":
  #      active=False
  #  else:
  #      print(message_1)
#使用break退出循环
#break为流程控制语句
#message="\n请输入字符开始循环或输入2退出"
#while True:#while true将不断的循环直到break退出
#    a=input(message)
 #   if a=="a":
 #    break
 #   else:
  #      print(a)

#在循环中使用continue，这个用来返回到循环开头重新循环
a=1
while a<=20:
    a+=1#a=a+1的简写
    if a%2==0:
        continue
    print("奇数为："+""+str(a))

#避免无限循环,任何循环都必须有停止运行的条件
#无限循环示例
#x=1
#while x<=5:
 #   print(x)

#test 1，输入x退出
#message="\n请输入你想要的蘸料："
#a=True
#while a:
 #   b=input(message)
  #  if b=="x":
  #     a=False
  #  else:
   #     print("我们将会在面中添加"+" "+b)

#test 2
#message="\n请输入年龄，我会告诉你电影票的价格："
#a=True
#while a:
 #   b=input(message)
  #  b=int(b)
  #  if b<3:
  #      print("你还不满3岁，可以免费观看。")
  #  elif b>=3 and b<=12:
  #      print("你的年龄在3到12岁之间，需要支付10美元！")
  #  elif b>12:
   #     print("你的年龄大于12岁，需要支付15美元！")
    




#使用while循环处理列表和字典
#在列表之间移动元素
#首先创建一个列表a_1[1,2,3],再创建一个空列表a_2,将a_1的元素移动到a_2
a_1=["wangli","zhang3","li4"]
a_2=[]
while a_1:
    b=a_1.pop()
    print("已验证的用户："+b.title())
    a_2.append(b)
print(a_2)
a_2.reverse()
print(a_2)

#删除包含特定值的所有列表元素
#使用remove()删除包含特定值的所有元素
a=['apple',"2","apple",'aaaa','bbbb']
print(a)
while "apple" in a:#建立这个循环。只要列表中有“apple”元素，就一直循环删除它，直到他消失为止
    a.remove("apple")
print(a)


#使用用户的输入来填充字典
#调查问卷
a={}
biaozhi=True
while biaozhi:
    name=input("请告诉我你的名字：")
    wenti=input("你喜欢的女生的名字叫什么？：")
    a[name]=wenti
    c=input("可以告诉我你为什么喜欢她妈？(yes/no)：")
    if c=='yes':
        print("good, And have a son soon!")
        print(a)
        for n,q in a.items():
            print(n+"喜欢的人是"+q)


        biaozhi=False
    if c=="no":
        biaozhi=False
    
    
