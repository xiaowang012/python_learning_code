#分解字符串中英文字母，空格，数字和其他字符的个数
import string

zifuchuan=input('请输入一段字符串：')
zimu=0
space=0
shuzi=0
others=0
for a in zifuchuan:
    if a.isalpha():
        zimu+=1
    elif a.isspace():
        space+=1
    elif a.isdigit():
        shuzi+=1
    else:
        others+=1
print('字母数为：'+str(zimu))
print('空格数为：'+str(space))
print('数字个数为:'+str(shuzi))
print('其他的为:'+str(others))