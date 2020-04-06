# -*- coding: utf-8 -*-
# @Time : 2019/10/3 20:15
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
class Hero:
    game = 'League of legend'

    def __init__(self, chinesename):
        self.chinesename = chinesename

    def flash(self):
        print(self.chinesename + ':我闪了过去！')


class AD(Hero):
    slogan = 'Everything in the world is tied to an arrow!'

    def Q(self):
        print("嘟嘟嘟嘟嘟嘟！")



