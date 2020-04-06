# -*- coding: utf-8 -*-
# @Time : 2019/10/18 16:12
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a4.py
# @Software: PyCharm
import time
def out(a):
    print(a)
    def CalTime(fun):
        print(fun)
        def In(*args):
            print(args)
            start = time.clock()
            fun(*args)
            end = time.clock()
            print("函数的运行时间为：" + str(end - start))

        return In
    return CalTime

@out(0)
def add(*args):
    print(sum(args))
add(1,2)