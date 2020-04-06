# -*- coding: utf-8 -*-
# @Time : 2019/8/15 10:23
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : b.py
# @Software: PyCharm
import copy
a=[1,2,3,4,[4,5,6,7]]
b=copy.copy(a)
print("变量a所在内存地址为："+str(id(a))+'-值为'+str(a))
print("变量b所在内存地址为："+str(id(b))+'-值为'+str(b))
a[4].append(100)
print("变量a所在内存地址为："+str(id(a))+'-值为'+str(a))
print("变量b所在内存地址为："+str(id(b))+'-值为'+str(b))