# -*- coding: utf-8 -*-
# @Time : 2019/12/2 22:50
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : function_plot.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt


def square(x):
    return -x ** 2 + 1


a = np.linspace(-5, 5, 200)
# print(a)
print(square(a).shape)
plt.plot(a, square(a))
plt.show()
