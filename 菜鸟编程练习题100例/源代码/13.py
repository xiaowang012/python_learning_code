for number in range(100,1000):
    number=str(number)
    a=number[0]
    b=number[1]
    c=number[2]
    a=int(a)
    b=int(b)
    c=int(c)
    if a**3+b**3+c**3==100*a+10*b+1*c:
        print('水仙花三位数为:'+number)

