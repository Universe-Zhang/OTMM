# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 16:55
# @Author  : Zy
# @File    : data_provider.py
# @Software: PyCharm
import statics as s
import pandas as pd
import datetime as dt
import numpy as np
from pandas import datetime
from sklearn import model_selection


def get_data(start_time='2013-5-5 00:02:00', end_time='2013-5-5 00:10:00', request_limit=100, ):
    pd.set_option('display.max_columns', None)
    orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05-5-11_order.csv", sep=',', )
    orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'])
    orders = orders[(orders['pickup_datetime'] > start_time) & (orders['pickup_datetime'] < end_time)]
    return orders.head(request_limit)


def getVehicles(number=1000):
    pd.set_option('display.max_columns', None)
    orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05_vehicles.csv", sep=',', )
    orders = orders.tail(number)
    fleet = []
    for indexs in orders.index:
        rowData = orders.loc[indexs]
        rowData = rowData.to_dict()
        r = {'id': rowData['Unnamed: 0'],
             'end_datetime': rowData['dropoff_datetime'],
             'end_date': rowData['dropoff_date'],
             'end_time': rowData['dropoff_time'],
             'location': [rowData['dropoff_latitude'], rowData['dropoff_longitude']],
             'aim node': [rowData['dropoff_latitude'], rowData['dropoff_longitude']],
             'passenger_count': rowData['passenger_count'],
             'capacity': s.vc
             }
        fleet.append(r)  # 逐行写入excel的sheet1
    return fleet


def getVehicles2(number=1000):
    pd.set_option('display.max_columns', None)
    orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05_vehicles.csv", sep=',', )
    orders = orders.tail(number)
    fleet = []
    for indexs in orders.index:
        rowData = orders.loc[indexs]
        rowData = rowData.to_dict()
        r = {'id': rowData['Unnamed: 0'],
             'end_datetime': rowData['dropoff_datetime'],
             'end_date': rowData['dropoff_date'],
             'end_time': rowData['dropoff_time'],
             'location': [rowData['dropoff_latitude'], rowData['dropoff_longitude']],
             'aim node': [rowData['dropoff_latitude'], rowData['dropoff_longitude']],
             'passenger_count': rowData['passenger_count'],
             'capacity': s.vc
             }
        fleet.append(r)  # 逐行写入excel的sheet1
    return fleet


def getRequests(start_time='2013-5-8 12:02:00', end_time='2013-5-8 13:10:00', request_limit=10000000, ):
    pd.set_option('display.max_columns', None)
    orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05-6-12_order.csv", sep=',', low_memory=False)
    orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'])
    orders = orders[(orders['pickup_datetime'] > start_time) & (orders['pickup_datetime'] < end_time)]
    orders = orders.head(request_limit)
    # orders = orders.head(request_limit)
    # print('-------------------')
    # #print(orders.size)
    # print(len(orders))
    # print('-------------------')
    # print(orders.count)
    requests = []
    for indexs in orders.index:
        rowData = orders.loc[indexs]
        # 　ｓprint(rowData,indexs)
        rowData = rowData.to_dict()
        r = {'id': rowData['Unnamed: 0'],
             'start_datetime': rowData['pickup_datetime'],
             'acceptable_time': rowData['pickup_datetime'] + dt.timedelta(seconds=s.mwt),
             'start_date': rowData['pickup_date'],
             'start_time': rowData['pickup_time'],
             'start_node': [rowData['pickup_latitude'], rowData['pickup_longitude']],
             'end_datetime': rowData['dropoff_datetime'],
             'end_date': rowData['dropoff_date'],
             'end_time': rowData['dropoff_time'],
             'end_node': [rowData['dropoff_latitude'], rowData['dropoff_longitude']],
             'trip_distance': rowData['trip_distance'],
             'passenger_count': rowData['passenger_count'],
             'total_amount': rowData['total_amount'],
             # 'srp_bound': 0.8,
             }
        requests.append(r)  # 逐行写入excel的sheet1
    # print(len(requests))
    return requests


root = '2013-05-'
data1 = 6
data2 = 10
data3 = 12

time1 = 0
time2 = 5
time3 = 12
time4 = 19

tail = ':00:00'
tail2 = ':05:00'

Instance_list = []
params = []

# instance 1
param = dict()
param['start_time'] = root + '%02d ' % (data1) + '%02d' % (time1) + tail
param['end_time'] = root + '%02d ' % (data1) + '%02d' % (time1) + tail2
params.append(param)
# instance 2
param = dict()
param['start_time'] = root + '%02d ' % (data1) + '%02d' % (time2) + tail
param['end_time'] = root + '%02d ' % (data1) + '%02d' % (time2) + tail2
params.append(param)
# instance 3
param = dict()
param['start_time'] = root + '%02d ' % (data1) + '%02d' % (time3) + tail
param['end_time'] = root + '%02d ' % (data1) + '%02d' % (time3) + tail2
params.append(param)
# instance 4
param = dict()
param['start_time'] = root + '%02d ' % (data1) + '%02d' % (time4) + tail
param['end_time'] = root + '%02d ' % (data1) + '%02d' % (time4) + tail2
params.append(param)

# instance 5
param = dict()
param['start_time'] = root + '%02d ' % (data2) + '%02d' % (time1) + tail
param['end_time'] = root + '%02d ' % (data2) + '%02d' % (time1) + tail2
params.append(param)
# instance 6
param = dict()
param['start_time'] = root + '%02d ' % (data2) + '%02d' % (time2) + tail
param['end_time'] = root + '%02d ' % (data2) + '%02d' % (time2) + tail2
params.append(param)
# instance 7
param = dict()
param['start_time'] = root + '%02d ' % (data2) + '%02d' % (time3) + tail
param['end_time'] = root + '%02d ' % (data2) + '%02d' % (time3) + tail2
params.append(param)
# instance 8
param = dict()
param['start_time'] = root + '%02d ' % (data2) + '%02d' % (time4) + tail
param['end_time'] = root + '%02d ' % (data2) + '%02d' % (time4) + tail2
params.append(param)

# instance 9
param = dict()
param['start_time'] = root + '%02d ' % (data3) + '%02d' % (time1) + tail
param['end_time'] = root + '%02d ' % (data3) + '%02d' % (time1) + tail2
params.append(param)
# instance 10
param = dict()
param['start_time'] = root + '%02d ' % (data3) + '%02d' % (time2) + tail
param['end_time'] = root + '%02d ' % (data3) + '%02d' % (time2) + tail2
params.append(param)
# instance 11
param = dict()
param['start_time'] = root + '%02d ' % (data3) + '%02d' % (time3) + tail
param['end_time'] = root + '%02d ' % (data3) + '%02d' % (time3) + tail2
params.append(param)
# instance 12
param = dict()
param['start_time'] = root + '%02d ' % (data3) + '%02d' % (time4) + tail
param['end_time'] = root + '%02d ' % (data3) + '%02d' % (time4) + tail2
params.append(param)

# instance 13
param = dict()
param['request_limit'] = 10
params.append(param)

# instance 14
param = dict()
param['request_limit'] = 50
params.append(param)

# instance 15
param = dict()
param['request_limit'] = 100
params.append(param)

# instance 16
param = dict()
param['request_limit'] = 200
params.append(param)

# instance 18
param = dict()
param['request_limit'] = 500
params.append(param)

# instance 18
param = dict()
param['request_limit'] = 1000
params.append(param)


def get_Instance(ind):
    rparam = params[ind]
    # print(rparam)
    if ind < 12:
        P = getRequests(start_time=rparam['start_time'], end_time=rparam['end_time'])
        # print(len(P))
        P_tail = len(P) % 3
        for i in range(P_tail):
            P.pop()

        # print(len(P))
        P = np.array(P)
        np.random.seed(2)
        np.random.shuffle(P)
        D, R = P[:P.shape[0] // 3], P[P.shape[0] // 3:]

    else:
        P = getRequests(request_limit=rparam['request_limit'] * 3 // 2)
        # P_tail = len(P) % 3
        # for i in range(P_tail):
        #     P.pop()
        P = np.array(P)
        np.random.seed(2)
        np.random.shuffle(P)
        D, R = P[:P.shape[0] // 3], P[P.shape[0] // 3:]

    return D, R


import time
import match.init_matrix as mi
import pickle


def matrix_generation(i, distance='Euclidean'):
    print('--------------instance %d----------------' % (i + 1))
    t1 = time.perf_counter()
    print('t1:', t1)
    D, R = get_Instance(i)
    print(len(D))
    print(len(R))

    t2 = time.perf_counter()
    print('t2:', t2)
    vm, pm = mi.value_matrix(D, R, distance=distance)
    t3 = time.perf_counter()
    print('t3:', t3)
    print(t2 - t1, t3 - t2)
    # print(t3-t1)
    with open("..\\data\\instance_%d_%s.pk" % (i, distance), "wb") as file:
        pickle.dump((vm, pm), file, )
    print('--------------instance %d end----------------' % (i + 1))


def get_Instance_cache(ind, distance='Euclidean'):
    with open("..\\data\\instance_%d_%s.pk" % (ind, distance), "rb") as file:
        vm, pm = pickle.load(file, )
    return vm, pm


if __name__ == '__main__':
    # for dis in []:
    # distance_list = ['Euclidean', 'Manhattan', 'Spherical']
    # for i in range(12, 18):
    #     for d in distance_list:
    #         print('--------------instance %d----------%s-----' % (i + 1, d))
    #         # t0 = time.perf_counter()
    #         matrix_generation(i ,distance=d)
    #  print('instance %d \t )
    matrix_generation(17, distance='MySpherical')
