import util.location as ul
import numpy as np
import time
import data_deal.data_provider as dp
import pandas as pd
import statics


def get_total_value(ll):
    sum_a = 0
    for i in ll:
        sum_a += i[3]
    return sum_a


def total_travel_distance(pes):
    paths = [
        ['a1', 'b1', 'd1', 'b2', 'f2'],
        ['a1', 'c', 'd1', 'e', 'f2', ],
        ['a1', 'c', 'b2', 'e', 'f1', ],
        ['a2', 'b2', 'd2', 'b1', 'f1'],
        ['a2', 'c', 'd2', 'e', 'f1', ],
        ['a2', 'c', 'b1', 'e', 'f2', ],
    ]
    spd = float('inf')
    spi = -1
    path_distance_list = []
    for pi, path in enumerate(paths):
        path_distance = 0
        for edge in path:
            path_distance += pes[edge]
        # if path_distance < spd:
        #     spd = path_distance
        #     spi = pi
        path_distance_list.append(path_distance)
    path_distance_list = np.array(path_distance_list)
    # print('llllllllllllllllllllllllllllllllllllll')
    # print(path_distance_list)
    spd = path_distance_list.min()
    spi = path_distance_list.argmin()
    # print(spd,spi)
    # print('llllllllllllllllllllllllllllllllllllll')
    return spd, spi


def objective(pes):
    return total_travel_distance(pes)


def value_matrix(D, R, distance='Euclidean'):
    group_edge_dict = dict()

    # v_matrix = np.zeros((len(D), len(R), len(R), 6))
    v_matrix = np.zeros((len(D), len(R), len(R)))
    v_matrix += float('inf')
    p_matrix = np.zeros(v_matrix.shape)
    p_matrix -= 1.0
    if distance == 'Euclidean':
        Distance_Metric = ul.Euclidean_distance
    elif distance == 'Manhattan':
        Distance_Metric = ul.Manhattan_distance
    elif distance == 'Spherical':
        Distance_Metric = ul.Spherical_distance
    elif distance == 'Spherical2':
        Distance_Metric = ul.Spherical_distance2
    elif distance == 'MySpherical':
        Distance_Metric = ul.My_Spherical_distance
    else:
        Distance_Metric = ul.Euclidean_distance

    for r1i, r1 in enumerate(R):
        for r2i in range(r1i + 1, len(R)):
            # for r2i, r2 in enumerate(R):
            r2 = R[r2i]
            if r1i == r2i:
                continue
            else:
                # rg['route'] = [r1['start_node'], r2['start_node'], r1['end_node'], r2['end_node'], ]
                group_edges = {}
                b1 = Distance_Metric(r1['start_node'], r1['end_node'])
                b2 = Distance_Metric(r2['start_node'], r2['end_node'])
                c = Distance_Metric(r1['start_node'], r2['start_node'])
                d1 = Distance_Metric(r1['end_node'], r2['start_node'])
                d2 = Distance_Metric(r2['end_node'], r1['start_node'])
                e = Distance_Metric(r1['end_node'], r2['end_node'])
                group_edges['b1'] = b1
                group_edges['b2'] = b2
                group_edges['c'] = c
                group_edges['d1'] = d1
                group_edges['d2'] = d2
                group_edges['e'] = e
                rg = (r1i, r2i)
                # print(group_edges)
                group_edge_dict[rg] = group_edges
    # print(group_edge_dict.keys())
    for di, d in enumerate(D):
        for rg in group_edge_dict.keys():
            r1i = rg[0]
            r2i = rg[1]
            r1 = R[r1i]
            r2 = R[r2i]
            # print(d)
            # print(r1)
            # print(r2)
            a1 = Distance_Metric(d['start_node'], r1['start_node'])
            a2 = Distance_Metric(d['start_node'], r2['start_node'])
            f1 = Distance_Metric(r1['end_node'], d['end_node'])
            f2 = Distance_Metric(r2['end_node'], d['end_node'])
            path_edges = group_edge_dict[rg].copy()
            path_edges['a1'] = a1
            path_edges['a2'] = a2
            path_edges['f1'] = f1
            path_edges['f2'] = f2

            spd, spi = objective(path_edges)
            v_matrix[di, r1i, r2i] = v_matrix[di, r2i, r1i] = spd
            p_matrix[di, r1i, r2i] = p_matrix[di, r2i, r1i] = spi
            # if r1i == 1 and r2i == 2 and di == 2:
            # print("------------------------------------------")
            # print(v_matrix[di, r1i, r2i])
            # print("------------------------------------------")
            # print(di,rg)
    return v_matrix, p_matrix
    # print(v_matrix)
    # print(p_matrix)


def vm_3d_to_2d(vm):
    R_size = vm.shape[1]
    D_size = vm.shape[0]
    matrix = np.zeros((R_size ** 2, D_size))
    matrix += float('inf')
    for r1i in range(R_size):
        for r2i in range(R_size):
            if r1i == r2i:
                continue
            else:
                for di in range(D_size):
                    tl = vm[di, r1i, r2i]
                    matrix[r1i * R_size + r2i, di] = tl
    return matrix


D = {'capacity': 4,
     'end_node': [40.729137, -73.98427499999998],
     'end_date': '2013-05-05 ',
     'start_node': [40.729137, -73.98427499999998],
     'passenger_count': 1, 'end_time': '00:08:00', 'end_datetime': '2013-05-05 00:08:00', 'id': 10964265}, {
        'capacity': 4, 'end_node': [40.779005, -73.95311499999998], 'end_date': '2013-05-05 ',
        'start_node': [40.779005, -73.95311499999998], 'passenger_count': 1, 'end_time': '00:10:00',
        'end_datetime': '2013-05-05 00:10:00', 'id': 10964266}, {'capacity': 4, 'end_node': [40.711222, -74.01643],
                                                                 'end_date': '2013-05-05 ',
                                                                 'start_node': [40.711222, -74.01643],
                                                                 'passenger_count': 1, 'end_time': '00:06:00',
                                                                 'end_datetime': '2013-05-05 00:06:00',
                                                                 'id': 10964267}, {'capacity': 4, 'end_node': [40.85706,
                                                                                                               -73.90039199999998],
                                                                                   'end_date': '2013-05-05 ',
                                                                                   'start_node': [40.85706,
                                                                                                  -73.90039199999998],
                                                                                   'passenger_count': 2,
                                                                                   'end_time': '00:09:00',
                                                                                   'end_datetime': '2013-05-05 00:09:00',
                                                                                   'id': 10964268}, {'capacity': 4,
                                                                                                     'end_node': [
                                                                                                         40.760602,
                                                                                                         -73.96736699999998],
                                                                                                     'end_date': '2013-05-05 ',
                                                                                                     'start_node': [
                                                                                                         40.760602,
                                                                                                         -73.96736699999998],
                                                                                                     'passenger_count': 3,
                                                                                                     'end_time': '00:06:00',
                                                                                                     'end_datetime': '2013-05-05 00:06:00',
                                                                                                     'id': 10964269}, {
        'capacity': 4, 'end_node': [40.777872, -73.979837], 'end_date': '2013-05-04 ',
        'start_node': [40.777872, -73.979837], 'passenger_count': 1, 'end_time': '23:35:00',
        'end_datetime': '2013-05-04 23:35:00', 'id': 10964270}, {'capacity': 4,
                                                                 'end_node': [40.758013, -73.97659299999998],
                                                                 'end_date': '2013-05-04 ',
                                                                 'start_node': [40.758013, -73.97659299999998],
                                                                 'passenger_count': 5, 'end_time': '23:40:00',
                                                                 'end_datetime': '2013-05-04 23:40:00',
                                                                 'id': 10964271}, {'capacity': 4,
                                                                                   'end_node': [40.756167, -73.966537],
                                                                                   'end_date': '2013-05-04 ',
                                                                                   'start_node': [40.756167,
                                                                                                  -73.966537],
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

instance_1 = (D, R)

if __name__ == '__main__':
    # D, R = instance_1
    # print(len(D))
    # print(len(R))
    # matrix, pm = value_matrix(D, R)
    # distance_list = ['Euclidean','Manhattan','Spherical']
    # for i in range(12, 18):
    #     for d in distance_list:
    #         print('--------------instance %d----------%s-----' % (i + 1,d))
    #         t0 = time.perf_counter()
    #         D, R = dp.get_Instance(i)
    #         t1 = time.perf_counter()
    #         vm, pm = value_matrix(D, R, distance = d)
    #         t2 = time.perf_counter()
    #         print('数据读取 %d \t %f' % (i, t1 - t0))
    #         print('instance %d \t %f' % (i, t2 - t1))
    distance_list = ['Euclidean', 'Manhattan', 'Spherical']
    for i in range(12, 18):
        # for d in distance_list:
        print('--------------instance %d---------------' % (i + 1,))
        t0 = time.perf_counter()
        D, R = dp.get_Instance(i)
        t1 = time.perf_counter()
        vm, pm = value_matrix(D, R, distance='Spherical2')
        t2 = time.perf_counter()
        print('数据读取 %d \t %f' % (i, t1 - t0))
        print('instance %d \t %f' % (i, t2 - t1))
