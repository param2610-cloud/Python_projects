import mysql.connector 
conn= mysql.connector.connect(host='localhost',password='#S^9k6B0%N7', user='root')

if conn.is_connected():
    print("connection established")