# -*- coding: utf-8 -*-
# @Time : 2019/12/19 16:26
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : r_&c_.py
# @Software: PyCharm
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
# print(np.concatenate((a,b),axis=0))
# print(np.r_[np.arange(0, 5, 1), a, b])
# print(np.r_[np.linspace(0, 5, 1), a, b])
print(np.r_['0', a, b])
# print(a)
