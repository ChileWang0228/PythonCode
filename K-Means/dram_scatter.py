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
			x_arr.append(int(x.strip()))
			y_arr.append(int(y.strip()))
	return x_arr, y_arr
def get_cluster_door():
	x_arr = []
	y_arr = []
	with open("cluster_center.txt", "r+")as f:
		for line in f:
			line.strip()
			x, y = line.split('\t')
			x_arr.append(int(x.strip()))
			y_arr.append(int(y.strip()))
	return x_arr, y_arr	

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
	plt.scatter(x_arr, y_arr, s=area,facecolors='red')
	plt.scatter(cx_arr, cy_arr, s=area,facecolors='green')
	plt.pause(2)
	name = '/home/PythonCode/K-Means/figure/' + str(int(time.time())) + '.png'
	plt.savefig(name)
	plt.close()


if __name__ == '__main__':
	main()
