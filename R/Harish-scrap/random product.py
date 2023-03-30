import random
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="link_create"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT entity_id FROM `missing_random` WHERE id BETWEEN 99363 AND 100000")

myresult = mycursor.fetchall()

for x in myresult:

   entity_id = x[0]

   temp = []

   i = 0

   while i < 5:

       ab = random.randint(1,1456658)

       if ab not in temp:

          temp.append(ab)

          i = i + 1

   for entry in temp :

       ra_no = (entry)

       product_id = entity_id

       sql = "INSERT INTO product_random (entity_id, ra_no) VALUES (%s, %s)"

       mycursor.execute(sql,(product_id,ra_no,))

       mydb.commit()

       print(mycursor.rowcount, "record inserted.")
