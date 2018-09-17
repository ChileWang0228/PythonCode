#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from collections import Counter
import matplotlib.pyplot as plt
"""
@Created on 2018-09-17 15:36
@Author:ChileWang
@Funtion:蓄水池抽样验证
"""


def sample(iterable, n):
    res = []
    for t, item in enumerate(iterable):
        if t < n:
            res.append(item)
        else:
            m = random.randint(0,t)
            if m < n:
                res[m] = item
    return res


def vertify():
    iterable = []
    samples = []
    for i in range(10):
        iterable.append(i)
    random.shuffle(iterable)
    for i in range(100000):
        res = sample(iterable,3)
        samples.extend(res)
    r = Counter(samples)
    r = dict(r)
    print(r)
    return r


def pipe_display():
    r = vertify()
    labels = []
    x = []
    for key in r:
        labels.append(key)
        x.append(r[key])
    print(labels)
    print(x)
    plt.pie(x, labels=labels, autopct='%1.2f%%')
    plt.title("Pie Chart")
    plt.show()
    plt.savefig("PieChart.png")
    print("Done!")


if __name__ == '__main__':
    pipe_display()
