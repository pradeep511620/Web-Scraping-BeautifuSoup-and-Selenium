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
cur.execute("SELECT url,bullet FROM `general_pipe_cleaner_bullet`  ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    bullet = fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    for pd in soup.find("div", class_="product-description").find_all('ul'):
        s = str(pd)
        if s == bullet:
            bt = "bullet same"
            sql = "UPDATE  `general_pipe_cleaner_bullet` SET bullet_test ='" + str(bt) + "' where url='" + str(
                product_url) + "' "
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        else:
            bt1 = "bullet not same"
            sql = "UPDATE  `general_pipe_cleaner_bullet` SET bullet_test ='" + str(bt1) + "' where url='" + str(
                product_url) + "' "
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done but some issue ")
