# -*- coding: utf-8 -*-
# @Time : 2019/10/4 19:56
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
class Hero:
    def __init__(self,chinesename):
        self.chinesename=chinesename
class AD(Hero):
    def __init__(self,chinesename,gender):
        self.chinesename=chinesename
        # Hero.__init__(self,chinesename)
        # super(AD,self).__init__(chinesename)
        self.gender=gender
    pass
ashe=AD("艾希")
print(ashe.__dict__)

