# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 10:18
# @Author  : Zy
# @File    : data_demand_day.py
# @Software: PyCharm

import statics as s
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
订单量与天的关系

"""

# pd.set_option('display.max_columns', None)
# orders = pd.read_csv(s.data_path+"\\yellow_tripdata_2013-05_clean.csv", sep=',',  )
# # orders = pd.read_csv(s.data_path+"\\yellow_tripdata_2013-05.csv", sep=',',  )
# print(orders.head(20))
# orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'],format='%Y-%m-%d %H:%M:%S')
# # orders.sort_values('pickup_datetime', inplace=True)
# # print(orders.head(20))


color = ['red', 'blue', 'black', 'skyblue', 'yellow', 'gray', "DarkBlue", "DarkRed"]
# data = []
# a = orders.groupby('pickup_date').count()
# print(a)
# for index, row in a.iterrows():
#     # print(row.keys())
#     print( index,row['pickup_time'])
#     data.append(row['pickup_time'])
# print(data)

# 清洗后数据量
data = [486921, 513202, 540183, 544252, 478759, 458730, 481334, 499290, 516774, 527961, 530186, 452156, 450673, 476941,
        496588, 513193, 518051, 520576, 475288, 450346, 446886, 411344, 383280, 384324, 354260, 304581, 330141, 436986,
        471169, 500827, 516273]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# sub_axix = filter(lambda x: x % 200 == 0, x_axix)
# plt.title(tittle,fontsize=14)

# print(i,x[i],y[i])
plt.bar(np.arange(len(data)) + 1, height=np.array(data) / 1000, )
fs = 16
xlabel = 'Day'
ylabel = 'Demand (10$^3$)'
xtlabel = ["5-%d" % (i) for i in (np.arange(len(data)) + 1)]
plt.xticks(np.arange(len(data)) + 1, xtlabel, rotation=45)
plt.tick_params(labelsize=fs)
plt.xlabel(xlabel, fontsize=fs)
plt.ylabel(ylabel, fontsize=fs)
# plt.scatter(np.array(df.values.tolist())[:,0],np.array(df.values.tolist())[:,1],color='DarkBlue')
plt.show()
