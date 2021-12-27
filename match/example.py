# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:04
# @Author  : Zy
# @File    : example.py
# @Software: PyCharm

import util.location as ul
import numpy as np
from scipy.special import comb, perm


def occupy_append(l, i):
    for j in l:
        if j == i:
            return False
    l.append(i)
    return True


D = {'capacity': 4,
     'aim node': [40.729137, -73.98427499999998],
     'end_date': '2013-05-05 ',
     'location': [40.729137, -73.98427499999998],
     'passenger_count': 1, 'end_time': '00:08:00', 'end_datetime': '2013-05-05 00:08:00', 'id': 10964265}, {
        'capacity': 4, 'aim node': [40.779005, -73.95311499999998], 'end_date': '2013-05-05 ',
        'location': [40.779005, -73.95311499999998], 'passenger_count': 1, 'end_time': '00:10:00',
        'end_datetime': '2013-05-05 00:10:00', 'id': 10964266}, {'capacity': 4, 'aim node': [40.711222, -74.01643],
                                                                 'end_date': '2013-05-05 ',
                                                                 'location': [40.711222, -74.01643],
                                                                 'passenger_count': 1, 'end_time': '00:06:00',
                                                                 'end_datetime': '2013-05-05 00:06:00',
                                                                 'id': 10964267}, {'capacity': 4, 'aim node': [40.85706,
                                                                                                               -73.90039199999998],
                                                                                   'end_date': '2013-05-05 ',
                                                                                   'location': [40.85706,
                                                                                                -73.90039199999998],
                                                                                   'passenger_count': 2,
                                                                                   'end_time': '00:09:00',
                                                                                   'end_datetime': '2013-05-05 00:09:00',
                                                                                   'id': 10964268}, {'capacity': 4,
                                                                                                     'aim node': [
                                                                                                         40.760602,
                                                                                                         -73.96736699999998],
                                                                                                     'end_date': '2013-05-05 ',
                                                                                                     'location': [
                                                                                                         40.760602,
                                                                                                         -73.96736699999998],
                                                                                                     'passenger_count': 3,
                                                                                                     'end_time': '00:06:00',
                                                                                                     'end_datetime': '2013-05-05 00:06:00',
                                                                                                     'id': 10964269}, {
        'capacity': 4, 'aim node': [40.777872, -73.979837], 'end_date': '2013-05-04 ',
        'location': [40.777872, -73.979837], 'passenger_count': 1, 'end_time': '23:35:00',
        'end_datetime': '2013-05-04 23:35:00', 'id': 10964270}, {'capacity': 4,
                                                                 'aim node': [40.758013, -73.97659299999998],
                                                                 'end_date': '2013-05-04 ',
                                                                 'location': [40.758013, -73.97659299999998],
                                                                 'passenger_count': 5, 'end_time': '23:40:00',
                                                                 'end_datetime': '2013-05-04 23:40:00',
                                                                 'id': 10964271}, {'capacity': 4,
                                                                                   'aim node': [40.756167, -73.966537],
                                                                                   'end_date': '2013-05-04 ',
                                                                                   'location': [40.756167, -73.966537],
                                                                                   'passenger_count': 1,
                                                                                   'end_time': '23:37:00',
                                                                                   'end_datetime': '2013-05-04 23:37:00',
                                                                                   'id': 10964272}
R = {'start_node': [40.756968, -73.98620599999998], 'passenger_count': 1,
     'end_node': [40.728483000000004, -73.98472199999998],
     'start_date': '2013-05-05 ',
     'end_date': '2013-05-05 ',
     'end_time': '00:15:21',
     'start_datetime': ('2013-05-05 00:00:29'),
     'acceptable_time': ('2013-05-05 00:10:29'),
     'total_amount': 13.5,
     'start_time': '00:00:29',
     'id': 1862979,
     'end_datetime': '2013-05-05 00:15:21',
     'trip_distance': 2.8}, {'start_node': [40.743549, -74.00724099999998], 'passenger_count': 1,
                             'end_node': [40.771279, -73.95044199999998], 'start_date': '2013-05-05 ',
                             'end_date': '2013-05-05 ', 'end_time': '00:17:28',
                             'start_datetime': ('2013-05-05 00:00:29'), 'acceptable_time': ('2013-05-05 00:10:29'),
                             'total_amount': 18.0, 'start_time': '00:00:29', 'id': 1880280,
                             'end_datetime': '2013-05-05 00:17:28', 'trip_distance': 5.0}, {
        'start_node': [40.744863, -73.98054499999998], 'passenger_count': 1, 'end_node': [40.73485, -73.98818199999998],
        'start_date': '2013-05-05 ', 'end_date': '2013-05-05 ', 'end_time': '00:05:17',
        'start_datetime': ('2013-05-05 00:00:29'), 'acceptable_time': ('2013-05-05 00:10:29'), 'total_amount': 9.5,
        'start_time': '00:00:29', 'id': 1733408, 'end_datetime': '2013-05-05 00:05:17', 'trip_distance': 0.8}, {
        'start_node': [40.732956, -73.998059], 'passenger_count': 1, 'end_node': [40.781085, -73.958409],
        'start_date': '2013-05-05 ', 'end_date': '2013-05-05 ', 'end_time': '00:18:23',
        'start_datetime': ('2013-05-05 00:00:29'), 'acceptable_time': ('2013-05-05 00:10:29'), 'total_amount': 18.0,
        'start_time': '00:00:29', 'id': 1859656, 'end_datetime': '2013-05-05 00:18:23', 'trip_distance': 4.4}, {
        'start_node': [40.748952, -73.987521], 'passenger_count': 2, 'end_node': [40.735368, -73.978541],
        'start_date': '2013-05-05 ', 'end_date': '2013-05-05 ', 'end_time': '00:10:06',
        'start_datetime': ('2013-05-05 00:00:29'), 'acceptable_time': ('2013-05-05 00:10:29'), 'total_amount': 10.08,
        'start_time': '00:00:29', 'id': 1725050, 'end_datetime': '2013-05-05 00:10:06', 'trip_distance': 1.6}, {
        'start_node': [40.688319, -73.99917499999998], 'passenger_count': 4, 'end_node': [40.719437, -73.960634],
        'start_date': '2013-05-05 ', 'end_date': '2013-05-05 ', 'end_time': '00:19:07',
        'start_datetime': ('2013-05-05 00:00:29'), 'acceptable_time': ('2013-05-05 00:10:29'), 'total_amount': 19.5,
        'start_time': '00:00:29', 'id': 1881365, 'end_datetime': '2013-05-05 00:19:07', 'trip_distance': 4.8}
D = D[0:3]
print(len(D))
print(len(R))
RGs = []
matrix = np.zeros((len(R) ** 2, len(D)))
matrix += float('inf')
for r1i, r1 in enumerate(R):
    for r2i, r2 in enumerate(R):
        if r1i == r2i:
            continue
        else:
            rg = {}
            rg['riders'] = [r1['id'], r2['id']]
            rg['route'] = [r1['start_node'], r2['start_node'], r1['end_node'], r2['end_node'], ]
            tl = 0
            for i in range(len(rg) - 1):
                tl += ul.distance(rg['route'][i][0], rg['route'][i][1], rg['route'][i + 1][0], rg['route'][i + 1][1])
            rg['tl'] = tl
            RGs.append(rg)
            for di, d in enumerate(D):
                tl = rg['tl'] + \
                     ul.distance(d['location'][0], d['location'][1], rg['route'][0][0], rg['route'][0][1]) + \
                     ul.distance(rg['route'][-1][0], rg['route'][-1][1], d['aim node'][0], d['aim node'][1])
                matrix[r1i * len(R) + r2i, di] = tl
print(matrix)
# print(RGs)
# print(matrix.shape)
# answer = []
# occupy = []
# N = len(R)
# sum = float('inf')
# for i1 in range(matrix.shape[1]):
#     rowid1 = i1 // N
#     if occupy_append(rowid1):
#         pass
#     else:
#         continue
#     for j1 in range(matrix.shape[0]):
#         a1 = [i1,j1]
#
#         colid1 = i1%N
#         if occupy_append(colid1):
#             pass
#         else:
#             continue
#         for i2 in range(matrix.shape[1]):
#             for j2 in range(matrix.shape[0]):
#                 a2 = [i2,j2]
#                 rowid2 = i2//N
#                 colid2 = i2%N
#                 if i1 ==i2 or j2 == j1 or rowid1 == rowid2 or colid1 == colid2 or rowid1 == colid2 or colid1 == rowid2:
#                     continue
#                 else:
#                     for i3 in range(matrix.shape[1]):
#                         for j3 in range(matrix.shape[0]):
#                             a3 = [i3, j3]
#                             rowid3 = i3 // N
#                             colid3 = i3 % N
#                             if i1 == i2 or j2 == j1 or rowid1 == rowid2 or colid1 == colid2 or rowid1 == colid2 or colid1 == rowid2:
#                                 continue
#
#
#
#         pass

import match.KM_prototype as KM

cost = matrix
from match.KM_2e import linear_sum_assignment

# from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost)
print(row_ind, col_ind)
c = cost[row_ind, col_ind].sum()
print(c)
