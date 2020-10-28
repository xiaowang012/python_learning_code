#求出s=a+aa+aaa+aaaa+...的值，
#其中a为数字，指定项数n，求Sn
    
a=input('please a:')
n=input('please n:')
while True:
    try:
        a=int(a)
        n=int(n)
    except ValueError:
        print('error! a,n! ')
        a=input('please a')
        n=input('please n')
    else:
        break

def jisuan(a,n):
    sn=     