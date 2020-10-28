#coding=utf-8
import re

def qiangkouling(a):
    k_1Regex=re.compile(r"\d+")
    k_2Regex=re.compile(r".{8,}")
    k_3Regex=re.compile(r"[a-z]+")
    k_4Regex=re.compile(r'[A-Z]+')
    mo1=k_1Regex.search(a)
    mo2=k_2Regex.search(a)
    mo3=k_3Regex.search(a)
    mo4=k_4Regex.search(a)
    print(mo1.group())
    print(mo2.group())
    print(mo3.group())
    print(mo4.group())

qiangkouling("wwwAAA11111111111111111111111111111")#至少有1个数字，一个大写字母，一个小写字母，位数大于等于8，才不会报错。