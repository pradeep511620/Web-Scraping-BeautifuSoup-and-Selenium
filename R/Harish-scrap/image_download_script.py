import mysql.connector
import requests
import shutil

mydb = mysql.connector.connect(
   host="rpt-m24-stage-28-june.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
   user="raptoradmin",
   password="Raptorpwa2020",
   database="usa_inventory_updates_07_02_2022"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT image_name,image_url FROM `product_images`")

myresult = mycursor.fetchall()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for row in myresult:
 try:
     image_name = row[0]
     image_url = row[1]
     resp = requests.get(image_url, stream=True,headers=headers)

     if image_url.endswith(".jpg"):
        local_file = open(image_name+".jpg" ,'wb')

     elif image_url.endswith(".png"):
       local_file = open(image_name+".png",'wb')

     else:
         local_file = open(image_name + ".jpg", 'wb')

     resp.raw.decode_content = True
     shutil.copyfileobj(resp.raw,local_file)
     del resp

     print(image_name)

 except:

     pass