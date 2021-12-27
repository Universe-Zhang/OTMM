# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 16:00
# @Author  : Zy
# @File    : distribution.py
# @Software: PyCharm


import util.location as ul

import matplotlib.pyplot as plt
import statics

import data_deal.data_provider as dp


def get_window_data(sts=None, ets=None, limit=10000):
    df = dp.get_data().head(1000)
    window = []
    for indexs in df.index:
        rowData = df.loc[indexs]
        rowData = rowData.to_dict()
        r = {'id': rowData['Unnamed: 0'],
             'start_time': rowData['pickup_datetime'],
             'start_node': [rowData['pickup_latitude'], rowData['pickup_longitude']],
             'end_time': rowData['dropoff_datetime'],
             'end_node': [rowData['dropoff_latitude'], rowData['dropoff_longitude']],
             'trip_distance': rowData['trip_distance'],
             'passenger_count': rowData['passenger_count'],
             'total_amount': rowData['total_amount'],
             # 'srp_bound': 0.8,
             }
        window.append(r)  # 逐行写入excel的sheet1
    # print(a)
    return window


import matplotlib.image as img

fig = plt.figure()
bgimg = img.imread('..\\素材\\地图3.png')
ax = fig.add_subplot(111)

# ax.imshow(bgimg,alpha=0.5,extent=[30.6552828,30.727818,104.042102,104.129591])
# pltfig(fig)
window = get_window_data()

# print(window)
# plt.xlabel('Location X',fontsize=27)
# plt.ylabel('Location Y',fontsize=27)
# plt.tick_params(labelsize=27)
# ax.tick_params(labellef="")
# ax.spines['left'].set_color('none')
# ax.spines['bottom'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# plt.axis('off')

# plt.tick_params(labelleft=False)
# plt.tick_params(labelbottom=False)
# plt.xticks([])
# plt.yticks([])
# for rider in window:
#     plt.scatter((rider['start_node'][0]-104.055)*2+104.055,(rider['start_node'][1]-30.65)*2+30.65,color='red',s=0.5)
print('draw...')
for rider in window:
    # t = ul.wgs84_to_gcj02(rider['start_node'][1],rider['start_node'][0])
    plt.scatter(rider['start_node'][0], rider['start_node'][1], color='red', s=0.5)
    # 　plt.scatter(t[1],t[0],color='red',s=0.5)
# xl = np.around(np.arange(30.6552828,30.727823,(30.727818-30.6552828)/4), decimals=2, out=None)
# yl = np.around(np.arange(104.042102,104.129595,(104.129591-104.042102)/4), decimals=2, out=None)
# print(xl)
# print(yl)
fontsize = 16
plt.xlabel('经度/度', fontsize=fontsize)
plt.ylabel('纬度/度', fontsize=fontsize)
# # ax.set_xlim(30.6552828,30.727818)
# # ax.set_ylim(104.042102,104.129591)
# plt.xticks(np.arange(0,17,4),xl)
# plt.yticks(np.arange(0,17,4),yl)
# print(static.left_bottom[0]*0.95,static.right_top[0]*1.05,static.left_bottom[1]*0.95,static.right_top[1]*1.05)
ax.imshow(bgimg, alpha=0.5, aspect='auto',
          extent=[statics.left_bottom[0] - 0.005, statics.right_top[0] + 0.005, statics.left_bottom[1] - 0.007,
                  statics.right_top[1] + 0.005])
# 	103.5998，30.32164	104.483069，31.01437
ax.set_xlim(statics.left_bottom[0], statics.right_top[0])
ax.set_ylim(statics.left_bottom[1], statics.right_top[1])
# plt.savefig("C:\\Users\\zy\\Desktop\\hurry\\distrnew.png")
import matplotlib as mpl

# mpl.rcParams['pdf.fonttype'] = 20
plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['figure.dpi'] = 300

plt.tick_params(labelsize=fontsize)
plt.savefig('..\\素材\\test.png')
plt.show()

# print(od.head())
# a = od.sample(n=1000,random_state=1)
# print(a)
# import matplotlib.pyplot as plt
#
# import matplotlib.image as img
# fig = plt.figure()
#
# bgimg = img.imread('D:\论文2\数据\\taxi_zone_map_manhattan.jpg')
# # ax = fig.add_subplot()
# for ii,i in a.iterrows():
#     plt.scatter(i['pickup_latitude'],i['pickup_longitude'],color='red',s=0.5)
#
# plt.xlabel('Longitude (degree)',fontsize = 16)
# plt.ylabel('Latitude (degree)',fontsize = 16)
# import util.location as ul
# print(s.xrange[0],s.yrange[0],s.xrange[1],s.yrange[1])
# xa = ul.gcj02_to_wgs84(s.xrange[0],s.yrange[0])
# ya = ul.gcj02_to_wgs84(s.xrange[1],s.yrange[1])
# print(xa[0],xa[1],ya[0],ya[1])
# plt.imshow(bgimg,alpha=0.5,
#           extent=[xa[0],ya[0],xa[1],ya[1]])
# # 	103.5998，30.32164	104.483069，31.01437
#
#
# plt.ylim(xa[1],ya[1])
# plt.xlim(xa[0],ya[0])
# # plt.xlabel('Longitude ($^\circ$)',fontsize = 16)
# plt.show()
