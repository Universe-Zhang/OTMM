# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 10:35
# @Author  : Zy
# @File    : data_analising.py
# @Software: PyCharm

import statics as s
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
数据关于实践方面的分析
"""

pd.set_option('display.max_columns', None)
orders = pd.read_csv(s.data_path + "\\yellow_tripdata_2013-05_clean.csv", sep=',', )
# orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'])
print(orders.head(20))
orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
# orders.sort_values('pickup_datetime', inplace=True)
# print(orders.head(20))


color = ['red', 'blue', 'black', 'skyblue', 'yellow', 'gray', "DarkBlue", "DarkRed"]
# data = []
# orders = pd.to_datetime(orders['pickup_datetime'])
# orders['dayofweek'] = orders.dt.dayofweek
# a = orders.groupby('dayofweek').count()
# print(a)
# for index, row in a.iteritems():
#     # print(row.keys())
#     print( index,row)
#     data.append(row)
# print(data)

# [6-19]
# data = [909403, 958275, 995878, 1029967, 1046012, 1050762, 927444]
# data = [1689890, 1842147, 2365312, 2427276, 2486792, 1949274, 1710784]
# data = np.array(data)
# times = [4,4,5,5,5,4,4]
# times = np.array(times)
# data = data/times
# print(data)
# 全部

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# sub_axix = filter(lambda x: x % 200 == 0, x_axix)
# plt.title(tittle,fontsize=14)

# print(i,x[i],y[i])
# plt.bar( np.arange(len(data))+1,height=np.array(data)/1000, )
# fs=16
# xlabel='Day of week'
# ylabel='Demand (10$^3$)'
# xtlabel = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# plt.xticks(np.arange(len(data))+1,xtlabel,rotation=45)
# plt.tick_params(labelsize  = fs)
# plt.xlabel(xlabel,  fontsize=fs)
# plt.ylabel(ylabel,  fontsize=fs)
# # plt.scatter(np.array(df.values.tolist())[:,0],np.array(df.values.tolist())[:,1],color='DarkBlue')
# plt.show()

"""

    Unnamed: 0 vendor_id      pickup_datetime     dropoff_datetime  \
0            0       VTS  2013-05-01 00:04:00  2013-05-01 00:12:00
1            1       VTS  2013-05-01 00:03:00  2013-05-01 00:10:00
2            2       VTS  2013-05-01 00:04:00  2013-05-01 00:10:00
3            3       VTS  2013-05-01 00:05:00  2013-05-01 00:09:00
4            4       VTS  2013-05-01 00:05:00  2013-05-01 00:14:00
5            5       VTS  2013-05-01 00:00:00  2013-05-01 00:12:00
6            6       VTS  2013-05-01 00:01:00  2013-05-01 00:10:00
7            7       VTS  2013-05-01 00:05:00  2013-05-01 00:12:00
8            8       VTS  2013-05-01 23:57:00  2013-05-02 00:08:00
9            9       VTS  2013-05-01 00:04:00  2013-05-01 00:06:00
10          10       VTS  2013-05-01 00:02:00  2013-05-01 00:07:00
11          11       VTS  2013-05-01 00:04:00  2013-05-01 00:06:00
12          12       VTS  2013-05-01 00:02:00  2013-05-01 00:09:00
13          13       VTS  2013-05-01 00:04:00  2013-05-01 00:06:00
14          14       VTS  2013-05-01 00:01:00  2013-05-01 00:06:00
15          15       VTS  2013-05-01 00:04:00  2013-05-01 00:09:00
16          16       VTS  2013-05-01 00:02:00  2013-05-01 00:13:00
17          17       VTS  2013-05-01 00:05:00  2013-05-01 00:13:00
18          18       VTS  2013-05-01 00:00:00  2013-05-01 00:08:00
19          19       VTS  2013-05-01 00:03:00  2013-05-01 00:10:00

    passenger_count  trip_distance  pickup_longitude  pickup_latitude  \
0                 1           1.34        -73.982287        40.772815
1                 5           2.60        -73.963010        40.711900
2                 2           1.31        -73.981780        40.724352
3                 1           0.82        -73.964017        40.709692
4                 1           1.65        -73.973917        40.752787
5                 5           2.41        -74.002355        40.750325
6                 1           2.44        -73.950115        40.771767
7                 1           2.42        -74.009295        40.724732
8                 1           2.98        -74.003837        40.738477
9                 1           0.76        -73.979085        40.740397
10                6           1.06        -73.985552        40.755752
11                5           0.93        -73.981722        40.741010
12                3           2.20        -73.979642        40.771287
13                5           0.47        -73.956933        40.764012
14                3           0.82        -73.981472        40.764820
15                1           1.46        -74.006282        40.733255
16                1           2.52        -74.005432        40.740837
17                1           1.44        -74.000150        40.730415
18                1           1.63        -73.985107        40.745602
19                1           1.39        -74.003107        40.734837

    rate_code store_and_fwd_flag  dropoff_longitude  dropoff_latitude  \
0           1                NaN         -73.986210         40.758742
1           1                NaN         -73.991875         40.721917
2           1                NaN         -73.973755         40.736892
3           1                NaN         -73.950895         40.710972
4           1                NaN         -73.996203         40.755867
5           1                NaN         -73.972882         40.756097
6           1                NaN         -73.977318         40.759240
7           1                NaN         -73.998672         40.754932
8           1                NaN         -73.976475         40.775472
9           1                NaN         -73.983017         40.731517
10          1                NaN         -73.984955         40.760172
11          1                NaN         -73.976537         40.751512
12          1                NaN         -73.954187         40.784452
13          1                NaN         -73.963575         40.766840
14          1                NaN         -73.975072         40.757807
15          1                NaN         -73.993063         40.748762
16          1                NaN         -73.983168         40.758027
17          1                NaN         -74.005800         40.741240
18          1                NaN         -73.967647         40.757612
19          1                NaN         -73.998130         40.722567

   payment_type  fare_amount  surcharge  mta_tax  tip_amount  tolls_amount  \
0           CSH          7.0        0.5      0.5        0.00           0.0
1           CRD          9.5        0.5      0.5        2.00           0.0
2           CRD          6.5        0.5      0.5        1.00           0.0
3           CSH          5.5        0.5      0.5        0.00           0.0
4           CRD          8.5        0.5      0.5        1.80           0.0
5           CRD         11.0        0.5      0.5        2.30           0.0
6           CRD         10.0        0.5      0.5        1.50           0.0
7           CRD          9.0        0.5      0.5        1.00           0.0
8           CRD         11.5        0.5      0.5        2.40           0.0
9           CSH          4.0        0.5      0.5        0.00           0.0
10          CSH          6.0        0.5      0.5        0.00           0.0
11          CSH          4.5        0.5      0.5        0.00           0.0
12          CSH          8.5        0.5      0.5        0.00           0.0
13          CSH          4.0        0.5      0.5        0.00           0.0
14          CSH          5.5        0.5      0.5        0.00           0.0
15          CRD          6.5        0.5      0.5        1.40           0.0
16          CRD         11.0        0.5      0.5        2.88           0.0
17          CSH          7.5        0.5      0.5        0.00           0.0
18          CSH          8.0        0.5      0.5        0.00           0.0
19          CRD          7.5        0.5      0.5        1.60           0.0

    total_amount  pickup_date pickup_time dropoff_date dropoff_time
0           8.00  2013-05-01     00:04:00  2013-05-01      00:12:00
1          12.50  2013-05-01     00:03:00  2013-05-01      00:10:00
2           8.50  2013-05-01     00:04:00  2013-05-01      00:10:00
3           6.50  2013-05-01     00:05:00  2013-05-01      00:09:00
4          11.30  2013-05-01     00:05:00  2013-05-01      00:14:00
5          14.30  2013-05-01     00:00:00  2013-05-01      00:12:00
6          12.50  2013-05-01     00:01:00  2013-05-01      00:10:00
7          11.00  2013-05-01     00:05:00  2013-05-01      00:12:00
8          14.90  2013-05-01     23:57:00  2013-05-02      00:08:00
9           5.00  2013-05-01     00:04:00  2013-05-01      00:06:00
10          7.00  2013-05-01     00:02:00  2013-05-01      00:07:00
11          5.50  2013-05-01     00:04:00  2013-05-01      00:06:00
12          9.50  2013-05-01     00:02:00  2013-05-01      00:09:00
13          5.00  2013-05-01     00:04:00  2013-05-01      00:06:00
14          6.50  2013-05-01     00:01:00  2013-05-01      00:06:00
15          8.90  2013-05-01     00:04:00  2013-05-01      00:09:00
16         14.88  2013-05-01     00:02:00  2013-05-01      00:13:00
17          8.50  2013-05-01     00:05:00  2013-05-01      00:13:00
18          9.00  2013-05-01     00:00:00  2013-05-01      00:08:00
19         10.10  2013-05-01     00:03:00  2013-05-01      00:10:00
"""
#
import re


def hour_demand(i, orders):
    orders = orders[(orders['pickup_datetime'] >= '2013-5-%d 00:00:00' % (i)) & (
                orders['pickup_datetime'] <= '2013-5-%d 23:59:59' % (i))]
    h = []
    nr = []
    for i in range(0, 24):
        c = "%d" % (i)
        d = c.zfill(2)
        odt = orders[orders['pickup_time'].str.contains(re.compile(d + ':[0-9]{2}:[0-9]{2}'))]
        h.append(i)
        nr.append(odt.size)
    print(h)
    print(nr)

    # h = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    # nr = [13367301, 9721663, 7063484, 5025431, 3672824, 3324006, 7089129, 12664444, 15334422, 15677536, 15232187, 15811787, 16522004, 16070583, 16569798, 15557108, 12637718, 15561915, 19529668, 20736064, 19871241, 19668772, 19131262, 17003578]

    xlabel = 'Hour'
    ylabel = 'Demand  (10$^4$)'
    plt.plot(h, np.array(nr) / 10000, color=color[0], linestyle=':', marker='o', ms=5)
    fs = 20
    plt.tick_params(labelsize=fs)
    plt.xlabel(xlabel, fontsize=fs)
    plt.ylabel(ylabel, fontsize=fs)
    plt.show()


for i in range(13, 20):
    hour_demand(i, orders)
