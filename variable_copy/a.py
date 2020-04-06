# -*- coding: utf-8 -*-
# @Time : 2019/8/14 9:33
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm

#直接引用
a=[1,2,3]
b=a
print("变量a所在内存地址为："+str(id(a))+'-值为'+str(a))
print("变量b所在内存地址为："+str(id(b))+'-值为'+str(b))
# a=[4,5,6]
a[0]=4
a[1]=5
a[2]=6
print("变量a所在内存地址为："+str(id(a))+'-值为'+str(a))
print("变量b所在内存地址为："+str(id(b))+'-值为'+str(b))



