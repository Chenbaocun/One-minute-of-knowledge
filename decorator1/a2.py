# -*- coding: utf-8 -*-
# @Time : 2019/10/13 15:31
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a2.py
# @Software: PyCharm
import time
def CalTime(fun):
    def In():
        start = time.clock()
        fun()
        end = time.clock()
        print("函数运行时间为：" + str(end - start))
    return In
@CalTime
def a():
    # start=time.clock()
    temp=[]
    for i in range(100000):
        temp.append("LPL,给爷杀！！")
    print(len(temp))
    # end=time.clock()
    # print("函数运行时间为："+str(end-start))
a()
# print(CalTime(a))
# new_a=CalTime(a)
# new_a()
