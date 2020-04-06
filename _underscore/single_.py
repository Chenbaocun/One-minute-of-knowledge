# -*- coding: utf-8 -*-
# @Time : 2019/11/12 17:31
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : single_.py
# @Software: PyCharm


# vim: set fileencoding=utf-8
# a = [1, 2, 3, 4]
# a1, _, _, a4 = a
# print(a1, a4)
# print(_)
# for _ in range(10):
#     print("循环了一次")

# from sklearn import linear_model
#
# reg = linear_model.LinearRegression()
# reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# print(reg.coef_)
a = 100_0000
print(a)
b=0xFF_FF_FF_FF
print(b)

print('{:_}'.format(1000000))
print('{:_d}'.format(1000000))