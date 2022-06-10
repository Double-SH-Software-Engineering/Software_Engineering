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
username = "1 23"
follower ="1234"

cursors = DB.cursor()
sql = "select exists(select * from follow where user_ID = %s and followee = %s)"
cursors.execute(sql,(username,follower))
s = cursors.fetchall()
s= s[0][0]
print(s)




