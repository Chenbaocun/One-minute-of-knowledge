# -*- coding: utf-8 -*-
# @Time : 2019/8/9 17:29
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCha
def main(arg,*args,**kwargs):
    print(type(arg))
    print(type(args))
    print(type(kwargs))
main(1,2,2,2,2,2,2,Student="学生",Teacher="老师")