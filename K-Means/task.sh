#!/bin/bash

function init_job(){
	cd /home/PythonCode/K-Means
	# produce 80 coordinate data
	python random_data_produce.py
	# produce 8 init cluster centerns
	python reservoir_sample.py
}


function cal_delta(){
	cd /home/PythonCode/K-Means
	# Calculate the delta
	python cal_delta.py
}


function mr_job(){
	# DELETE THE OUTPUT DIR init_cluster_centers-output
	hadoop fs -rm -r init_cluster_centers-output
	# DELETE THE OUTPUT DIR coordinate
	hadoop fs -rm -r coordinate
	# create the INPUT DIR
	hadoop fs -mkdir -p coordinate
	# put the  coordinate file to HDFS
	hadoop fs -put /home/PythonCode/K-Means/coordinate.txt coordinate

	# run MapReduce job
	cd /usr/local/hadoop/hadoop-3.0.3
	bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.0.3.jar \
	-file /home/PythonCode/K-Means/cluster_center.txt \
	-file /home/PythonCode/K-Means/mapper.py    -mapper /home/PythonCode/K-Means/mapper.py \
	-file /home/PythonCode/K-Means/reducer.py   -reducer /home/PythonCode/K-Means/reducer.py \
	-input coordinate/*  -output init_cluster_centers-output
	#-D stream.non.zero.exit.is.failure=false \


}

function end_job(){
	# get MapReduce output and Change its name
	mkdir -p /home/map_reduce_result
	cd /home/map_reduce_result
	hadoop fs -get init_cluster_centers-output
	cur_date="`date +%Y%m%d_%H:%M:%S`" 
	mv init_cluster_centers-output $cur_date
	cd /home/PythonCode/K-Means
	python dram_scatter.py
}


function main(){
	# set the delta
	JOB_Done="done"
	echo "-------init_job is beginning--------"
	init_job
	echo "-------init_job is ended------------"
	echo "-------mr_job is beginning----------"
	while : # do mr_job until delta < 1
	do
		mr_job
		# get the new cluster centers dir
		cd /home/PythonCode/K-Means
		hadoop fs -get init_cluster_centers-output
		cd /home/PythonCode/K-Means/draw_pic_coordinate
		mkdir -p 1
		cd /home/PythonCode/K-Means/draw_pic_coordinate/1
		hadoop fs -get init_cluster_centers-output
		cd /home/PythonCode/K-Means/draw_pic_coordinate
		cur_date="`date +%Y%m%d_%H:%M:%S`" 
		mv 1 $cur_date
		

		# calculate the delta and show the cluster centers
		cal_delta
		delta=$(cat delta.txt)
		cd /home/PythonCode/K-Means
		python dram_scatter.py
		echo "delta.txt = ${delta}"
		if [ "$JOB_Done" = "$delta" ];then
			break
		fi
		cd /home/PythonCode/K-Means
		rm -r init_cluster_centers-output
	done
	echo "-----------mr_job is ended----------"
	echo "-----------end_job begin----------"
	end_job
	echo "-----------Mission Completed!----------"
}


main

