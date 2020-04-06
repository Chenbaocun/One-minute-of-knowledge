# -*- coding: utf-8 -*-
# @Time : 2019/9/28 15:27
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
class Hero:
    # 类变量
    game = '英雄联盟'

    # 实例方法
    def flash(self):
        print(self.game)
        print(Hero.game)
    #类方法
    @classmethod
    def heal(cls,yasuo):
        print(cls.game)
        print(yasuo.game)
    #静态方法
    @staticmethod
    def ignit(yasuo):
        print("使用了点燃")
        print(Hero.game)
        print(yasuo.game)


yasuo = Hero()
yasuo.game = 'DNF'
yasuo.flash()
yasuo.heal(yasuo)
Hero.ignit(yasuo)
