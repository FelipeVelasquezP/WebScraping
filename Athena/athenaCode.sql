#Creacion de la base de Datos
create database yahooscraping

#Creacion de la tabla particionada , de acuerdo con el bucket donde se almaceno lo ejecutado en la funcion lambda
CREATE EXTERNAL TABLE `periodicos`(
  `category` date, 
  `title` float, 
  `url` float)
PARTITIONED BY ( 
  `periodico` string, 
  `year` int, 
  `month` int, 
  `day` int)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://newsscrapingcsv/stocks'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1634426186',
  'skip.header.line.count'='1')

#Particionamiento de la tabla
MSCK REPAIR TABLE periodicos;

#Prueba de la particion
select * from periodicos