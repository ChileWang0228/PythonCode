#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Created on 2018-09-17 22:08
@Author:ChileWang
@Function:蓄水池抽样生出8个初始聚类中心
"""
import random
from collections import Counter
import matplotlib.pyplot as plt


def sample(n):  # 蓄水池抽样抽出n个聚类中心坐标
    with open('coordinate.txt', 'r+')as f:
        t = 0
        # 聚类中心坐标
        x_arr = []
        y_arr = []
        for line in f:
            line = line.rstrip()
            x, y = line.split('\t')
            if t < n:
                x_arr.append(x)
                y_arr.append(y)
                t += 1
            else:
                m = random.randint(0, t)
                if m < n:
                    x_arr[m] = x
                    y_arr[m] = y
        content = f.read()
    with open('cluster_center.txt', 'w+')as f:  # 将聚类中心坐标写入文件
        for i in range(n):
            x = x_arr[i]
            y = y_arr[i]
            f.write(x + '\t' + y + '\n')
        f.write('End\n')  # 插入标志，方便mapper函数辨认
        with open('coordinate.txt', 'r+')as f1:
            for line in f1:
                f.write(line)
    return x_arr, y_arr


def ver_truth():  # 验证蓄水池抽样定理
    samples = []
    for i in range(5000000):
        x_arr, y_arr = sample(3)
        res = zip(x_arr, y_arr)
        samples.extend(res)
    r = Counter(samples)
    r = dict(r)
    print(r)
    return r


def pipe_display():
    r = ver_truth()
    labels = []
    x = []
    for key in r:
        labels.append(key)
        x.append(r[key])
    plt.pie(x, labels=labels, autopct='%1.2f%%')
    plt.title("Pie Chart")
    plt.show()
    plt.savefig("PieChart.png")
    print("Done!")


if __name__ == '__main__':
    sample(8)
    #  pipe_display()
