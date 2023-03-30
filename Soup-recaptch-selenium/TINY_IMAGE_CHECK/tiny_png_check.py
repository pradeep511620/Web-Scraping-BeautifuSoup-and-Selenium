from PIL import Image
import io
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"

)
cur = mydb.cursor()
cur.execute('select image_url,id from `tiny_image_24_mar_after_update` where  status is null')
myresult = cur.fetchall()
for fetch in myresult:
    image_url = fetch[0]
    id = fetch[1]
    image_data = requests.get(image_url).content
    st = requests.get(image_url)
    img = Image.open(io.BytesIO(image_data))
    sta =st.status_code
    width, height = img.size
    s = f"{width}x{height}"
    exe = img.format
    mode = img.mode
    file_size_kb = len(image_data) / 1024

    file_size = (f"{file_size_kb:.2f} KB")

    sql = ("UPDATE `tiny_image_24_mar_after_update` SET status ='" + str(sta) + "',image_size ='" + str(s) + "',image_mode ='" + str(mode) + "',image_exe ='" + str(exe) + "',file_size ='" + str(file_size) + "' WHERE   id='" + str(id) + "'")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "records successful Done")

