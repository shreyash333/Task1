import mysql.connector

mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="123456", database="TCS")
mainDB_Cursor = mysqldb.cursor()
