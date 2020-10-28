import sys

import math

#斐波那契数列 ，输入数字n，打印出第n个斐波那契数列中的第n个数字

# 使用递归
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(1))


