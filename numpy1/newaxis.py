# -*- coding: utf-8 -*-
# @Time : 2019/12/16 15:51
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : newaxis.py
# @Software: PyCharm
import numpy as np

a = np.arange(4).reshape((2, 2))
print(a[:, :, np.newaxis].shape)
