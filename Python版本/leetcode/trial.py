# -*- coding: utf-8 -*-
'''
Created on 2018年5月15日
@author: user
@attention:  Gibbs Sampling利用条件概率产生符合分布的样本，用于估计分布的期望，边缘分布；是一种在无法精确计算情况下，用计算机模拟的方法。
'''

import random
import math
import matplotlib.pyplot as plt


def xrange(x):
    return iter(range(x))


def p_ygivenx(x, m1, m2, s1, s2):
    return (random.normalvariate(m2 + rho * s2 / s1 * (x - m1), math.sqrt(1 - rho ** 2) * s2))


def p_xgiveny(y, m1, m2, s1, s2):
    return (random.normalvariate(m1 + rho * s1 / s2 * (y - m2), math.sqrt(1 - rho ** 2) * s1))


N = 5000
K = 20
x_res = []
y_res = []
m1 = 10
m2 = -5
s1 = 5
s2 = 2

rho = 0.5
y = m2

for i in xrange(N):
    for j in xrange(K):
        x = p_xgiveny(y, m1, m2, s1, s2)
        y = p_ygivenx(x, m1, m2, s1, s2)
        x_res.append(x)
        y_res.append(y)

num_bins = 50
plt.hist(x_res, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.hist(y_res, num_bins, normed=1, facecolor='red', alpha=0.5)
plt.title('Histogram')
plt.show()