import statics as s
import pandas as pd
import numpy as np

"""
截取5号至11号数据
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
# dataRange=[]
# for i in range(5,12):
#     dataRange.append(("-%d"%(i)).zfill(3))
# print(dataRange)
# order_names = ['VendorID', 'tpep_pickup_datetime',
#                'tpep_dropoff_datetime', 'Passenger_count',
#                'Trip_distance','PULocationID', 'DOLocationID'
#                'RateCodeID','Store_and_fwd_flag', 'Payment_type'
#                'Fare_amount','Extra', 'MTA_tax'
#                'Improvement_surcharge','Tip_amount', 'Tolls_amount', 'Total_amount'
#                ]
orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05_clean.csv", sep=',', )
od = pd.DataFrame(orders)
print(od.head())
od = od[(od['pickup_datetime'].str[8:10].astype(int) >= 6) & (od['pickup_datetime'].str[8:10].astype(int) < 13)]
# od = od[ (od['dropoff_datetime'].str[8:10].astype(int)>=6 )&(od['dropoff_datetime'].str[8:10].astype(int)<13 ) ]
od.to_csv(s.data_path + "/yellow_tripdata_2013-05-6-12_clean.csv")

# pd.set_option('display.max_columns', None)
# orders = pd.read_csv(s.data_path + "/yellow_tripdata_2013-05_clean.csv", sep=',', )
# orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'])
# orders = orders[(orders['pickup_datetime'] >'2013-5-4 23:00:00') & (orders['pickup_datetime'] < '2013-5-5 00:00:00')]
# orders.to_csv(s.data_path+"/yellow_tripdata_2013-05_vehicles.csv")
