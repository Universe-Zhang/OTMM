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
orders = pd.read_csv(s.data_path + "\\yellow_tripdata_2013-05-6-12_order.csv", sep=',', )
# orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'])
print(orders.head(20))
orders['pickup_datetime'] = pd.to_datetime(orders['pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
orders['_day'] = orders['pickup_datetime'].dt.day
orders['_hour'] = orders['pickup_datetime'].dt.hour

# orders.sort_values('pickup_datetime', inplace=True)
print(orders.head(20))
color = ['red', 'blue', 'black', 'skyblue', 'yellow', 'gray', "DarkBlue", "DarkRed"]
data = []
a = orders.groupby(['_day', '_hour']).count()
# print(a)
ind = []
for index, row in a.iterrows():
    # print(row.keys())
    print(index, row['pickup_time'])
    data.append(row['pickup_time'])
    ind.append(index)
print(data)

# 清洗后数据量
# data = [486921, 513202, 540183, 544252, 478759, 458730, 481334, 499290, 516774, 527961, 530186, 452156, 450673, 476941, 496588, 513193, 518051, 520576, 475288, 450346, 446886, 411344, 383280, 384324, 354260, 304581, 330141, 436986, 471169, 500827, 516273]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# sub_axix = filter(lambda x: x % 200 == 0, x_axix)
# plt.title(tittle,fontsize=14)

# print(i,x[i],y[i])
# plt.bar( np.arange(len(data))+1,height=np.array(data)/1000, )
plt.plot(np.arange(len(data)) + 1, np.array(data) / 10000, color=color[0], linestyle=':', marker='o', ms=5)
fs = 16
xlabel = 'Day&Hour'
ylabel = 'Demand (10$^3$)'
xtlabel = ["5-%d" % (i) for i in (np.arange(6, 13))]
# xtlabel = ind
print(xtlabel)
plt.xticks(np.arange(0 * 24, 7 * 24, 24) + 1, xtlabel, rotation=45, )
# plt.tick_params(labelsize=8)
# plt.xticks()
plt.tick_params(labelsize=fs - 8)
plt.xlabel(xlabel, fontsize=fs)
plt.ylabel(ylabel, fontsize=fs)
# plt.scatter(np.array(df.values.tolist())[:,0],np.array(df.values.tolist())[:,1],color='DarkBlue')
plt.show()
