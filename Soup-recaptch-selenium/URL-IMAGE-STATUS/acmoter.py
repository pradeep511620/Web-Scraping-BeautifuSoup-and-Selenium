import urllib
import mysql.connector
from bs4 import BeautifulSoup
import requests
from hurry.filesize import size
from PIL import Image
import urllib.request, urllib.error
#headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM acmoter")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = (url)
    a = urllib.request.urlopen(url)
    print(a.getcode())

    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        c=(format(e.code))
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        c=(format(e.reason))
    else:
        # 200
        # ...
        c=('200')

    image = Image.open(urllib.request.urlopen(url))
    width, height = image.size
    p=(width, height)

    size1=requests.get(url).content
    s=(len(size1))
    z=(size(s))



    """sql=(" UPDATE acmoter SET status='"+str(c)+"',pixels='"+str(p)+"',size='"+str(z)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")"""