# -*- coding: utf-8 -*-
# @Time : 2019/10/24 19:34
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : ClassDecorator.py
# @Software: PyCharm
import time


class Decorator:
    def __init__(self, fun):
        self._fun = fun

    def __call__(self, *args, **kwargs):
        start = time.clock()
        self._fun(*args)
        end = time.clock()
        print(f'函数的运时间为{str(end-start)}')


@Decorator  # add=Decorator(add)
def add(*args):
    print(sum(args))


add(1, 2, 3, 4, 5)
