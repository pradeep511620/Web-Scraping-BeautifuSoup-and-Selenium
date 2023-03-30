import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

myresult=['https://catalog.nibco.com/item/gate-valves-4/lass-150-ductile-iron-bronze-trim-flanged-f-639-31/nha703j']

for row in myresult:

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

    title1 = soup.find("nav", id="plp-product-title")
    title2 = title1.find('h1')
    title = (title2.text.strip() if title2 else "not given")
    print(title)

    try:
        bread = soup.find("nav", {'id': "plp-bread-crumb", "class" :"ui-corner-all ui-widget-header"}).find_all('span', itemprop = "name")
        list1 = []
        for b in bread:
            list1.append(b.text.strip())
        print(list1)
    except:
        list1 = []

    bread = soup.find("nav", {'id': "plp-bread-crumb", "class": "ui-corner-all ui-widget-header"})\
        .find_all('span', itemprop = "name")
    list_b = []
    for b in bread:
        list_b.append(b.text.strip())
    mat_no = (list_b[-1].replace('Material Number', '') if list_b else "not given")
    print(mat_no)

    desc1 = soup.find("div", class_="plp-item-description")
    desc = (desc1.text.strip() if desc1 else "not given")
    print(desc)

    img1 = soup.find("li", {'data-clientid-wt' : "ImageBrowserPopup"}).find('img')
    image = (img1['src'] if img1 else "not given")
    print(image)

    prod1 = soup.find("table", class_="plp-table")
    if prod1:
        prod3 = prod1.find_all("td", class_="plp-table-name left")  # plp-item-table
    else:
        prod1 = soup.find("table", class_="plp-item-table")
        prod3 = prod1.find_all("td", class_="plp-table-name left")  # plp-item-table
    loc1 = 0
    prod_lst = []
    for p3 in prod3:
        loc1 += 1
        prod = p3.text.strip()
        prod_lst.append(prod)
        print(loc1, prod)
    print(prod_lst)
    specs1 = prod1.find_all("td", class_="plp-table-value")
    # print(specs1)
    loc2 = 0
    spec_lst = []
    for s1 in specs1:
        loc2 += 1
        specs2 = s1.text.strip()
        specs3 = specs2.replace('N/A', '')
        specs = specs3.replace('\n', '')
        spec_lst.append(specs)
        print(loc2, specs)
    print(spec_lst)

    i = 0
    while i < len(prod_lst):
        j = 0
        while j < len(spec_lst):
            z = (prod_lst[i] if prod_lst else "not given")
            print(z)
            i += 1
            x = (spec_lst[j] if spec_lst else "not given")
            print(x)
            j += 1
            save_details: TextIO = open("nibco_final1.txt", "a+", encoding="utf-8")
            save_details.write("\n" + product_url + "\t" + title + "\t" + mat_no + "\t" + desc + "\t" + " , ".join(
                list1) + "\t" + str(image) + "\t" + "rp_" + z + "\t" + "rp_" + x)
            save_details.close()
            print("\n**Record stored into txt file.**")


 except AttributeError:

   pass

