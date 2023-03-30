import re
import bs4
import requests
url="https://www.raptorsupplies.com/en-gb/merit/08834154463"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
#get price
print(soup.find('div',class_='realprice').find('span',class_="pricetext").text)
#get heading
for heading in soup.find_all('h1'):
    print("\n"+heading.text)
#Check if the string has any digits:
txt="MERIT 08834154463 Bore Polisher Extension Mandrel"
x = re.findall("[0-9]", txt)
print(x)

#find detail of model
for detail in soup.find('div',class_="b_detail"):
    print("\n"+detail.text)
#find product Specification
#print(soup.find("table",class_="table").find_all("strong").find_all("td"))
for product in soup.find('div',class_="prodcutspec"):

   print("\n"+product.text)

#print(soup.find('div',class_='productshing').find('table',class_="table").text)
#find shipping specification
for shipping in soup.find('div',class_="productshing"):
    print("\n"+shipping.text)
#find part number
for partn in soup.find("div",class_="mpndropdown"):
    print(partn.text)
#get all link
for links in soup.find_all("link"):
    link = links.get('href')
    print(link)





