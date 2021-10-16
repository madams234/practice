from pyspark.sql import SparkSession
from operator import add

spark = SparkSession.builder.appName("appName").getOrCreate() 

#Read data.csv in a RDD
raw_rdd = spark.sparkContext.\
           textFile("/sparkmini/data.csv")

# Map on the original RDD to create new RDD of key,value pair i.e ((vin_number),make,year,incident_type)
vin_kv = raw_rdd.map(lambda x:((x.split(",")[2]),(x.split(",")[3],x.split(",")[5],x.split(",")[1])))

#('VXIO456XLBB630221', ('Nissan', '2003', 'I'))
#('INU45KIOOPA343980', ('Mercedes', '2015', 'I'))


# GroupByKey is applied on above RDD of (K,V) as input to get an output RDD of (K,Iterable) pairs i.e. (vin_number, Iterable((make1,year1),(make2,year2)...)
# and flatMap on the iterable to get the make and year and final filter to get the records which have the make and year available
enhance_make_year = vin_kv.groupByKey().mapValues(lambda x:list(x)).\
                 flatMap(lambda x: [(item[0],item[1]) for (item) in x[1]]).\
                 filter(lambda x:x[0]!="" and x[1]!="")


# Map to get a RDD of ((make, year),1)
make_year = enhance_make_year.map(lambda x: ((x[0],x[1]),1))


# ReduceByKey to count the number of accidents per make and year
accident_rec_per_year = make_year.reduceByKey(add)

# A new RDD created using map to get the output in specific format 
accident_rec_per_year_frmt = accident_rec_per_year.map(lambda i:i[0][0]+"-"+i[0][1]+","+str(i[1]))

#['Nissan-2003,1', 'Mercedes-2015,2', 'Mercedes-2016,1', 'Toyota-2017,1']

# Save the final RDD 'accident_rec_per_year' as text file
accident_rec_per_year_frmt.saveAsTextFile("accident_records_count")