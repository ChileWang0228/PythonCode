#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-09-19 21:43
@Author:ChileWang
@Function: Calculate the delta and write it into delta.txt
"""
def cal_delta():
	delta = 0
	x1_arr = []
	x2_arr = []
	y1_arr = []
	y2_arr = []
	with open("cluster_center.txt", "r+")as f:
		for line in f:
			line.strip()
			x, y = line.split('\t')
			x1_arr.append(float(x))
			y1_arr.append(float(y))
	with open("init_cluster_centers-output/part-00000","r+")as f:
		for line in f:
			line.strip()
			x, y = line.split('\t')
			x2_arr.append(float(x))
			y2_arr.append(float(y))
	for i in range(len(y1_arr)):
		x = x1_arr[i] - x2_arr[i]
		y = y1_arr[i] - y2_arr[i]
		delta += x * x + y * y
	delta = delta / len(y1_arr)
	if float(delta) < 0.01 :
		with open("delta.txt","w")as f:
			f.write("done")
	else:
		with open("delta.txt","w")as f:
			f.write(str(delta))
		with open("cluster_center.txt","w")as f:
			with open("init_cluster_centers-output/part-00000","r+")as f1:
				for line in f1:
					f.write(line)

if __name__ == '__main__':
	print("----------Begin Calculate the delta-----------")
	cal_delta()
