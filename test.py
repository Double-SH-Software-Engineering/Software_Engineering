import pymysql
from datetime import datetime



DB = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='-',
            db='SEDB',
            charset='utf8'
)






