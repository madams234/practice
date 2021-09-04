hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /home/hdfs/hadoop2.py    -mapper /home/hdfs/hadoop2.py \
-file /home/hdfs/hadoopreduce.py   -reducer /home/hdfs/hadoopreduce.py \
-input /output/ \
-output /accidents_count_per_make
