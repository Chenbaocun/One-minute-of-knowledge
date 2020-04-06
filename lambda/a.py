# -*- coding: utf-8 -*-
# @Time : 2019/8/8 10:41
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
a=lambda x:x**2
print(a(2))
b=lambda x,y:x if x>y else y
print(b(1,2))
a_list=[lambda x:x.strip(),lambda x:x**2]
print(a_list)
print(a_list[0]('giao      '))
print(a_list[1](3))
def main():
    return lambda x:x**2
print(main())
print(main()(4))
