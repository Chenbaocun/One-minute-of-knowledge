# -*- coding: utf-8 -*-
# @Time : 2019/10/7 23:32
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
def add(x,y):
    print(x+y)
add(1,2)
print(add)
b=add
b(2,2)
print(b is add)

def temp(x,y,fun):
    fun(x,y)
temp(3,2,add)

def temp1(x,y):
    def add():
        print(x+y)
    return add
temp1(4,2)()


