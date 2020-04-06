# -*- coding: utf-8 -*-
# @Time : 2019/8/23 0:24
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)
a=filter(lambda x:x%2==0,a)
print(list(a))