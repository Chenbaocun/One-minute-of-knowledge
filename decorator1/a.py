# -*- coding: utf-8 -*-
# @Time : 2019/10/11 22:28
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
import time
def out(fun):
    def In():
        start=time.clock()
        fun()
        end=time.clock()
        print("函数运行时间为："+str(end-start))
    return In
# In=out(1)
# In()
@out
def append():
    a=[]
    for i in range(100000):
        a.append("棋子带帅比嗷！")
# append=out(append)
append()