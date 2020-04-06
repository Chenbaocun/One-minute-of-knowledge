# -*- coding: utf-8 -*-
# @Time : 2019/9/25 22:20
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
class Hero:
    #构造函数
    def __init__(self,chinesename):
        self.chinesename=chinesename
    # 实例方法
    def flash(self):
        print(self.chinesename+":我闪了过去！")
        print(self)


yasuo = Hero("亚索")
# yasuo.flash()
Hero.flash(yasuo)
print(yasuo)
