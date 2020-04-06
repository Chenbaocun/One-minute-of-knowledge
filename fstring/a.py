# -*- coding: utf-8 -*-
# @Time : 2019/11/17 16:22
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
import decimal

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f'result: {value:{0}{width}.{precision}}')
print(abs.__annotations__)