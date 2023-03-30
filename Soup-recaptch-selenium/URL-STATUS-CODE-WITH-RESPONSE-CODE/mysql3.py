import mysql.connector
from bs4 import BeautifulSoup
import requests
import httplib2

http = httplib2.Http()
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="rahul"
)

cur=mydb.cursor()

cur.execute("SELECT url FROM grainger WHERE STATUS is null")

myresult = cur.fetchall()

for x in myresult:

  url = x[0]

  a= print(url)

  page = requests.get(url, headers=headers)

  soup = BeautifulSoup(page.content,'html.parser')

  st=page.status_code
  b = print(st)
  sql=("UPDATE grainger SET STATUS='"+str(b)+"'  WHERE url='"+str(a)+"'")

  sql.execute(sql)

  mydb.commit()

  print(cur.rowcount, "record(s) affected")




