# -*- coding: utf-8 -*-
# @Time : 2019/10/21 19:50
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : MultiDecorator.py
# @Software: PyCharm
def a(fun):
    print("执行了装饰器a")
    def In():
        print("aaaaaaaa")
        fun()
    return In

def b(fun):
    print("执行了装饰器b")
    def In():
        print("bbbbbbbbbb")
        fun()
    return In
@b
@a
def main():
    print("执行了main函数")

main()