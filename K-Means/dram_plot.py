#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Created on 2018-09-20 08:07
@Author: ChileWang
@Function: Draw the dynatic picture.
"""
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

# first set up the figure,the axis,and the plot element we want to animate
fig, ax = plt.subplots()

dot, = ax.plot([], [], 'ro')

def init():
	ax.set_xlim(0, 100)
	ax.set_ylim(0, 160)
	with open("coordinate.txt",'r+')as f:
		for line in f:
			line.strip()	
			x, y = line.split('\t')	
			l = ax.plot(int(x.strip()), int(y.strip()))

	return l

def get_dot():
	with open("coordinate.txt",'r+')as f:
		for line in f:
			line.strip()	
			x, y = line.split('\t')	
			print(x+","+y)
			yield [int(x.strip()), int(y.strip())]


# animate funciton ,this is called sequentially
def animate(newdot):
	dot.set_data(newdot[0], newdot[1])
	return dot,



if __name__ == '__main__':
	am = animation.FuncAnimation(fig, animate, init_func = init, frames = get_dot, interval = 1000,blit=True)
	plt.show()
