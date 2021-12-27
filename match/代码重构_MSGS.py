# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:04
# @Author  : Zy
# @File    : example.py
# @Software: PyCharm

import util.location as ul
import numpy as np
import time
import pandas as pd
import match.init_matrix as mi
import statics
import copy


# 随机算子
# def iteratorA(matrix, result, num=2):
#     x_size, y_size = matrix.shape
#     len_result = len(result)
#     instance_index = np.random.choice(range(len_result), size=num, replace=False)
#     if type(result) != type([1]):
#         result = result.tolist()
#     instance = np.array(result)[instance_index].tolist()
#     instance = np.array(instance)
#     x_indexs = instance[:, 0]
#     y_indexs = instance[:, 1]
#     x_indexs = x_indexs.astype('int64').tolist()
#     y_indexs = y_indexs.astype('int64').tolist()
#     return matrix[x_indexs][:, y_indexs], instance_index, x_indexs, y_indexs


# 发散算子
def iteratorA(matrix, result, Tabu):
    # print(result)
    d_size, x_size, y_size = matrix.shape
    d_ind = np.random.choice(range(d_size), size=2, replace=False)
    r_ind = np.random.choice(range(1, 3), size=2, replace=True)
    t = result[d_ind[0]].copy()
    result[d_ind[0]][r_ind[0]] = result[d_ind[1]][r_ind[1]]
    # print(result[d_ind[0]][0:3])
    # print(result[d_ind[0]][0],result[d_ind[0]][1],result[d_ind[0]][2])
    # print(matrix[result[d_ind[0]][0],result[d_ind[0]][1],result[d_ind[0]][2]])
    result[d_ind[1]][r_ind[1]] = t[r_ind[0]]

    result[d_ind[0]][-1] = matrix[result[d_ind[0]][0], result[d_ind[0]][1], result[d_ind[0]][2]]
    result[d_ind[1]][-1] = matrix[result[d_ind[1]][0], result[d_ind[1]][1], result[d_ind[1]][2]]
    # print(result)

    # instance_index = np.random.choice(range(x_size), size=2, replace=False)
    # ax = instance_index[0]
    #     ai = None
    #     bx = instance_index[1]
    #     bi = None
    #     for ii,i in enumerate(result):
    #         if i[0]==ax:
    #             ai = ii
    #         if i[0]==bx:
    #             bi = ii
    #         if ai is not None and bi is not None:
    #             break
    #     if ai is None:
    #         if bi is None:
    #             return
    #         else:
    #             result[bi] = [ax,result[bi][1],matrix[ax][result[bi][1]]]
    #     else:
    #         if bi is None:
    #             result[ai] = [bx,result[ai][1],matrix[bx][result[ai][1]]]
    #         else:
    #             result[ai] = [bx,result[ai][1],matrix[bx][result[ai][1]]]
    #             result[bi] = [ax,result[bi][1],matrix[ax][result[bi][1]]]
    # else:
    #     instance_index = np.random.choice(range(y_size), size=2, replace=False)
    #     ay = instance_index[0]
    #     ai = None
    #     by = instance_index[1]
    #     bi = None
    #     for ii, i in enumerate(result):
    #         if i[1] == ay:
    #             ai = ii
    #         if i[1] == by:
    #             bi = ii
    #         if ai is not None and bi is not None:
    #             break
    #     if ai is None:
    #         if bi is None:
    #             return
    #         else:
    #             result[bi] = [result[bi][0], ay, matrix[result[bi][0]][ay]]
    #     else:
    #         if bi is None:
    #             result[ai] = [ result[ai][0],by, matrix[result[ai][0]][by]]
    #         else:
    #             result[ai] = [ result[ai][0],by, matrix[result[ai][0]][by]]
    #             result[bi] = [result[bi][0], ay, matrix[result[bi][0]][ay]]


# a = np.arange(15).reshape(3,5)
# print(a)
# result = [[0,0,0],[1,1,4],[2,2,8]]
# iteratorA(a,result)
# print(result)


# 概率上山算子
def iteratorB(matrix, result, Tabu):
    d_size, x_size, y_size = matrix.shape
    len_result = len(result)
    # print(range(len_result))
    # print(0,len_result)
    d_ind = np.random.randint(0, d_size, )
    d1 = result[d_ind]  # 随机的第一个选取对象
    r1 = d1[1]
    r2 = d1[2]
    e_d1 = d1[0]
    r_t = np.zeros(shape=(x_size, y_size))
    r_t[r1, :] = d1[3] - matrix[d_ind][r1, :]
    r_t[:, r2] = d1[3] - matrix[d_ind][:, r2]
    r_t[np.where(r_t < 0)] = 0
    # r_t+=+ 0.0001
    r_t_b = r_t[r_t > 0]
    if len(r_t_b) == 0:
        return
    # print(r_t_b)

    r_t_p = r_t_b / r_t_b.sum()
    # print(r_t_p)
    r2_ind = np.random.choice(list(range(len(r_t_b))), replace=False, p=r_t_p)
    # print(instance_index2)
    # print(np.where(r_t>0))
    # print(np.where(r_t>0)[0][instance_index2])
    # print(np.where(r_t>0)[1][instance_index2])
    r1_a = np.where(r_t > 0)[0][r2_ind]
    r1_b = np.where(r_t > 0)[1][r2_ind]
    e_r1 = r1
    e_r2 = r2
    if r1_a == r1:
        e_r3 = r1_b
    else:
        e_r3 = r1_a
    e_r4 = -1
    e_d2 = -1
    for i in result:
        if i[1] == e_r3:
            e_r4 = i[2]
            e_d2 = i[0]
            break
        elif i[2] == e_r3:
            e_r4 = i[1]
            e_d2 = i[0]
            break
        else:
            pass
    # print(e_r1, e_r2, e_r3, e_r4)
    # print(e_d1, e_d2)
    # if e_r4 == -1 or e_r1 == e_r2 or e_r3 == e_r4:
    #     print('asdasd')
    # print(matrix[e_d1, e_r1, e_r2] + matrix[e_d2, e_r3, e_r4], matrix[e_d1, e_r1, e_r3] + matrix[e_d2, e_r2, e_r4])
    if matrix[e_d1, e_r1, e_r2] + matrix[e_d2, e_r3, e_r4] >= matrix[e_d1, e_r1, e_r3] + matrix[e_d2, e_r2, e_r4]:
        result[e_d1] = [e_d1, e_r1, e_r3, matrix[e_d1, e_r1, e_r3]]
        result[e_d2] = [e_d2, e_r2, e_r4, matrix[e_d2, e_r2, e_r4]]


# 最大上山算子
def iteratorC(matrix, result, Tabu):
    d_size, x_size, y_size = matrix.shape
    len_result = len(result)
    # print(range(len_result))
    # print(0,len_result)
    d_ind = np.random.randint(0, d_size, )
    d1 = result[d_ind]  # 随机的第一个选取对象
    r1 = d1[1]
    r2 = d1[2]
    e_d1 = d1[0]
    r_t = np.zeros(shape=(x_size, y_size))
    r_t[r1, :] = d1[3] - matrix[d_ind][r1, :]
    r_t[:, r2] = d1[3] - matrix[d_ind][:, r2]
    r_t[np.where(r_t < 0)] = 0
    # r_t+=+ 0.0001
    r_t_b = r_t[r_t > 0]
    if len(r_t_b) == 0:
        return
    # print(r_t_b)

    # r_t_p = r_t_b / r_t_b.sum()
    # print(r_t_p)
    r2_ind = np.argmax(r_t_b)
    # print(instance_index2)
    # print(np.where(r_t>0))
    # print(np.where(r_t>0)[0][instance_index2])
    # print(np.where(r_t>0)[1][instance_index2])
    r1_a = np.where(r_t > 0)[0][r2_ind]
    r1_b = np.where(r_t > 0)[1][r2_ind]
    if r1_a == r1:
        return
    e_r1 = r1
    e_r2 = r2
    if r1_a == r1:
        e_r3 = r1_b
    else:
        e_r3 = r1_a
    e_r4 = -1
    e_d2 = -1
    for i in result:
        if i[1] == e_r3:
            e_r4 = i[2]
            e_d2 = i[0]
            break
        elif i[2] == e_r3:
            e_r4 = i[1]
            e_d2 = i[0]
            break
        else:
            pass
    # print(e_r1, e_r2, e_r3, e_r4)
    # print(e_d1, e_d2)
    # if e_r4 == -1 or e_r1 == e_r2 or e_r3 == e_r4:
    #     print('asdasd')
    # print(matrix[e_d1, e_r1, e_r2] + matrix[e_d2, e_r3, e_r4], matrix[e_d1, e_r1, e_r3] + matrix[e_d2, e_r2, e_r4])
    if matrix[e_d1, e_r1, e_r2] + matrix[e_d2, e_r3, e_r4] >= matrix[e_d1, e_r1, e_r3] + matrix[e_d2, e_r2, e_r4]:
        result[e_d1] = [e_d1, e_r1, e_r3, matrix[e_d1, e_r1, e_r3]]
        result[e_d2] = [e_d2, e_r2, e_r4, matrix[e_d2, e_r2, e_r4]]

    #
    # # 随机的第2个选取对象
    # by = list_bi[instance_index2[0]]
    # bi = None
    # bw = 0
    # for r in range(len_result):
    #     if result[r][1] == by:
    #         bi = r
    #         bx = result[r][0]
    #         bw = result[r][2]
    #         break
    # if bi is None:
    #     if (aw <= matrix[ax][by]):
    #         result[ai] = [ax, by, matrix[ax][by]]
    # else:
    #     if (aw + bw <= matrix[ax][by] + matrix[bx][ay]):
    #         result[ai] = [ax, by, matrix[ax][by]]
    #         result[bi] = [bx, ay, matrix[bx][ay]]


# a = np.arange(15).reshape(3,5)
# print(a)
# result = [[0,2,a[0][2]],[1,1,a[1][1]],[2,0,a[2][0]]]
# iteratorB(a,result)
# print(result)
#
# # 贪婪上山算子
# def iteratorC(matrix, result):
#     x_size, y_size = matrix.shape
#     len_result = len(result)
#     instance_index = np.random.choice(range(len_result), size=1, replace=False, )
#     ai = instance_index[0]
#     a = result[ai]  # 随机的第一个选取对象
#     # print(a)
#     ax = a[0]
#     ay = a[1]
#     aw = a[2]
#     if x_size <= y_size:
#         by = ay
#         for j in range(y_size):
#             if j != ay and matrix[ax, j] >= matrix[ax][by]:
#                 by = j
#         if by == ay:
#             return
#         bi = None
#         bw = 0
#         for r in range(len_result):
#             if result[r][1] == by:
#                 bi = r
#                 bx = result[r][0]
#                 bw = result[r][2]
#                 break
#         if bi is None:
#             if (aw <= matrix[ax][by]):
#                 result[ai] = [ax, by, matrix[ax][by]]
#         else:
#             if (aw + bw <= matrix[ax][by] + matrix[bx][ay]):
#                 result[ai] = [ax, by, matrix[ax][by]]
#                 result[bi] = [bx, ay, matrix[bx][ay]]
#     else:
#         bx = ax
#         for j in range(x_size):
#             if j != ax and matrix[j, ay] >= matrix[bx][ay]:
#                 bx = j
#         if bx == ax:
#             return
#         bi = None
#         bw = 0
#         for r in range(len_result):
#             if result[r][0] == bx:
#                 bi = r
#                 by = result[r][1]
#                 bw = result[r][2]
#                 break
#         if bi is None:
#             if (aw <= matrix[bx][ay]):
#                 result[ai] = [bx, ay, matrix[bx][ay]]
#         else:
#             if (aw + bw <= matrix[ax][by] + matrix[bx][ay]):
#                 result[ai] = [ax, by, matrix[ax][by]]
#                 result[bi] = [bx, ay, matrix[bx][ay]]


# a = np.arange(15).reshape(5,3)
# print(a)
# result = [[0,2,a[0][2]],[1,1,a[1][1]],[2,0,a[2][0]]]
# iteratorC(a,result)
# print(result)


def get_total_value(ll):
    sum_a = 0
    for i in ll:
        sum_a += i[3]
    return sum_a


#
# def optimize_mode_C(matrix,drivers,riders,name=None,fname=None, times = static.times, trace_space =
# static.trace_space, memory=static.memory ,high_threshold = static.high_threshold , low_threshold =
# static.low_threshold,divergence_algebra = static.divergence_algebra): _, result = (matrix,drivers,riders)
#
#     max_plan = []
#     max_srp=0
#     trajectory=[]
#     mt=[]
#     last_divergence_time=0
#     max_value_time = 0
#     for j in range(times):
#         if j > memory * trace_space:
#             last = trajectory[-1][1]+
#             last4 = 0
#             for i in range(-2, -memory-1, -1):
#                 last4 += trajectory[i][1]
#             last4 = last4 / (memory-1)
#
#             # b = trajectory[-1][2] - 2 * trajectory[-2][2] + trajectory[-3][2]
#             # a = trajectory[-3][2] - 2 * trajectory[-4][2] + trajectory[-5][2]
#             # tend = b - a
#             if j - last_divergence_time < divergence_algebra:
#                 f = iteratorA
#             elif last-last4<low_threshold:
#                 last_divergence_time =j
#                 f = iteratorA
#             elif last-last4<high_threshold:
#                 f = iteratorB
#             else:
#                 f = iteratorC
#         else:
#             f = iteratorB
#             # print(bi_matrix)
#         r = f(matrix, result, )
#         if get_total_value(result)>max_srp:
#             max_srp = get_total_value(result)
#             max_plan = result.copy()
#             max_value_time=j
#             mt.append([j+1,get_total_value(result),time.perf_counter()])
#             # print(max_srp/len(result))
#         if (j + 1) % trace_space == 0:
#             sum = get_total_value(result)
#             # t5 = time.perf_counter()
#             # print(t5,'迭代第%d次,fitness:'%(j+1),sum)
#             trajectory.append((j + 1, sum,time.perf_counter()))
#     df = pd.DataFrame(mt,columns=['times','cost','time'])
#     if fname is not None and name is not None:
#         df.to_csv(trajectory_path+fname+name)
#     plan=[]
#     for re in max_plan:
#         re2 = [drivers[re[0]]['id'], riders[re[1]]['id'], re[2]]
#         plan.append(re2)
#     print(max_value_time)
#     return plan,max_plan
# # b = optimize_mode_C(a,drivers,riders)
# # print(b)


def alonso_greedy_match(vm):
    plan = []
    marked = np.zeros(vm.shape[1:])
    # print('------------------------')
    # print(marked.shape)
    # np.argmax(state.marked[row] == 1)
    for i in range(vm.shape[0]):
        t_vm = vm[i].copy()
        t_vm[marked == 1] = float('inf')
        rg = np.unravel_index(t_vm.argmin(), t_vm.shape)
        # rg = np.argmax(vm[i][marked == 0])
        # print(i, rg[0], rg[1])
        plan.append([i, rg[0], rg[1], vm[i, rg[0], rg[1]]])
        marked[rg[0], :] = 1
        marked[rg[1], :] = 1
        marked[:, rg[0]] = 1
        marked[:, rg[1]] = 1
    # print(plan)
    s = 0.0
    for p in plan:
        s += p[3]
    return s, plan


def vm_3d_to_2d(vm):
    matrix = np.zeros((len(R) ** 2, len(D)))
    matrix += float('inf')
    for r1i, r1 in enumerate(R):
        for r2i, r2 in enumerate(R):
            if r1i == r2i:
                continue
            else:
                for di, d in enumerate(D):
                    tl = vm[di, r1i, r2i]
                    matrix[r1i * len(R) + r2i, di] = tl
    return matrix


def greedy_match(vm):
    plan = []

    return plan


def MSGS(matrix, ShowLog=False, curves_path=None):
    if ShowLog:
        print('当前参数:')
        print('迭代次数:', statics.times, )
        print('记忆步长:', statics.trace_space, )
        print('记忆长度:', statics.memory, )
        print('阈值阿尔法:', statics.high_threshold, )
        print('阈值贝塔:', statics.low_threshold, )
        print('发散强度:', statics.divergence_algebra, )
    # print(statics.times)

    times = statics.times
    trace_space = statics.trace_space
    memory = statics.memory
    high_threshold = statics.high_threshold
    low_threshold = statics.low_threshold
    divergence_algebra = statics.divergence_algebra
    # print(matrix.shape)
    # print(matrix)
    v, result = alonso_greedy_match(matrix)
    # print(v)
    # print(result)

    max_plan = result
    max_srp = v
    trajectory = []
    # 收敛轨迹

    mt = []
    last_divergence_time = 0

    max_value_time = v
    # 最大值代数

    # for i in range(memory * trace_space):
    #     f = iteratorA
    #     r = f(matrix, result, )
    #     if get_total_value(result) > max_srp:
    #         max_srp = get_total_value(result)
    #         max_plan = result.copy()
    #         max_value_time = i
    #         mt.append([i, get_total_value(result), time.perf_counter()])
    #         # print(max_srp/len(result))
    #     if (i) % trace_space == 0:
    #         sum = get_total_value(result)
    #         trajectory.append((i, sum, time.perf_counter()))
    # print(times)
    Tabu = {}
    for j in range(times):
        operator = 0
        if j > memory * trace_space:
            last = trajectory[-1][1]
            last4 = 0
            for i in range(-2, -memory - 1, -1):
                last4 += trajectory[i][1]
            last4 = last4 / (memory - 1)

            # b = trajectory[-1][2] - 2 * trajectory[-2][2] + trajectory[-3][2]
            # a = trajectory[-3][2] - 2 * trajectory[-4][2] + trajectory[-5][2]
            # tend = b - a
            if j - last_divergence_time < divergence_algebra:
                f = iteratorA
                operator = 1
            elif last / last4 > low_threshold:
                last_divergence_time = j
                f = iteratorA
                operator = 1
            # else:
            #     f = iteratorB

            elif last / last4 < high_threshold:
                f = iteratorB
                operator = 2
            else:
                f = iteratorC
                operator = 3
        else:
            f = iteratorB
            operator = 2
            # print(bi_matrix)
        r = f(matrix, result, Tabu)
        a = get_total_value(result)
        if a < max_srp:
            max_srp = a
            max_plan = copy.deepcopy(result)
            max_value_time = j
            Tabu = {}
        mt.append([j + 1, get_total_value(result), time.perf_counter(), operator])
        # print(max_srp/len(result))
        if (j + 1) % trace_space == 0:
            sum = get_total_value(result)
            # t5 = time.perf_counter()
            # print(t5,'迭代第%d次,fitness:'%(j+1),sum)
            trajectory.append((j + 1, sum, time.perf_counter(),))
    df = pd.DataFrame(mt, columns=['times', 'cost', 'time', 'operator'], )
    if curves_path is not None:
        df.to_csv(statics.trajectory_path + curves_path + '.csv')
    # plan = []
    # for re in max_plan:
    #     re2 = [drivers[re[0]]['id'], riders[re[1]]['id'], re[2]]
    #     plan.append(re2)
    # print(max_value_time)
    max_value = get_total_value(max_plan)
    # print(max_value)
    # print(max_srp)
    # print(max_plan)
    return max_value, max_plan


def occupy_append(l, i):
    for j in l:
        if j == i:
            return False
    l.append(i)
    return True


if __name__ == '__main__':
    D, R = mi.instance_1
    print(len(D))
    print(len(R))
    vm, pm = mi.value_matrix(D, R)

    v, m = MSGS(vm, curves_path='Simple_ins')
    print(v, m)

"""
49046.69452696007 [[0, 0, 5, 17394.89477696853], [1, 2, 3, 13398.716492015583], [2, 1, 4, 18253.08325797596]]

0.456482049840925 [[0, 2, 4, 0.054445462975660525], [1, 0, 3, 0.14510671413030382], [2, 1, 5, 0.25692987273496065]]

0.37926098927838026 [[0, 0, 4, 0.061166570731613606], [1, 3, 1, 0.15816924253357026], [2, 2, 5, 0.15992517601319636]]
"""
