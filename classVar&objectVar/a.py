# -*- coding: utf-8 -*-
# @Time : 2019/9/26 20:38
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
class Hero:
    # 类变量
    game = '英雄联盟'
    def __init__(self,chinesename):
        #实例变量，由每个对象自行赋值，互不影响
        self.chinesename=chinesename
    def flash(self):
        #局部变量
        a=0
        print(self.chinesename)
        print(Hero.game)
    # def heal(self):
    #     print(a)

yasuo = Hero("亚索")
yasuo.game='DNF'
print(id(yasuo.game))
print(id(Hero.game))
yasuo.flash()
# garen=Hero('盖伦')
# print(yasuo.chinesename)
# print(garen.chinesename)
# print(yasuo.game)
# print(garen.game)
# print(yasuo.game)
# yasuo.game = 'DNF'
# print(yasuo.game)
# del yasuo.game
# print(yasuo.game)

