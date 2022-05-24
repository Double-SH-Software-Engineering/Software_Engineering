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

product = []
uid = 'heejun'
cursors = DB.cursor()
sql = "select product_id, product_name,user_ID,register_date,soldout from product where user_ID = %s"
cursors.execute(sql, uid)
item_t = list(cursors.fetchall())
item = []
for i in item_t:
    i = list(i)
    item.append(i)
print(item)
pro_item = []
for i in item:
    pro_item.append(i[:-1])

print(pro_item)