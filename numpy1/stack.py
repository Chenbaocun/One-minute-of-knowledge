# -*- coding: utf-8 -*-
# @Time : 2019/12/12 19:03
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : stack.py
# @Software: PyCharm
import numpy as np

a = np.array([1, 2])[:,np.newaxis]
b = np.array([3, 4])[:,np.newaxis]
c = np.array([5, 6])[:,np.newaxis]
# print(a.shape)
d = np.stack((a, b, c), axis=0)
d = np.concatenate((a, b, c), axis=1)
print(d)
