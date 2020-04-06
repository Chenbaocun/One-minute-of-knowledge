# -*- coding: utf-8 -*-
# @Time : 2019/8/24 20:35
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a=[x for x in range(10)]
print(a)
a={x for x in range(10)}
print(a)
a={x:x%2==0 for x in range(10)}
print(a)