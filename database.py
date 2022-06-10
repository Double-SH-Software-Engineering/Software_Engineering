from datetime import datetime
import pymysql


class Database:
    def __init__(self):
        DB = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='-',
            db='SEDB',
            charset='utf8'
        )
        self.db = DB

    def login(self, id_, pwd):
        cursors = self.db.cursor()
        sql = """select user_ID, Password_ from Customer"""
        cursors.execute(sql)
        item = list(cursors.fetchall())
        self.db.commit()
        info = (id_, pwd)
        cond = 0
        for i in item:
            if info == i:
                cond = 1
                break

        if cond == 1:
            return True
        else:
            return False

    def signup(self, id_, pwd):
        cursors = self.db.cursor()
        sql = """select user_ID from Customer"""
        cursors.execute(sql)
        item = list(cursors.fetchall())
        self.db.commit()

        if (id_,) in item :
            return False
        else:
            sql = """insert into Customer values (%s, %s)"""
            cursors.execute(sql,(id_,pwd))
            cursors.fetchall()
            self.db.commit()
            return True
        
    def product_detail(self,product_id):
        cursors = self.db.cursor()
        
        sql =  "select * from product where product_id=" + str(product_id) 
        cursors.execute(sql)    
        for c in cursors:
            product = c
        
        return product

    def product_list(self):
        cursors = self.db.cursor()
        sql = "select product_id, product_name,user_ID, register_date,soldout from product"
        cursors.execute(sql)
        product = list(cursors.fetchall())

        return product


    def profile_item(self, uid):
        cursors = self.db.cursor()
        sql = "select product_id, product_name, register_date,soldout from product where user_ID = %s"
        cursors.execute(sql,uid)

        product_t = list(cursors.fetchall())
        product = []
        for i in product_t:
            i = list(i)
            product.append(i)

        return product

    def search_item(self, keyword):
        cursors = self.db.cursor()
        sql = "select product_id, product_name, user_ID, register_date,soldout from product where keyword = %s"
        cursors.execute(sql,keyword)

        product_t = list(cursors.fetchall())
        product = []
        for i in product_t:
            i = list(i)
            product.append(i)

        return product
    
    def upload_info(self, uid, pname, price, keyword, descript, soldout):
        now_date = datetime.now().date()
        r_date = now_date.strftime("%Y-%m-%d")
        
        cursors = self.db.cursor()
        sql = "insert into product(user_ID, product_name, price, register_date, keyword, description_, soldout) values ( %s, %s, %s, %s, %s, %s, %s)"        
        cursors.execute(sql, (uid, pname, price, r_date, keyword, descript, soldout))
        cursors.fetchall()
        self.db.commit()
        pid = cursors.lastrowid
        
        return str(pid)
        
   
        
    def upload_url(self, pid, purl):
        cursors = self.db.cursor()
        sql = "insert into Product_image values (%s, %s)"
        cursors.execute(sql, (pid, purl))
        cursors.fetchall()
        self.db.commit()
        
    def show_image(self,pid):
        cursors = self.db.cursor()
        sql = "select image from product_image where product_id = %s"
        cursors.execute(sql,pid)
        p_images = list(cursors.fetchall())
        for i in range(len(p_images)):
            p_images[i] = p_images[i][0]
        
        
        return p_images
    
    def search_product(self, pid):
        
        cursors = self.db.cursor()
        sql = "select product_name, description_ , keyword, price, soldout from product where product_id = %s"
                
        cursors.execute(sql, pid)
        product = list(cursors.fetchall())
        product = product[0]
        product = list(product)
        product.append(pid)
        
        
        
        return product
    
    def user_certificate(self,pid):
        cursors = self.db.cursor()
        sql = "select user_ID from product where product_id = %s"
        cursors.execute(sql,pid)
        user = list(cursors.fetchall())
        user = user[0][0]
        return user
    
    def modify_sold(self, pid, soldoption):
        cursors = self.db.cursor()
        sql = "update product set soldout = %s where product_ID = %s;"
        cursors.execute(sql,(soldoption,pid))
        cursors.fetchall()
        self.db.commit()
        


    
    

