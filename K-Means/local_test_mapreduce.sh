cd /home/PythonCode/K-Means
# produce 80 coordinate data
python random_data_produce.py
# produce 8 init cluster centerns
python reservoir_sample.py
#Test the mapreduce procedure
cat coordinate.txt | python mapper.py | sort | python reducer.py

