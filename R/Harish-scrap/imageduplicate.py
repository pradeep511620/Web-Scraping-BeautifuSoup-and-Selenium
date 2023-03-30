from PIL import Image
import imagehash
import mysql.connector
import os, os.path

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testing"
)

mycursor = mydb.cursor()

table_name = "duplicate_image2"

mycursor.execute("DROP TABLE "+str(table_name)+"")

mycursor.execute("CREATE TABLE "+str(table_name)+" (image_name mediumtext, status1 mediumtext,status2 mediumtext,status3 mediumtext,status4 mediumtext)")

path = r"C:/Users/Harish/Desktop/product2/product2"

valid_images = [".jpg",".png"]

for f in os.listdir(path):
 try:
    ext = os.path.splitext(f)[1]

    if ext.lower() not in valid_images:

        continue

    status = (Image.open(os.path.join(path,f)))

    hash = imagehash.dhash(status)

    hash1 = imagehash.colorhash(status)

    hash2 = imagehash.phash(status)

    hash3 = imagehash.average_hash(status)

    status1 = (hash)

    status2 = (hash1)

    status3 = (hash2)

    status4 = (hash3)


    image_name = (f)

    mycursor = mydb.cursor()

    sql = ('INSERT INTO duplicate_image2(image_name,status1,status2,status3,status4) VALUES (%s,%s,%s,%s,%s)')

    mycursor.execute(sql, (str(image_name),str(status1),str(status2),str(status3),str(status4),))

    print(mycursor.rowcount, "succesfully inserted")

    mydb.commit()

 except OSError:

     print(image_name)

     pass