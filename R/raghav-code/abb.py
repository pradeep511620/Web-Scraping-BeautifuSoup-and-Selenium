import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re



myresult=[]

for row in myresult:

 try:

    product_url = row
    print(row)

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print(result.status_code)

    #a = (result.content.decode())

    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())

    data=soup.find("div",class_="warning site-message")

    y = (data.text.strip() if data else "not given")
    print(y)
    save_details: TextIO = open("abbbbaa.txt", "a+", encoding="utf-8")
    save_details.write("\n" + row + "\t" + y)
    save_details.close()
    print("\n**Record stored into txt file.**")








 except AttributeError:

   pass
