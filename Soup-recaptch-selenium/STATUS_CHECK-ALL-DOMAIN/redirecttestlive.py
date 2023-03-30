
import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM redirect_status_check where id between 2047 and 2690")
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    url1=(brand_url)
    page = requests.get(brand_url)

    s=(page.status_code)
    t=(page.history)
    sql = (" UPDATE redirect_status_check SET status='" + str(s) + "' ,response='"+str(t)+"' WHERE url='" + str(brand_url) + "' ")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")