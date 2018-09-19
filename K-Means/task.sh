#!/usr/bin/env bash

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
		cal_delta
		cat delta.txt | while read line
		do 
			delta=$line # get delta
			echo "delta = "$delta
			break
		done
		if [ "$JOB_Done" = "$delta" ];then
			break
		fi
	done
	echo "-----------mr_job is ended----------"
	echo "-----------end_job begin----------"
	end_job()
	echo "-----------Mission Completed!----------"
}


main

