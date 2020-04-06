# -*- coding: utf-8 -*-
# @Time : 2019/8/10 17:27
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
def main():
    global a
    a=2
    print("函数内的a="+str(a))
a=1
main()
print("函数外的a="+str(a))
def fun1():
    a1=1
    def fun2():
        nonlocal a1
        a1=a1*2
        print(a1)
    return fun2()
fun1()

