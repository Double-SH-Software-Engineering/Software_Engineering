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




pid = 6
cursors = DB.cursor()

sql = "delete from product_image where product_ID = %s;"
cursors.execute(sql,pid)
user = list(cursors.fetchall())
cursors.
print(user)

