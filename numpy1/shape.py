# -*- coding: utf-8 -*-
# @Time : 2019/12/4 15:36
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : shape.py
# @Software: PyCharm
import numpy as np

a = np.arange(12)
print(id(a))
b = a.reshape((3, 4))
print(a)
print(id(b))
a.resize((3, 4))
print(id(a))

print(a.T)
print(a.flat)
for i in a.flat:
    print(i)