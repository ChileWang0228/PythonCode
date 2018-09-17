#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Created on 2018-09-17 22:42
@Author:ChileWang
@Function:reducer.py
"""
import sys


def main():  # 统计词频
    current_word = None
    current_x = 0
    current_y = 0
    word = None
    line_num = 1  # 统计行数
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        try:
            x, y = count.split(',', 1)
            x = int(x)
            y = int(y)
        except ValueError:
            continue

        if current_word == word:
            line_num += 1
            current_x += x
            current_y += y
        else:
            if current_word:  # 输出新的聚类中心
                # 计算平均值
                avg_x = current_x / line_num
                avg_y = current_t / line_num
                line_num = 1  # 清零，重新计行数
                print("%s\t%s" % (avg_x, avg_y))
            current_x = x
            current_y = y
            current_word = word

    if current_word == word:  # 输出最后一个聚类中心
        avg_x = current_x / line_num
        avg_y = current_t / line_num
        print("%s\t%s" % (avg_x, avg_y))


if __name__ == '__main__':
    main()
