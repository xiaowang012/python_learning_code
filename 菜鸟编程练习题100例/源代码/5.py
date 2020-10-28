#输入三个整数,由小到大排序

a=input('请输入第一个数：')
b=input('请输入第二个数：')
c=input('请输入第三个数：')

while True:
    try:
        a=int(a)
        b=int(b)
        c=int(c)
    except ValueError:
        print('请输入正确的数字！')
        a=input('请输入第一个数：')
        b=input('请输入第二个数：')
        c=input('请输入第三个数：')
    else:
        break

if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<a<b:
    print(c,a,b)
elif c<b<a:
    print(c,b,a)