import sqlite3
import json
class DB:
    def __init__(self) -> None:
        self.con = sqlite3.connect('db.sqlite3' ,  check_same_thread=False)
        self.cur = self.con.cursor()

    def emailExists(self , email):
        sql = "select * from user where email = '"+email+"'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        if(len(rows)>0):
            return True
        else:
            return False
    def addUser(self, email ,fname , lname , phone , password ):
        sql = "insert into user (email , fname , lname , phone , password) values ('"+email+"' , '"+fname+"' , '"+lname+"' , '"+phone+"' , '"+password+"')"
        try:
            self.cur.execute(sql)
            self.con.commit()
            return True
        except:
            return False
    def showAllUsers(self):
        sql = "select * from user"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        userDict = []
        for user in rows:
            tempDict = {}
            tempDict['email'] = user[1]
            tempDict['fname'] = user[2]
            tempDict['lname'] = user[3]
            tempDict['phone'] = user[4]
            tempDict['password'] = user[5]
            userDict.append(tempDict)
        return userDict
    
    def showUser(self , email):
        sql = "select * from user where email = '"+email+"'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return json.dumps(rows)
        
    