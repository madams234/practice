hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /home/hdfs/hadoop.py    -mapper /home/hdfs/hadoop.py \
-file /home/hdfs/hadoopreduce.py   -reducer /home/hdfs/hadoopreduce.py \
-input /hadoopminiprk/data.csv \
-output /output