# -*- coding: utf-8 -*-
# @Time : 2019/11/17 17:04
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : a.py
# @Software: PyCharm
def flash(chinesename: str, status: bool) -> int:
    if status:
        print(f'我{chinesename}闪了过去！')
        return 1
    else:
        print("老子闪现还提莫CD呢！")
        return 0


flash("亚索", False)
