# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 22:35
# @Author  : Zy
# @File    : route number.py
# @Software: PyCharm

from scipy.special import perm

l = {}


def fun(i, j):
    if i == 0:
        return perm(j, j)
    elif j > i:
        a = (i) * fun(i - 1, j) + (j - i) * fun(i, j - 1)
        return a
    else:
        a = (i) * fun(i - 1, j)
        if i == j:
            l[i] = a
        return a


print(fun(10, 10))
print(l)
