#!/usr/bin/python
# -*- Coding:UTF-8 -*-
"""
@Created on 2018-09-17 21:48
@Author:ChileWang
@Function:生成80个二维随机坐标数据集
"""
import random


def produce_data():
    print(1)
    with open(coordinate.txt, 'r+')as f:
        print(1)
        for i in range(80):
            print(i)
            x = random.randint(0, 100)
            y = random.randint(0, 150)
            print(x + '\t' + y + '\n')
            f.write(x + '\t' + y + '\n')


if __name__ == '__main__':
    print(1)
    #produce_data()
