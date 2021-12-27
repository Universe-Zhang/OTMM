# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:04
# @Author  : Zy
# @File    : example.py
# @Software: PyCharm

import util.location as ul
import numpy as np
from scipy.special import comb, perm
from copy import deepcopy
import match.init_matrix as mi


def get_opt(matrix, plan):
    s = 0.0
    for i in range(len(plan) // 2):
        s += matrix[i, plan[2 * i], plan[2 * i + 1]]
    return s


def BTWBB(matrix):
    plan = []
    occupy = [False] * 2 * matrix.shape[0]
    opt_value = float('inf')
    opt_plan = []
    opt = dict()
    opt['value'] = opt_value
    opt['plan'] = opt_plan
    v = subproblem(matrix, plan, occupy, opt)
    return opt['value'], opt['plan']


def subproblem(matrix, plan, occupy, opt):
    if len(plan) == 2 * matrix.shape[0]:
        v = get_opt(matrix, plan)
        # print(v,plan)
        if v < opt['value']:
            opt_value = v
            opt_plan = deepcopy(plan)
            tv = get_opt(matrix, plan)
            opt['value'] = opt_value
            opt['plan'] = opt_plan
        # return opt_value,opt_plan
        return
    elif get_opt(matrix, plan) > opt['value']:
        # return opt_value,opt_plan
        return
    else:
        for r1 in range(0, 2 * matrix.shape[0]):
            if occupy[r1]:
                continue
            occupy[r1] = True
            plan.append(r1)
            for r2 in range(r1 + 1, 2 * matrix.shape[0]):
                if occupy[r2]:
                    continue
                occupy[r2] = True
                plan.append(r2)
                subproblem(matrix, plan, occupy, opt)
                # if v < opt_value:
                #     opt_value = v
                #     # opt_plan = plan.copy()
                plan.remove(r2)
                occupy[r2] = False

            plan.remove(r1)
            occupy[r1] = False
        # return opt_value,opt_plan
        return


if __name__ == '__main__':
    D, R = mi.instance_1
    print(len(D))
    print(len(R))
    matrix, pm = mi.value_matrix(D, R)
    N = len(R)
    print(matrix.shape)
    sume, answerf = BTWBB(matrix)
    print(answerf)
    print(sume)

"""
37485.532943654354
6606.7 + 15079.5 + 15799.4
[0, 4, 1, 3, 2, 5]

[0, 4, 1, 3, 2, 5]
0.37926098927838026
"""
