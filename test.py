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
cursors = DB.cursor()
keyword = "스포츠 용품"
sql = "select product_id, product_name,user_ID,register_date,soldout from product where keyword = %s"
cursors.execute(sql, keyword)
item_t = list(cursors.fetchall())
item = []
for i in item_t:
    i = list(i)
    item.append(i)
print(item)
