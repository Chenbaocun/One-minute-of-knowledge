# -*- coding: utf-8 -*-
# @Time : 2019/12/12 19:07
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : concatenate.py
# @Software: PyCharm
import numpy as np

a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
b=((5,6))
# print(a.shape)
# print(b.shape)
c = np.concatenate((a, b), axis=0)
print(c)
