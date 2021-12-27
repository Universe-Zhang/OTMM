# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 9:18
# @Author  : Zy
# @File    : Figure1a.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

t_x = 900
w = 1 / 900


def function(x):
    x = np.array(x)
    obj = np.zeros(x.shape)
    obj[x <= t_x] = 1
    obj[x > t_x] = w * x[x > t_x] - w * t_x + 1
    return obj


def draw(x, y, text=None, ):
    x = x
    y = y
    # plt.xlim(,2000)
    plt.ylim(0, 2.5)
    print(x)
    print(y)

    plt.vlines([t_x, 1800], 0, [1, 2], linestyle="dashed")
    # plt.hlines(1, 0, t_x, linestyle="dashed")
    plt.xticks([0, 900, 1800], ['0', '$^{δ_{driver}^{acp}}$', '$^{δ_{driver}^{max}}$'], fontsize=20)
    plt.yticks([1], [1], fontsize=20)
    plt.plot(x, y)
    plt.xlabel('delay', fontsize=20)
    plt.ylabel('τ', fontsize=20)

    plt.subplots_adjust(left=0.12, bottom=0.15, right=0.95, top=0.95, )
    plt.show()


x = np.arange(0, 1800)
y = function(x)
draw(x, y)
