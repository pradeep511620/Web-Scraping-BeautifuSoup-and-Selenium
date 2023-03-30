import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re


myresult=['https://stage.raptorsupplies.com/pd/morse-drum/86']

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

    title = soup.find_all("img")
    list3=[]
    for tit in title:
        try:
            list3.append(tit.get("src"))
        except:
            pass
    print(list3)

    save_details: TextIO = open("dayton-11.txt", "a+", encoding="utf-8")
    save_details.write("\n"+c+"\t"+a+"\t"+" > ".join(list1)+" > "+k+"\t"+d+"\t"+e+"\t"+"rp_"+f+"\t"+"rp_"+g+"\t"+y+"\t"+u+"\t"+z+"\t"+"RP_"+x)
    save_details.close()
    print("\n**Record stored into txt file.**")






 except AttributeError:

   pass
