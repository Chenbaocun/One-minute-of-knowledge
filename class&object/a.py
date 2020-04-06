# -*- coding: utf-8 -*-
# @Time : 2019/9/23 19:28
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
# 英雄类
# 英雄类
class Hero:
    # 构造函数
    a='1'
    def __init__(self, chinesename, slogan):
        # 实例变量（成员变量）
        self.chinesename = chinesename
        self.slogan = slogan

    # 实例方法
    def flash(self):
        print(self.chinesename + ":我闪了过去")


yasuo = Hero("亚索", 'Death is like wind, always by my side!')
yasuo.flash()
print(yasuo.__dict__)

garen=Hero('盖伦','For Demacia!!')
print(garen.__dict__)
garen.flash()
