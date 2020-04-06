# -*- coding: utf-8 -*-
# @Time : 2019/9/2 20:36
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
import time

a = ''
start = time.clock()
for i in range(10000000):
    a += 'a'
end = time.clock()
print("程序运行时间为" + str(end - start))
print(len(a))
# a = []
# for i in range(10000000):
#     a.append("a")
# start = time.clock()
# ''.join(a)
# end = time.clock()
# print(len(a))
# print("程序运行时间为：" + str(end - start))
