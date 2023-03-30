import random
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="link_create"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT entity_id,min_no,max_no FROM `missing_suggest` where id > 70246")

myresult = mycursor.fetchall()

for x in myresult:
 try :
     entity_id = x[0]

     min_no = x[1]

     max_no = x[2]

     min_no1 = int(min_no)

     max_no2 = int(max_no)

     temp = []

     i = 0

     if max_no2 - min_no1 + 1 < 5:

        n = max_no2 - min_no1 + 1

     else:

        n = 5

     while i < n:

        ab = random.randint(min_no1, max_no2)

        if ab not in temp:

           temp.append(ab)

           i = i + 1

     for entry in temp:

        ra_no = (entry)

        product_id = entity_id

        sql = "INSERT INTO data_random1 (entity_id, ra_no) VALUES (%s, %s)"

        mycursor.execute(sql,(product_id,ra_no,))

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

 except TypeError:

     pass


