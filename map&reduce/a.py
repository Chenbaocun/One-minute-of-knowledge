# -*- coding: utf-8 -*-
# @Time : 2019/8/18 11:15
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i**2)
print(b)
# def mul(num):
#     return num**2
# print(list(map(mul,a)))
print(sum(a))
#累乘呢？
rst=1
for i in a:
    rst*=i
print(rst)


