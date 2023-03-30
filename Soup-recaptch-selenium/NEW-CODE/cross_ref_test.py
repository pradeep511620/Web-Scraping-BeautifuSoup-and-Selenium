from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="new_stage_data"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,cross_ref,id FROM `genral_pipe_cleaner` limit 1")
myresult = cur.fetchall()

for fetch in myresult:

    product_url = fetch[0]
    cross_ref = fetch[1]
    id = fetch[2]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    s = dict()
    a = 0
    for attr in soup.find("div", class_="brand-info").find_all("span")[1:]:
        a += 1
        z = (attr.text)
        if a == 3:
            print(z)
            c = ("Cross Ref: "+ cross_ref)
            # if c == z:
            #     par = ("cross_ref same")
            #     sql = ("UPDATE `genral_pipe_cleaner` SET cross_ref_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            #     cur.execute(sql)
            #     mydb.commit()
            #     print(cur.rowcount, "records successful Done")
            # else:
            #     par1 = ("cross_ref not same")
            #     sql = ("UPDATE `genral_pipe_cleaner` SET cross_ref_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            #     cur.execute(sql)
            #     mydb.commit()
            #     print(cur.rowcount, "records successful Done")

