import pymysql
from config import Config

class Connection:
    def __init__(self):
        self.con = pymysql.connect(
            host = Config.HOST,
            user = Config.USER,
            password = Config.PASSWORD,
            db = Config.DBNAME,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        self.cur = self.con.cursor()
    
    def _select(self,sql,args=None):
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchone()
        self.cur.close()
        self.con.close()
        return self.sel
    
    def _selectAll(self,sql,args=None):
        self.cur.execute(sql,args)
        self.sel = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return self.sel