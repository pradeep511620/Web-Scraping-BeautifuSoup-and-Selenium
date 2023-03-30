import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

myresult=[]

for row in myresult:

 try:

    product_url = row

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+str(result.status_code))

    #a = (result.content.decode())

    soup = BeautifulSoup(result.content, 'html.parser')
    #print(soup.prettify())

    # print(soup.prettify())

    title = soup.find("div", class_="module-product-detail-card__description b-body-copy excel_class")
    moree = soup.find("span", class_="b-eyebrow-small")
    if moree:
        aa = (moree.text.strip() if moree else "not given")
        print(aa)



    else:
        more = soup.find("a", class_="b-eyebrow-small b-eyebrow-small-link")
        aa = (more.text.strip() if more else "not given")
        print(aa)





    brand = soup.find("h1", class_="module-product-detail-card__title excel_class")
    try:
     bread = soup.find_all("div", class_="module-media-gallery__thumbnail-image-wrapper embed-responsive-item")
     list1 = []
     for b in bread:
        s=b.find("img")
        list1.append(s.get("data-src"))
     print(list1)
    except:
        list1=[]
    a = (title.text.strip() if title else "not given")
    print(a)
    imgg = soup.find("img", class_="rendition__image img-responsive staticSkuImage")
    # image = soup.find("img",attrs={'alt':a})

    y = (imgg.get("data-desktop-rendition") if imgg else "not given")
    print(y)

    c = (product_url)
    print(c)

    d = (brand.text.strip() if brand else "not given")
    print(d)


    prod = soup.find_all("div", class_="module-table__col b-eyebrow-small module-table__col-print")

    specs = soup.find_all("div", class_="module-table__col b-body-copy-small")

    i = 0

    while i < len(prod):

        j = 0

        while j < len(specs):
            z = (prod[i].text.strip() if prod else "not given")
            print(z)

            i += 1

            x = (specs[j].text.strip() if specs else "not given")
            print(x)

            j += 1
            save_details: TextIO = open("xyz1.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+aa+"\t"+a+"\t" + " , ".join(list1) + "\t" + d + "\t" + z + "\t" + "RP_" + x+"\t"+str(y))
            save_details.close()
            print("\n**Record stored into txt file.**")




 except AttributeError:

   pass
