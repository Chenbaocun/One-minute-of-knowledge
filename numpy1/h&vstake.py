# -*- coding: utf-8 -*-
# @Time : 2019/12/6 14:17
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : hs.py
# @Software: PyCharm
import numpy as np

a = np.arange(4).reshape((2, 2))
b = np.arange(4, 8).reshape((2, 2))
print(np.hstack([a, b]))
