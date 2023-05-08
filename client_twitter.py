from pyspark.sql import SparkSession 
from pyspark.sql import functions as f # importando as funções em Dados, do DF do Spark

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

lines = spark.readStream\
    .format('socket')\
    .option('host','localhost')\
    .option('port',9009)\
    .load()
words = lines.select(f.explode(f.split(lines.value, " ")).alias('word'))

# conteúdo da coluna, trataremos para poder contar, quebrando de acordo com o " "
# entenda que, SELEÇÃO DE DENTRO DO DF - explode (em cada linha, doq foi cortado), na lista de palavras, do conteúdo

wordCounts = words.groupBy('word').count() # conte cada palavra de cada linha, já que explodimos para cad linha.

query = wordCounts.writeStream\
    .outputMode('complete')\
    .format('console')\
    .start()

# para este tipo de averiguação usamos o complete, quando formos ver o nosso dataframe, com diferentes frequências de palavras, agrupadas iguais, esperando completamente - o primeiro SLOT
query.awaitTermination() 