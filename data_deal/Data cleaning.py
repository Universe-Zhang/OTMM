# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 9:55
# @Author  : Zy
# @File    : Data cleaning.py
# @Software: PyCharm
import statics as s
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05.csv", sep=',', )
od = pd.DataFrame(orders)
print(od.head())
print(od.count())

"""
将时间与日期分裂成单独列
"""
od['pickup_date'] = od['pickup_datetime'].str[0:11]
od['pickup_time'] = od['pickup_datetime'].str[11:]
od['dropoff_date'] = od['dropoff_datetime'].str[0:11]
od['dropoff_time'] = od['dropoff_datetime'].str[11:]

"""
数据清洗,将上下车经纬度信息错误的数据干掉
"""
od = od[(od.loc[:, 'pickup_latitude'] - 40.7143528).abs() < 20]
od = od[(od.loc[:, 'pickup_longitude'] + 74).abs() < 20]
od = od[(od.loc[:, 'dropoff_latitude'] - 40.7143528).abs() < 20]
od = od[(od.loc[:, 'dropoff_longitude'] + 74).abs() < 20]
# print(t)
print(od.count())

# od.to_csv(s.data_path+"/yellow_tripdata_2013-05_clean.csv")

# od = od[od.loc[:,'pickup_latitude'] < high_threshold & od.loc[:,'pickup_longitude'] > low_threshold]
# od = od[od.loc[:,'dropoff_longitude'] < high_threshold & od.loc[:,'pickup_longitude'] > low_threshold]
# od = od[od.loc[:,'dropoff_latitude'] < high_threshold & od.loc[:,'pickup_longitude'] > low_threshold]
