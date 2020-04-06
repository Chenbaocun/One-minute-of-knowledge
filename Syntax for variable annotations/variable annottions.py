# -*- coding: utf-8 -*-
# @Time : 2019/11/19 14:33
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : variable annottions.py
# @Software: PyCharm
from typing import Dict, List

a = 1  # type:int
b = False  # type:bool
c = []  # type:List[int]
d = {}  # type:Dict[str,int]

a1: int
b1: bool = False
c1: List[int] = []
d1: Dict[str, int] = {}


