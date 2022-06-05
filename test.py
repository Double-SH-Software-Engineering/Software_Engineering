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




# pid = 6
# cursors = DB.cursor()
# sql = "select user_ID from product where product_id = %s"
# cursors.execute(sql,pid)
# user = list(cursors.fetchall())
# user = user[0][0]
# print(user)
        
a = 2
if a:
    print("참")
else:
    print("거짓")
        
        
