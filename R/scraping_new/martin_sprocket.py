import requests
from bs4 import BeautifulSoup
from typing import TextIO

myresult=['https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=100A10&Website_CategoryName=Sprockets&Website_Code=SP1']

for row in myresult:

 try:

    product_url = row
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)","Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working" + str(result.status_code))

    # a = (result.content.decode())

    soup = BeautifulSoup(result.content, 'html.parser')
    print(soup.prettify())



    title = soup.find("div",attrs = {'style':'float: left; margin-left: 20px; width: 400px;'}).find_all("span")
    description=title[0].text.strip()
    print(description)
    a=(description if description else "not given")
    part=title[1].text.strip()
    print(part)
    b=(part if part else "not given")

    rest = soup.find("div", attrs={'style': 'float: left; margin-left: 20px; width: 400px;'}).find_all("div")
    upc = rest[0].text.strip()
    print(upc)
    cc=(upc if upc else "not given")
    data = rest[1].text.strip()
    print(data)
    d=(data if data else "not given")



    imgg=soup.find("img")
    y = (imgg.get("src") if imgg else "not given")
    print(y)

    c = (product_url)
    print(c)

    prod = soup.find_all("td",attrs = {'style':'text-align: left; color: black; background-color: #eeeeee; border: 1px solid silver; width: 200px;'})

    specs = soup.find_all("td",attrs = {'style':'text-align: right; background-color: White; border: 1px solid silver; width: 200px;'})


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
            save_details: TextIO = open("martin1=1.txt", "a+", encoding="utf-8")
            save_details.write("\n"+a+"\t"+b+"\t"+cc+"\t"+d+"\t"+y+"\t"+c+"\t"+"RP_"+z+"\t"+"RP_"+x)
            save_details.close()
            print("\n**Record stored into txt file.**")








 except AttributeError:

   pass
