import requests
from bs4 import BeautifulSoup

import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("select url,current_url,id from 301_redirect_dba_69  where id>30000")
myresults = cur.fetchall()
for fetch in myresults:
    url = fetch[0]
    current_url = fetch[1]
    id = fetch[2]
    page = requests.get(url)
    status = page.status_code
    response = page.history[0].status_code
    if status == 200:
        print("page url is working")
        if response == 301:
            s = page.url
            if s.split() == current_url.split():
                s1 = ('match')
                s = ("301")
                sql = ("UPDATE 301_redirect_dba_69 SET status ='" + str(s) + "',check_redirect ='" + str(s1) + "' WHERE   id='" + str(
                    id) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                s1 = ('not match')
                s = ("301")
                sql = ("UPDATE 301_redirect_dba_69 SET status ='" + str(s) + "',check_redirect ='" + str(
                    s1) + "' WHERE   id='" + str(
                    id) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        elif response == 302:
            print("page move is only temporary")
        else:
            print("something else")
    else:
        s = '404'
        sql = ("UPDATE 301_redirect_dba_69 SET status ='" + str(s) + "' WHERE   id='" + str(
            id) + "' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        