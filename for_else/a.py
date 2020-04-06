# -*- coding: utf-8 -*-
# @Time : 2019/9/18 19:49
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
# import random
#
# a = []
# for i in range(10):
#     a.append(random.randint(1, 10))
# print(a)
# import random
#
# a = []
# for i in range(10):
#     a.append(random.randint(1, 10))
# print(a)
a = [1, 2, 3, 4]
print(id(a[1]))
# flag = 0
for i in a:
    if i == 4:
        # flag = 1
        a[a.index(i)] = i ** 2
        print(id(a[1]))
        break
else:
    print("列表中没有")
# if flag:
#     pass
# else:
#     print("列表中没有2")
