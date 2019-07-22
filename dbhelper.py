import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self._connection=mysql.connector.connect(host="127.0.0.1", user="root", password="",database="tinderb2")
            self._cursor=self._connection.cursor()
            print("Connected to database")
        except:
            print("Could not connect")
            exit(0)

    def search(self, key1, value1, key2, value2, table):
        self._cursor.execute("""
        SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'""".format(table,key1,value1,key2,value2))
        data=self._cursor.fetchall()
        return data
    def searchOne(self,key1,value1,table,type):
        self._cursor.execute(""" SELECT * FROM `{}` WHERE `{}` {} '{}'""".format(table, key1, type, value1))
        data = self._cursor.fetchall()
        return data

    def insert(self,insertDict,table):
        #"""INSERT INTO `users` (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES ('NULL', 'Virat', 'virat@gmail.com','1234','Male','25','Mumbai')"""

        colValue=""
        dataValue=""
        for i in insertDict:
            colValue=colValue + "`" + i + "`,"
            dataValue=dataValue + "'" + insertDict[i] + "',"
        colValue=colValue[0:-1]
        dataValue=dataValue[0:-1]

        query="""INSERT INTO `{}` ({}) VALUES ({})""".format(table,colValue,dataValue)

        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0