import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db1"
)
cur=mydb.cursor()
s="CREATE TABLE Book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(s)
