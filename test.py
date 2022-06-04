import pymysql
from datetime import datetime

kwargs = {'host':'localhost', 'port':3306,'user':'root','password':'!9535010a','db':'SEDB', 'charset':'utf8'}

# DB = pymysql.connect(
#             host='localhost',
#             port=3306,
#             user='root',
#             password='!9535010a',
#             db='SEDB',
#             charset='utf8'
#         )

DB = pymysql.connect(**kwargs)



pid = 10
cursors = DB.cursor()
sql = '''select product_name, description_, keyword, price, soldout
    from product
    where product_id = ''' + str(pid)
                
cursors.execute(sql)
product = list(cursors.fetchall())
product = product[0]
product = list(product)
product[3] = str(product[3])
        
print(product)
