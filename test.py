import pymysql


DB = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='!9535010a',
        db='SEDB',
        charset='utf8'
        )

cursors = DB.cursor()
        
sql =  "select * from product where product_id=" + str(1) 
cursors.execute(sql)
        
for c in cursors:
    product = c
# product = cursors.fetchall()

print(product)