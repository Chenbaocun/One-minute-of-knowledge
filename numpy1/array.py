# -*- coding: utf-8 -*-
# @Time : 2019/11/25 11:33
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : array.py
# @Software: PyCharm
a = [1, 2, 3, 4]
a1 = [1, '2', [3]]
print(type(a1))

from array import array

a3 = array('q', (1000, 2000, 3000))
print(help(array))
print(id(a3[0]),id(a3[1]))