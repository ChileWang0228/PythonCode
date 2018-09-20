#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-09-17 21:48
@Author:ChileWang
@Function:生成80个二维随机坐标数据集
"""
import random


def produce_data(n):  # 生成n个二维随机坐标数据集
    with open("coordinate.txt", 'w')as f:
        for i in range(n):
            x = str(random.randint(0, 100))
            y = str(random.randint(0, 100))
            f.write(x + '\t' + y + '\n')



if __name__ == '__main__':
    produce_data(50)
