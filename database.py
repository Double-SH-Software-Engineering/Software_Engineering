import pymysql

class Database:
    def __init__(self):
        DB = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='!9535010a',
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


    def write_post(self, id_, contents,):
        pass

    def product_list(self):
        cursors = self.db.cursor()
        sql = "select product_id, product_name,user_ID, register_date from product"
        cursors.execute(sql)
        product = list(cursors.fetchall())

        return product

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass
