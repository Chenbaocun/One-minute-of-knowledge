# -*- coding: utf-8 -*-
# @Time : 2019/10/16 18:03
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a3.py
# @Software: PyCharm
import time
def out(a):
    print(a)
    def CalTime(fun):
        print(fun)
        def In(x, y):
            print(x,y)
            start = time.clock()
            fun(x, y)
            end = time.clock()
            print("函数运行时间为：" + str(end - start))

        return In
    return CalTime


# @CalTime
# def a():
#     temp=[]
#     for i in range(100000):
#         temp.append("LPL,给爷杀！！")
#     print(len(temp))
# a()
@out(0)
def add(x,y):
    print(x+y)
add(1,2)
