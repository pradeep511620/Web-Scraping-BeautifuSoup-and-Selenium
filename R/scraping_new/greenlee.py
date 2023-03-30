import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re




myresult=['https://www.greenlee.com/us/en/double-vision-dual-display-wireless-voltage-indicating-phaser-100v138kv-ohugsingle-kit-1-783310043041']

for row in myresult:

 try:

    product_url = row

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+result.status_code)

    #a = (result.content.decode())


    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())

    try:
     pd=soup.find_all("a",class_="file-download")
     list2=[]
     for p in pd:
        list2.append(p.get("href"))
     print(list2)
    except:
        list2=[]
    bc=soup.find("ul",class_="breadcrumb").find_all("li")
    list1=[]
    for b in bc:
        list1.append(b.text.strip())
    print(list1)

    title = soup.find("h1",class_="hide-on-small-only")
    a = (title.text.strip() if title else "not given")
    print(a)
    sku1=soup.find("div",class_="left single-sku-info")
    sku11=(sku1.text.strip() if sku1 else "not given")
    print(sku11)
    sku2 = soup.find("div", class_="left single-sku-info p-l-10")
    sku22 = (sku2.text.strip() if sku2 else "not given")
    print(sku22)


    image = soup.find("meta",attrs={'property':'og:image'})

    y = (image.get("content") if image else "not given")
    print(y)


    c = (product_url)
    print(c)
    model = soup.find("table",class_="alternate odd").find_all("td")
    print(len(model))
    i=0




    while i < len(model):

            z = (model[i].text if model else "not given")
            print(z)
            j=i+1
            i=j+1
            x = (model[j].text if model else "not given")
            print(x)


            save_details: TextIO = open("greenlee-done11156.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+a+"\t"+str(y)+"\t"+" > ".join(list1)+"\t"+" , ".join(list2)+"\t"+sku11+"\t"+sku22+"\t"+"RP_"+z+"\t"+"RP_"+x)
            save_details.close()
            print("\n**Record stored into txt file.**")






 except AttributeError:

   pass
