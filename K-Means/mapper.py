#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Created on 2018-09-17 22:42
@Author:ChileWang
@Function:mapper.py
"""
import sys
sep = '\t'


def cal_dis(x1, y1, x2, y2):  # 计算距离的平方,前者坐标为初始聚类坐标
    x = x1 - x2
    y = y1 - y2
    return x * x + y * y


def main():
    # 初始聚类中心二维坐标
    x_arr = []
    y_arr = []
    flag = 1
    min_dis = 99999999  # 最小距离平方和
    for line in sys.stdin:
        try:
            if line != 'End' and flag:  # 读取初始聚类中心坐标
                x, y = line.strip().split(sep)
                x_arr.append(x)
                y_arr.append(y)
            else:  # 读取初始聚类中心坐标结束，开始输出聚类中心ID和当前类别
                flag = 0
                continue  # 此时line == End 跳过此行
            if flag == 0:  # 读取初始聚类中心坐标结束，开始输出聚类中心ID和当前类别id
                x2, y2 = line.strip().split(sep)
                cluster_id = x_arr[0] + '\t' + y_arr[0]  # 聚类中心ID
                for i in range(len(x_arr)):
                    cur_dis = cal_dis(int(x_arr[i]), int(y_arr[i]), int(x2), int(y2))
                    if cur_dis < min_dis:  # 小于当前最小距离则替换
                        cluster_id = x_arr[i] + ',' + y_arr[i]
                        min_dis = cur_dis
                cur_id = x2 + ',' + y2
                print('%s\t%s' % (cluster_id, cur_id))  # 输出聚类中心ID和当前类别id
        except Exception as err:
            del err
            continue


if __name__ == '__main__':
    main()
