from pyspark.sql import SparkSession 
import shutil

for item in ['/check','./csv']:
    try:
        shutil.mtree(item)
    except OSError as err:
        print(f'Aviso {err.strerror}')

#tratamento em cada arquivo, para se caso algum tweet venha com erro, ele não passe por aquilo


spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

tweets = spark.readStream\
    .format('socket')\
    .option('host','localhost')\
    .option('port',9009)\
    .load()

query = tweets.writeStream\
    .outputMode('append')\
    .option('encoding','utf-8')\
    .format('csv')\
    .option('path','./csv')\
    .option('checkpointLocation','./check')\
    .start()

# forma de armazenamento dos Tweets - append(oq vem novo ele vai guardando)

query.awaitTermination() 