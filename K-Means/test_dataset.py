#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from sklearn import datasets

dbt = datasets.make_blobs()
print(type(dbt))
for item in dbt[0]:
	line = "%s\t%s\n" % (item[0], item[1])
	print(line)
	with open('coordinate.txt','a+')as f:
		f.write(line)
