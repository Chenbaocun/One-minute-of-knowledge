# -*- coding: utf-8 -*-
# @Time : 2019/10/29 22:48
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : decorator_for_class.py
# @Software: PyCharm
def decorator(cls):
    cls.x=1
    cls.y=2
    return cls

@decorator#new_class=decorator(Person)
class Person:
    pass
# person=Person()
print(Person.__dict__)