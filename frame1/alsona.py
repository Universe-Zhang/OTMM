# -*- coding: utf-8 -*-
# @Time    : 2021/9/17 16:52
# @Author  : Zy
# @File    : alsona.py
# @Software: PyCharm

import data_deal.data_provider as dp
import datetime as dt
import networkx as nx
import matplotlib.pyplot as plt
import util.location as ul
import statics as s


def cost_function():
    pass


def find_by_attr(list, attr, value):
    for l in list:
        if l[attr] == value:
            return l
    return None


# def Con_max_waiting_rr(rlist,path,node):
#     node0 = find_by_attr(rlist,'id',path[0][id])
#     node1 = find_by_attr(rlist,'id',node[id])
#     distance = ul.distance(node0['start_node'][0], node0['start_node'][1], node1['start_node'][0], node1['start_node'][1])
#     if distance/s.avsp <=s.mwt:
#         return True
#     else:
#         return False
#
# def Con_max_delay_rr(rlist,path,node):
#     for n in path:
#         if n[0]==node['id'] and n[1]=='o' and node[1]=='d':
#             origin = n
#     node0 = find_by_attr(rlist, 'id', origin[id])
#     node1 = find_by_attr(rlist, 'id', node[id])
#     distance = ul.distance(node0['start_node'][0], node0['start_node'][1], node1['start_node'][0],
#                            node1['start_node'][1])
#     if distance / s.avsp <= s.md:
#         return True
#     else:
#         return False
#
# def routing_rr(rlist):
#     re_nodes = []
#     for r in rlist:
#         re_nodes.append([[r['id'],'o'],[r['id'],'d']])
#     path = []
#     for i in range(len(rlist)*2):
#         for r in re_nodes:
#             r[]
#             if n[1]=='o':
#                 if Con_max_waiting_rr(rlist,path,n):
#                     path.append(n)
#                 else:
#                     pass
#             else:
#                 if Con_max_delay_rr(rlist,path,n):
#                     path.append(n)
#                 else:
#                     pass

def Constraint(r1, r2):
    a = b = c = 0

    if not Con_max_waiting_rr(a, b, c):
        return False
    if not Con_max_delay_rr(a, b, c):
        return False
    return True


def Con_max_waiting_rr(a, b, c):
    distance = a + b
    if distance / s.avsp <= s.mwt:
        return True
    else:
        return False


def Con_max_delay_rr(a, b, c):
    if a / s.avsp <= s.md and c / s.avsp <= s.md:
        return True
    else:
        return False


def RV_graph(requests, vehicles):
    rvGraph = nx.Graph()
    for r in requests:
        rvGraph.add_node(r['id'], role='request', attr=r)
    for v in vehicles:
        rvGraph.add_node(v['id'], role='vehicle', attr=v)
    for r1 in requests:
        for r2 in requests:
            if r1['id'] == r2['id']:
                continue
            if Constraint(r1, r2):
                rvGraph.add_edge(r1['id'], r2['id'])
        for v in vehicles:
            if Constraint(r1, v):
                rvGraph.add_edge(r1['id'], v['id'])

    return rvGraph


def batch_assignment(requests, vehicles):
    # rvgraph = RV_graph(requests,vehicles)
    # node_colors = [
    #     '#1f78b4' if rvgraph.nodes[v]['role'] == 'request' else '#33a02c' for v in rvgraph ]
    # # plt.figure(figsize=(15, 8))
    # # karate_pos = nx.spring_layout(rvgraph, k=0.05)
    # # nx.draw_networkx(rvgraph, karate_pos, label=True, node_color=node_colors)
    # # plt.show()
    for r1 in requests:
        for r2 in requests:
            if r1 == r2:
                continue
            for v in vehicles:
                pass

    pass


def rebalance():
    pass


def travel():
    pass


def timeframeSegmentation():
    pass


# 读取数据
fleet = dp.getVehicles()
requests = dp.getRequests(start_time='2013-5-5 00:00:00', end_time='2013-5-5 00:00:30')
# 分窗
print(fleet)
print(requests)
current_time = dt.datetime.strptime('2013-05-05 00:00:00', '%Y-%m-%d %H:%M:%S')
print(current_time)
requests = requests
vehicles = fleet
# print(requests)
trips, remainRequests, remainVehicles = batch_assignment(requests, vehicles)
trips, remainRequests, remainVehicles = rebalance(trips, remainRequests, remainVehicles)
# print(trips)

travel()

# 一次匹配

# 再平衡

# 输出结果
