# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 21:39
# @Author  : Zy
# @File    : statics.py
# @Software: PyCharm


"""
13,587车辆

"""

data_path = "..\\data"

yrange = [-74.054812, -73.883212]

xrange = [40.685928, 40.8795422]

mwt = 600
# the maximum waiting time  /s

vc = 4
# the vehicle capacity

md = 180
# the maximum delay by a request

avsp = 4.4402
"the average speed  m/s   该速度由数据随机取样1000个算取平均速度求出"

left_bottom = [40.682801, -74.054812];  # 设置区域左下角坐标（百度坐标系）
right_top = [40.8795422, -73.883212];  # 设置区域右上角坐标（百度坐标系）

times = 100000
trace_space = 10
memory = 20
high_threshold = 0.6

low_threshold = 0.9

divergence_algebra = 50
trajectory_path = '..\\result\\'
