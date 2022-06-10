import pymysql
from datetime import datetime

DB = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='!9535010a',
            db='SEDB',
            charset='utf8'
)
username = "1234"

cursors = DB.cursor()

sql = "select followee from follow where user_ID = %s"
cursors.execute(sql,username)
list_follow = cursors.fetchall()


print(list_follow[1][0])
