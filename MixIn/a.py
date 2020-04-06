# -*- coding: utf-8 -*-
# @Time : 2019/10/5 20:04
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
# 英雄
class Hero:
    isHero = True


# 野怪
class Wild_monster:
    isWildMonster = True


# # AD英雄
# class AD(Hero):
#     ADCarry = True


# # AP英雄
# class AP(Hero):
#     APCarry = True
#
#
# # 德玛西亚阵营的AD英雄
# class AdDemacia(AD):
#     pass
#
#
# # 诺克萨斯阵营的AD英雄
# class AdNoxus(AD):
#     pass
#
#
# # 德玛西亚阵营的AP英雄
# class ApDemacia(AP):
#     pass
# garen=ApDemacia
#
# # 诺克萨斯阵营的AP
# class ApNoxus(AP):
#     pass
#
#

class AD:
    pass


class AP:
    pass


# 德玛西亚阵营
class Demacia:
    pass


# 诺克萨斯阵营
class Noxus:
    pass


class Garen(Hero, AD, Demacia):
    pass

# class Garen(AD,Demacia):
#     pass
#
# class
#
#     # 德玛西亚阵营的AD英雄盖伦
#     class Garen(AD):
#         comefromDemacia = True
#
#     # 诺克萨斯阵营的AD英雄诺手
#     class Darius(AD):
#         ComeFromNoxus = True
#
#     # 德玛西亚阵营的AP英雄莫甘娜
#     class Morgana(AP):
#         comefromDemacia = True
#
#     # 诺克萨斯阵营的AP英雄瑞文
#     class Riven(AP):
#         ComeFromNoxus = True
