import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

myresult=['https://www.jmac.com/Altronix_6062_p/altronix-6062.htm',
          'https://www.jmac.com/Altronix_AT4_p/altronix-at4.htm',
          'https://www.jmac.com/Altronix_60628HR_p/altronix-60628hr.htm',
          'https://www.jmac.com/Altronix_DSTAT4_p/altronix-dstat4.htm']
loc = 0
for row in myresult:
 loc +=1
 print("URL : ", loc)
 try:

    product_url = row
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    result = requests.get(product_url, headers=headers)
    if result.status_code == 200:
        print("site working")
    else:
        print("site not working"+str(result.status_code))
    #a = (result.content.decode())

    soup = BeautifulSoup(result.content, 'html.parser')
    #print(soup.prettify())
    print(product_url)

    # listbr=[]
    # for u in upc:
    #    listbr.append(u.text.strip())
    # print(listbr)

    title1 = soup.find("font", class_= 'productnamecolorLARGE colors_productname').find('span', itemprop="name")
    title = (title1.text.strip() if title1 else "not given")
    print(title)

    proCode1 = soup.find("span", class_= "product_code")
    proCode = (proCode1.text.strip() if proCode1 else "not given")
    print(proCode)

    price1 = soup.find("span", itemprop="price")
    price = (price1.text.strip() if price1 else "not given")
    print(price)

    image1 = soup.find("img", class_="vCSS_img_product_photo_small")
    image = (image1['src'] if image1 else "not given")
    print(image)

    listb=[]
    for bread1 in soup.find("td", class_="vCSS_breadcrumb_td").find_all("a"):
       bread = (bread1.text.strip() if bread1 else "not given")
       listb.append(bread)
    print(listb)
    # prod2 = soup.find("table", attrs={"style": "text-align: left; width: 100%;"}).find_all("li")
    prod1 = soup.find("table",attrs={"style": "text-align: left; width: 100%;"}).find_all("li")
    for p in prod1:
       prod = p.text.strip()
       print(prod)
       save_details: TextIO = open("2jmac2.txt", "a+", encoding="utf-8")
       save_details.write("\n" + product_url + "\t" + title + "\t" + proCode + "\t" + price + "\t" + image + "\t" + " > ".join(listb) + "\t" + prod)
       save_details.close()
       print("\n**Record stored into txt file.**")#//*[@id="vCSS_mainform"]/table[2]/tbody/tr[1]/td[1]/table[2]/tbody/tr[2]/td[2]/text()

 except AttributeError:

   pass

