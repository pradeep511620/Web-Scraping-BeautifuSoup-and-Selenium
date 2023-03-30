import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

myresult=['https://www.myntra.com/2175341']

for row in myresult:

 try:

    product_url = row

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+str(result.status_code))

    #a = (result.content.decode())


    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())

    bread = soup.find_all("div",class_="image-grid-image")
    list1 = []
    for b in bread:
        list1.append(b)
    print(list1)


    save_details: TextIO = open("myntra.txt", "a+", encoding="utf-8")
    save_details.write("\n" + product_url + "\t" + " / ".join(list1))
    save_details.close()
    print("\n**Record stored into txt file.**")


 except AttributeError:

   pass
