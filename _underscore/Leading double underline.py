# -*- coding: utf-8 -*-
# @Time : 2019/11/9 18:42
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : Leading double underline.py
# @Software: PyCharm
# class Hero:
#     def __init__(self,name,chinesename):
#         self.name=name
#         self.__chinesename=chinesename
#     def __flash(self):
#         print(111)
# garen=Hero('garen',"盖伦")
# print(garen.name)
# print(dir(garen))
#
# print(garen.__flash())

def f2(a, b, c, * , d, **kw):
    print(f'a={a},b={b},c={c},d={d},kw={kw}')
    # print('a=',a,'b=',b)

args = (1, 2, 3)
dict = {'d': 88, 'x': '#'}
# print(*dict)
f2(*args, **dict)


