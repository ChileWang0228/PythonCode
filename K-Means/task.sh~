#!/usr/bin/env bash
# DELETE THE OUTPUT DIR init_cluster_centers-output
hadoop fs -rm -r init_cluster_centers-output
# DELETE THE OUTPUT DIR init_cluster_centers
hadoop fs -rm -r init_cluster_centers
# DELETE THE OUTPUT DIR coordinate
hadoop fs -rm -r coordinate

cd /home/PythonCode/K-Means
# produce 80 coordinate data
python random_data_produce.py
# produce 8 init cluster centerns
python reservoir_sample.py

# create the INPUT DIR
hadoop fs -mkdir -p coordinate
# put the  coordinate file to HDFS
hadoop fs -put /home/PythonCode/K-Means/coordinate.txt coordinate

# run MapReduce job
cd /usr/local/hadoop/hadoop-3.0.3
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.0.3.jar \
-file /home/PythonCode/K-Means/mapper.py    -mapper /home/PythonCode/K-Means/mapper.py \
-file /home/PythonCode/K-Means/reducer.py   -reducer /home/PythonCode/K-Means/reducer.py \
-input coordinate/*  -output init_cluster_centers-output

# get MapReduce output and Change its name
mkdir -p /home/map_reduce_result
cd /home/map_reduce_result
hadoop fs -get init_cluster_centers-output
cur_date="`date +%Y%m%d_%H:%M:%S`" 
mv init_cluster_centers-output $cur_date
