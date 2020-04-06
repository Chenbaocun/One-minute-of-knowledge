# -*- coding: utf-8 -*-
# @Time : 2019/9/9 19:11
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a = 'a'
b = 1
c = (1, 2)
d = [1, 2]
e = {'a': 1, 'b': b}
print("a={a} b={b}".format(**e))
a = {'1': 11, '2': 22, '3': 33}
print("{1}".format(**a))
