import sqlite3

class DB:
    def __init__(self) -> None:
        con = sqlite3.connect('db.sqlite3' ,  check_same_thread=False)
        self.cur = con.cursor()

    def emailExists(self , email):
        sql = "select * from user where email = '"+email+"'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        if(len(rows)>0):
            return True
        else:
            return False
