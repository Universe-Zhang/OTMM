# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:04
# @Author  : Zy
# @File    : example.py
# @Software: PyCharm
import time

import util.location as ul
import numpy as np
from scipy.special import comb, perm
import match.init_matrix as mi
import statics
import pandas as pd

import matplotlib.pyplot as plt


def occupy_append(l, i):
    for j in l:
        if j == i:
            return False
    l.append(i)
    return True


def check(polution):
    for DNA in polution:
        for i in range(len(DNA)):
            for j in range(i + 1, len(DNA)):
                if (DNA[i] == DNA[j]):
                    return False
    return True


N_CITIES = 6  # DNA size
CROSS_RATE = 0.1
MUTATE_RATE = 0.02
POP_SIZE = 500
N_GENERATIONS = 50


class GA(object):
    def __init__(self, C, DNA_size, cross_rate, mutation_rate, pop_size, ):
        self.DNA_size = DNA_size
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.pop_size = pop_size
        self.C = np.array(C)
        self.pop = np.vstack([np.random.permutation(DNA_size) for _ in range(pop_size)])

    def translateDNA(self, DNA, ):  # get cities' coord in order
        line_x = np.zeros((DNA.shape[0], DNA.shape[1] // 2), dtype=np.int8)
        for i, d in enumerate(DNA):
            for j in range(len(d) // 2):
                line_x[i, j] = d[2 * j] * self.DNA_size + d[2 * j + 1]
        return line_x

    def get_fitness(self, line_x, ):
        C = self.C
        total_distance = np.empty((line_x.shape[0],), dtype=np.float64)
        for i, xs in enumerate(line_x):
            # print(np.array(list(range(len(xs)))),xs)
            total_distance[i] = C[xs, np.array(list(range(len(xs))))].sum()
            # print(total_distance[i])
            # print(np.exp(self.DNA_size * 2 / total_distance[i]))
        fitness = np.exp(1 / total_distance)
        return fitness, total_distance

    def select(self, fitness):
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True, p=fitness / fitness.sum())
        return self.pop[idx]

    def crossover(self, parent, pop):
        if np.random.rand() < self.cross_rate:
            i_ = np.random.randint(0, self.pop_size, size=1)  # select another individual from pop
            cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)  # choose crossover points
            keep_drivers = parent[~cross_points]  # find the city number
            swap_drivers = pop[i_, np.isin(pop[i_].ravel(), keep_drivers, invert=True)]
            parent[cross_points] = swap_drivers

            # father = np.array([1, 2, 5, 4, 3, 6])
            # mother = np.array([3, 4, 5, 2, 1, 6])
            # cross_points = np.random.randint(0, 2, 6).astype(np.bool)  # choose crossover points
            # keep_drivers = father[~cross_points]  # find the city number
            # swap_drivers = mother[np.isin(mother.ravel(), keep_drivers, invert=True)]
            # parent = father
            # parent[cross_points] = swap_drivers
        return parent

    def mutate(self, child):
        for point in range(self.DNA_size):
            if np.random.rand() < self.mutate_rate:
                swap_point = np.random.randint(0, self.DNA_size)
                swapA, swapB = child[point], child[swap_point]
                child[point], child[swap_point] = swapB, swapA
        return child

    def evolve(self, fitness):
        pop = self.select(fitness)
        pop_copy = pop.copy()
        for parent in pop:  # for every parent
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop


def GA_solution(matrix, R_size, curves_path=None):
    ga = GA(C=matrix, DNA_size=R_size, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)
    t1 = time.perf_counter()
    mt = []
    ttd = float('inf')
    for generation in range(N_GENERATIONS):
        lx = ga.translateDNA(ga.pop, )
        # print(ga.pop)
        fitness, total_distance = ga.get_fitness(lx)

        best_idx = np.argmax(fitness)
        if not check(ga.pop):
            print('DNA is dead')
        # print(ga.pop)
        if total_distance[best_idx] <= ttd:
            lxb = lx[best_idx].copy()
            ans = ga.pop[best_idx].copy()
            ttd = total_distance[best_idx]

        ga.evolve(fitness)
        mt.append([generation, total_distance[best_idx], time.perf_counter()])

    if curves_path is not None:
        df = pd.DataFrame(mt, columns=['times', 'cost', 'time'])
        df.to_csv(statics.trajectory_path + 'GA_' + curves_path + '.csv')
        # print('Gen:', generation, '| best fit: %.2f' % fitness[best_idx],
        #       total_distance[best_idx], total_distance.mean(), np.median(total_distance))
    # print(ans)
    # print(ttd)
    # print(lxb)
    return ttd, ans


if __name__ == '__main__':
    D, R = mi.instance_1
    print(len(D))
    print(len(R))
    vm, pm = mi.value_matrix(D, R)
    matrix = mi.vm_3d_to_2d(vm)
    N = len(R)
    print(matrix.shape)
    ttd, ans = GA_solution(matrix, N, curves_path='Simple_ins')
    print(ttd)
    print(ans)
    print(check([ans]))
    # env.plotting(lx[best_idx], ly[best_idx], total_distance[best_idx])

"""
[4 0 3 1 5 2]
37485.532943654354

0.37926098927838026
[0 4 1 3 2 5]
"""
