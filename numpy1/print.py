# -*- coding: utf-8 -*-
# @Time : 2019/11/28 16:38
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : print.py
# @Software: PyCharm
import numpy as np

# a = np.array(['a', 'b', 'c'])
# print(a)

# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.ndim)  # 数组的维度(轴)的个数
# print(a.shape)  # 数组的形状(维度)
# print(a.size)  # 数组中元素的个数
# print(a.dtype)  # 数组中元素的类型
# print(a.itemsize)  # 数组中每个元素所占字节数
# print(a.data)  # 存储数组内元素的内存缓冲区地址，一般不用

np.set_printoptions(threshold=10000)
a = np.arange(10000).reshape((100, 100))
print(a)
