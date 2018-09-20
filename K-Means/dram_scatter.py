#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-09-20 08:07
@Author: ChileWang
@Function: Draw the dynatic picture.
"""
from numpy import *
from matplotlib import pyplot as plt
import time 
def get_coor_dot():
	x_arr = []
	y_arr = []
	with open("coordinate.txt", "r+")as f:
		for line in f:
			line.strip()
			x, y = line.split('\t')
			x_arr.append(float(x.strip()))
			y_arr.append(float(y.strip()))
	return x_arr, y_arr


def get_cluster_door():
	x_arr = []
	y_arr = []
	with open("cluster_center.txt", "r+")as f:
		for line in f:
			line.strip()
			x, y = line.split('\t')
			x_arr.append(float(x.strip()))
			y_arr.append(float(y.strip()))
	return x_arr, y_arr	


def cal_dis(x1, y1, x2, y2):
	x = x1- x2
	y = y1- y2
	return x * x + y * y


def marker(x_arr, y_arr,cx_arr, cy_arr, area):# dram the marker to cluster centers
	mark = ["o","<","+","x","s","8","p","*"]
	for i in range(len(x_arr)):
		x = x_arr[i]
		y = y_arr[i]
		min_dis = 999999
		for j in range(len(cy_arr)):
			cur_dis = cal_dis(x, y, cx_arr[j], cy_arr[j])
			if cur_dis < min_dis :
				mark_index = j
				min_dis = cur_dis
		plt.scatter(x, y, s=area,facecolors='red',marker=mark[mark_index])
	plt.scatter(cx_arr, cy_arr, s=area,facecolors='green')
		
		
	
	

def main():
	x_arr, y_arr = get_coor_dot()
	cx_arr, cy_arr = get_cluster_door()
	colors = []
	area = []
	for i in range(len(x_arr)):
		colors.append(0.1)
		area.append(25)
	plt.ion()
	plt.title("K-Means")
	plt.xlabel("X",fontsize=20)
	plt.ylabel("Y",fontsize=20)
	marker(x_arr, y_arr,cx_arr, cy_arr,area)
	#plt.scatter(x_arr, y_arr, s=area,facecolors='red')
	#plt.scatter(cx_arr, cy_arr, s=area,facecolors='green')
	plt.pause(2)
	name = '/home/PythonCode/K-Means/figure/' + str(int(time.time())) + '.png'
	plt.savefig(name)
	plt.close()


if __name__ == '__main__':
	main()
