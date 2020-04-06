# -*- coding: utf-8 -*-
# @Time : 2019/10/24 15:22
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : __call__.py
# @Software: PyCharm
def a():
    print("大家好我是棋子！")
a()
print(callable(a))

class B:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print("大家好我是棋子！")
print(callable(B))
b=B()
print(callable(b))
b()