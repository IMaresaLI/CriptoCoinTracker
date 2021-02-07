import mysql
import sqlite3


def Add(tableNames, name, current_price, low_24h, high_24h, history):
    connection = sqlite3.connect("Crypto.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {tableNames}(name,current_price,low_24h,high_24h,history) VALUES (?,?,?,?,?)",
                       (name, current_price, low_24h, high_24h, history))
    connection.commit()
    connection.close()
    
def getDatabase(tableName):
    connection = sqlite3.connect("Crypto.db")
    cursor = connection.cursor()
    cursor.execute(f"Select * from {tableName}")
    data = cursor.fetchall()
    connection.close()
    return data

def mysqlCon(host,user,passwd,database):
    connection = mysql.connector.connect(
        host=host, 
        user=user, 
        password=passwd, 
        database=database, 
        charset='utf8')
    cursor = connection.cursor()
    return cursor


