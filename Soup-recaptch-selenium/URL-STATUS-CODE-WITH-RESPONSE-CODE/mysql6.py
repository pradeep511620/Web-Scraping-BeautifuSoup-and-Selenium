import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db1"
)

mycursor = mydb.cursor()

sql = "UPDATE customer SET name = 'Rahul kumar singh' WHERE place = 'bihar' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")