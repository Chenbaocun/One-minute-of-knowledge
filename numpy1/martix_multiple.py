# -*- coding: utf-8 -*-
# @Time : 2019/11/30 22:24
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : martix_multiple.py
# @Software: PyCharm
import numpy as np

a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)
print(a)
print(b)
# print(a @ b)
a1 = np.matrix(a)  # np.matrix只能是二维的
b1 = np.mat(b)
print(a1)
print(b1)
print(a1 * b1)
