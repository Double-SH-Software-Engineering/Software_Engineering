import pymysql

class Database:
    def __init__(self):
        DB = pymysql.connect(
            host='-',
            port='-',
            user='-',
            password='-',
            db='-',
            charset='utf8'
        )
        self.db = DB

    def login(self, id_, pwd):
        cursors = self.db.cursor()
        sql = """select ID, Password_ from Customer"""
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
        sql = """select ID from Customer"""
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


    def write_post(self, id_, contents,):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass
