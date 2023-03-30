import itertools
import urllib

from PIL import Image
from hurry.filesize import size
import mysql.connector
import requests
import csv
import pandas as pd
import xlsxwriter
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()


with open(r'C:\Users\ashish\Documents\Book3.csv','rt')as f:
        data = csv.reader(f)

        for row in itertools.islice(data,838,1000):
            st=row[0]
            t=(st)
            r = requests.get(st)
            s = (r.status_code)
            size1 = requests.get(st).content
            y = (len(size1))
            z = (size(y))

            cur = mydb.cursor()
            sql = ("INSERT INTO datasheet (product_url,status,size) VALUES (%s, %s,%s)" )
            val = (t,s,z,)


            cur.execute(sql,val)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")

