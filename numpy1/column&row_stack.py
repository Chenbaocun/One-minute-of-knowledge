# -*- coding: utf-8 -*-
# @Time : 2019/12/17 17:10
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : column&row_stack.py
# @Software: PyCharm
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[4, 5, 6], [7, 8, 9]])
c = np.column_stack((a, b))
print(c)
