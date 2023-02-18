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
        print(rows)
        for user in rows:
            tempDict = {}
            tempDict['email'] = user[4]
            tempDict['fname'] = user[0]
            tempDict['lname'] = user[1]
            tempDict['phone'] = user[3]
            tempDict['password'] = user[5]
            userDict.append(tempDict)
        return userDict
    
    def showUser(self , email):
        sql = "select * from user where email = '"+email+"'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return json.dumps(rows)
    
    def addBus(self , busName , busNumber , busTime , busSource , busDestination , busPrice , busCapacity , busDeparture , busArrival):
        sql = "insert into Bus (busName , busNumber , busTime , busSource , busDestination , busPrice , busCapacity , busDeparture , busArrival) values ('"+busName+"' , '"+busNumber+"' , '"+busTime+"' , '"+busSource+"' , '"+busDestination+"' , '"+busPrice+"' , '"+busCapacity+"' , '"+busDeparture+"' , '"+busArrival+"')"
        try:
            self.cur.execute(sql)
            self.con.commit()
            return True
        except:
            return False
    def showAllBuses(self):
        sql = "select * from Bus"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        busDict = []
        print(rows)
        for bus in rows:
            tempDict = {}
            tempDict['busName'] = bus[0]
            tempDict['busNumber'] = bus[1]
            tempDict['busTime'] = bus[2]
            tempDict['busSource'] = bus[3]
            tempDict['busDestination'] = bus[4]
            tempDict['busPrice'] = bus[5]
            tempDict['busCapacity'] = bus[6]
            tempDict['busDeparture'] = bus[7]
            tempDict['busArrival'] = bus[8]
            busDict.append(tempDict)
        return busDict