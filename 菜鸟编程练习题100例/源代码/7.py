#将一个列表的数据复制到另一个列表中

liebiao1=['wangli','zhangfei','12345']
liebiao2=[1,2,3,45,5]

#将liebiao1的所有元素复制到liebiao2中，
#方法1
for x in liebiao1:
    liebiao2.append(x)

print(liebiao2)

#方法2
liebiao2+=liebiao1[:]
print(liebiao2)

#如果仅是将数据复制到空列表
a=[]
b=[3,4,5]

a=b[:]
print(a)