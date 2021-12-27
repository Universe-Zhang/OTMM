# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 21:07
# @Author  : Zy
# @File    : data_order.py
# @Software: PyCharm

import statics as s
import pandas as pd
import numpy as np

"""
为5号至11号数据排序
"""

# def get_data():
#     # order_names = ['id', 'start_time', 'end_time', 'start_x', 'start_y','end_x', 'end_y']
#     # orders = pd.read_table('D:\机器学习\order_20161101', sep=',', header=None, names=order_names)
#     orders = pd.read_csv(s.data_path+"/yellow_tripdata_2013-05.csv", sep=',', header=1, )
#     od = pd.DataFrame(orders)
#     # orders['dr']=orders['id'].apply(lambda x:np.random.randint(2))
#     # orders = orders.reset_index()
#     # orders.to_csv('D:/data/test2.csv')
#     return orders
# print(get_data().head())
pd.set_option('display.max_columns', None)
"""
tpep_pickup_datetime The date and time when the meter was engaged.
tpep_dropoff_datetime The date and time when the meter was disengaged.
2013-05-01 00:04:00
2013-05-01 00:10:00
"""

# order_names = ['VendorID', 'tpep_pickup_datetime',
#                'tpep_dropoff_datetime', 'Passenger_count',
#                'Trip_distance','PULocationID', 'DOLocationID'
#                'RateCodeID','Store_and_fwd_flag', 'Payment_type'
#                'Fare_amount','Extra', 'MTA_tax'
#                'Improvement_surcharge','Tip_amount', 'Tolls_amount', 'Total_amount'
#                ]
orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05-6-12_clean.csv", sep=',', )
od = pd.DataFrame(orders)
# od['pickup_datetime'] = pd.to_datetime(od['pickup_datetime'],format='%Y-%m-%d %H:%M:%S')

od['pickup_datetime'] = pd.to_datetime(od['pickup_datetime'], format='%Y-%m-%d %H:%M:%S')

od.sort_values('pickup_datetime', inplace=True)

print(od.tail(50))

od.to_csv(s.data_path + "/yellow_tripdata_2013-05-6-12_order.csv")
