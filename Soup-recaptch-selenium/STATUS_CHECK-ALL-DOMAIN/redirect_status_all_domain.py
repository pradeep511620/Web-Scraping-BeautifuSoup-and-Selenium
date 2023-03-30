
import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM test_redirect_all_domain where id >1946")
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    url1=(brand_url)
    page = requests.get(brand_url)

    s=(page.status_code)
    t=(page.history)
    sql = (" UPDATE test_redirect_all_domain SET status='" + str(s) + "' ,response='"+str(t)+"' WHERE url='" + str(brand_url) + "' ")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")