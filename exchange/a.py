# -*- coding: utf-8 -*-
# @Time : 2019/8/25 21:11
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
# a=1
# b=2
# c=3
# # temp=a
# # a=b
# # b=temp
# # print(a,b)
# # b,a=a,b
# # print(a,b)
# c,b,a=a,b,c
# print(a,b,c)
# 斐波那契数列

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fib(5)