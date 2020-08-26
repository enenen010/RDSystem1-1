import pymysql

con = pymysql.connect(
    user='root', 
    passwd='1234', 
    host='127.0.0.1', 
    db='juso-db', 
    charset='utf8'
)

def myInsert():
  