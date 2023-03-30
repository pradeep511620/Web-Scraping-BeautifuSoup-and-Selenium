from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_staging"
)
cur = mydb.cursor()
cur.execute("SELECT url from url_hit_aug WHERE STATUS='404'")
myresult = cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page=requests.get(url)
    s=(page.status_code)
    r=(page.history)
    c=(page.url)
    sql=("update url_hit_aug set status='"+str(s)+"',response='" +str(r)+"',current_url='"+str(c)+"' where url='"+str(url)+"' ")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount,"record successful")