import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re


myresult=['https://www.mcmaster.com/7843K5/']

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

    print(soup.prettify())

    title = soup.find("div",class_="heading-title heading-dotted text-center")
    a = (title.text.strip() if title else "not given")
    print(a)
    a=a.split(":")[1]
    a=a.split()
    print(a)






    brand = soup.find("h2")



    image = soup.find("img",attrs={'alt':a})

    y = (image.get("src") if image else "not given")
    print(y)

    c = (product_url)
    print(c)

    d = (brand.text.strip() if brand else "not given")
    print(d)
    pd = soup.find("a", attrs={'title': 'Download Drawing'})

    pp = (pd.get("href") if pd else "not given")
    print(pp)



    prod = soup.find_all("strong",class_="text-primary")

    specs = soup.find_all("div",class_="col-8 text-left")

    i = 0

    while i < len(prod):

        j = 0

        while j < len(specs):

            z = (prod[i].text if prod else "not given")
            print(z)

            i += 1

            x = (specs[j].text if specs else "not given")
            print(x)

            j += 1
            save_details: TextIO = open("vestil_done.txt", "a+", encoding="utf-8")
            save_details.write("\n"+str(a)+"\t"+d+"\t"+c+"\t"+y+"\t"+pp+"\t"+"RP_"+z+"\t"+"RP_"+x)
            save_details.close()
            print("\n**Record stored into txt file.**")






 except AttributeError:

   pass
