# -*- coding: utf-8 -*-
# @Time : 2019/8/7 15:41
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a=['a','c','c','b','a','d','a','b']
a1=list(set(a))
print(a1)
a1.sort(key=a.index)
print(a1)