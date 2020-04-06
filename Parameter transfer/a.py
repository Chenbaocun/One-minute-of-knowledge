# -*- coding: utf-8 -*-
# @Time : 2019/9/4 14:17
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a = 0


def main(num):
    num = 1
    print("函数内部的a=" + str(id(num)))


main(a)
print("调用函数后的a=" + str(id(a)))
# a = [0, 0, 0, 0]
#
#
# def main(list):
#     # list[0] = 1
#     list=[0]
#     print("函数内的a=" + str(id(list)))
#
#
# main(a)
# print("调用函数后的a=" + str(id(a)))
