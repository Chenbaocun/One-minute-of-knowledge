# -*- coding: utf-8 -*-
# @Time : 2019/11/12 15:23
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : magic_method.py
# @Software: PyCharm
class Hero:
    def __init__(self, name, chinesename):
        self.name = name
        self.chinesename = chinesename


garen = Hero("garen", '盖伦')

a = 'garen'
print(len(a))
