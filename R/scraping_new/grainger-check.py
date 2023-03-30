import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re




myresult=['https://www.grainger.com/product/19NP76']

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

    title = soup.find("h1",class_="product-detail__heading")


    bread = soup.find_all("a",class_="breadcrumb__link")






    brand = soup.find("p",class_="product-detail__brand")


    model = soup.find_all("span",class_="product-detail__product-identifiers-description")


    #price = soup.find("span",class_="pricing__price")


    # qnt = (soup.prettify().replace('data-ship-pack-quantity="', "raptor:").split("raptor:")[1].split('"')[0])

    #weight = soup.find("div",class_="rta sidebar__shipping-pane")

    country = soup.find("span",attrs={'data-automated-test':'leaf'})




    #detail = soup.find("div",class_="copyTextSection textSection")
    #image enhanced-content__carousel-main-image image--loaded
    #soup.find("span",attrs={'data-automated-test':'leaf'})
    a = (title.text.strip() if title else "not given")
    print(a)
    imgg=soup.find("div",class_="enhanced-content__carousel-image-container").find("img")
    #image = soup.find("img",attrs={'alt':a})

    y = (imgg.get("src") if imgg else "not given")
    print(y)


    b = (bread[0].text.strip() if bread else "not given")
    print(b)

    m = (bread[1].text.strip() if bread else "not given")
    print(m)
    n = (bread[2].text.strip() if bread else "not given")
    print(n)
    o = (bread[3].text.strip() if bread else "not given")
    print(o)




    c = (product_url)
    print(c)

    d = (brand.text.strip() if brand else "not given")
    print(d)

    e = (model[0].text.strip() if model else "not given")
    print(e)

    f = (model[1].text.strip() if model else "not given")
    print(f)

    g = (model[2].text.strip() if model else "not given")
    print(g)



    #u = (price.text.strip() if price else "not given")
    #print(u)

    #v = print(weight.text)

    k = (country.text if country else "not given")
    print(k)

    #m = (detail.text.strip())


    #
    # zxqw = qnt
    #https://static.grainger.com/rp/s/is/image/Grainger/29DJ11_GC01?hei=804&wid=804

    prod = soup.find_all("span",class_="specifications__description")

    specs = soup.find_all("span",class_="specifications__value")

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
            save_details: TextIO = open("--tyg----.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+a+"\t"+b+"\t"+m+"\t"+n+"\t"+o+"\t"+k+"\t"+d+"\t"+e+"\t"+f+"\t"+g+"\t"+y+"\t"+z+"\t"+"RP_"+x)
            save_details.close()
            print("\n**Record stored into txt file.**")






 except AttributeError:

   pass
