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

product = []
cursors = DB.cursor()
sql = "select product_id, product_name,user_ID,register_date from product"
cursors.execute(sql)
item = list(cursors.fetchall())
for c in cursors:
    product.append(list(c))
print(item)
print(product)