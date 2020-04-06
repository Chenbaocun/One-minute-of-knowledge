# -*- coding: utf-8 -*-
# @Time : 2019/12/1 16:32
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : slice.py
# @Software: PyCharm
import numpy as np

a = np.arange(12).reshape(4, 3)
print(a)
print(a[1:3:, :0:-1])
for i in a.flat:
    print(i)
