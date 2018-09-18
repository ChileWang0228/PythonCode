#!/bin/bash 
#sudo su
hadoop fs -rm -r gutenberg-output
cd /usr/local/hadoop/hadoop-3.0.3
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-3.0.3.jar \
-file /home/PythonCode/map_reduce/mapper.py    -mapper /home/PythonCode/map_reduce/mapper.py \
-file /home/PythonCode/map_reduce/reducer.py   -reducer /home/PythonCode/map_reduce/reducer.py \
-input gutenberg/* -output gutenberg-output
mkdir -p /home/map_reduce_result
cd /home/map_reduce_result
hadoop fs -get gutenberg-output
cur_date="`date +%Y%m%d_%H:%M:%S`" 
name="test"
mv gutenberg-output $cur_date"_"$name
