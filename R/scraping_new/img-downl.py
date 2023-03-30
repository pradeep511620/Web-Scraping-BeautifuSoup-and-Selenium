import mysql.connector
import requests
import shutil

mydb = mysql.connector.connect(
host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raghav_scrape"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT name,url FROM `rag`")

myresult = mycursor.fetchall()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for row in myresult:
 try:
     image_name = row[0]
     print(image_name)
     image_url = row[1]
     print(image_url)
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