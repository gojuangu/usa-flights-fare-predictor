import zipfile
import os
import glob
import zipfile
from os import listdir
from os.path import isfile, join
from pyspark.sql import SparkSession


# This function allows you to unzipp all the downloaded files functions

# def unzipp(path, target_path):
#    print('descompressing')
#    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#    for o in onlyfiles:
#        if o.endswith(".zip"):
#            zip = zipfile.ZipFile(o, 'r')
#            zip.extractall(target_path)
#            zip.close()
#    print('descompresed')

# Function to create the of pySpark
def sparkbuilder():
    print('start 1')
    spark = SparkSession.builder. \
        appName('<nombre_app>'). \
        master('local[2]'). \
        config('spark.sql.session.timeZone', 'UTC'). \
        config('spark.sql.repl.eagerEval.enabled', True). \
        config('spark.driver.memory', '4G'). \
        getOrCreate()
    print('start 2')
    return spark


# Function to read the CSV and convert them to parquet
def spark_parquet(spark, path_t, path_c, target_path):
    print('partq')

    df_t = spark.read.format("csv") \
        .option("header", "true") \
        .option("mode", "DROPMALFORMED") \
        .load(f'{path_t}/Origin_and_Destination_Survey_DB1BTicket*.csv')
    df_t.write.parquet(f'{target_path}/1')

    df_c = spark.read.format("csv") \
        .option("header", "true") \
        .option("mode", "DROPMALFORMED") \
        .load(f'{path_c}/Origin_and_Destination_Survey_DB1BCoupon*.csv')
    df_c.write.parquet(f'{target_path}/2')

    print('dfdfgh')


# Function to read the parquet file
def read_parquet_ticket(spark, path_pt):
    print('lets read')
    df_t = spark.read.format("parquet") \
        .option("header", "true") \
        .option("mode", "DROPMALFORMED") \
        .load(path_pt)
    return df_t

def read_parquet_coupon(spark, path_pc):
    print('lets read')
    df_c = spark.read.format("parquet") \
        .option("header", "true") \
        .option("mode", "DROPMALFORMED") \
        .load(path_pc)
    print('finish reading')
    return df_c
