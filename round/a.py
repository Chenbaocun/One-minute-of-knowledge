# -*- coding: utf-8 -*-
# @Time : 2019/8/29 18:04
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
b = 1
a = 'b+1'
print(str(eval(a,{'b':3},{'b':5})))
print(b)
print(eval("for i in range(10):"
           "print(i)"))