# -*- coding: utf-8 -*-
# @Time : 2019/11/29 18:55
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : broadcast.py
# @Software: PyCharm
import numpy as np

a = [i for i in range(12)]
print(a)

b = np.arange(12).reshape((3, 4))
print(b < 5)
