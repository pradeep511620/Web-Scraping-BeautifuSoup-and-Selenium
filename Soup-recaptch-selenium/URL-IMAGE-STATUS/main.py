import bs4
import requests
import re
url="https://www.raptorsupplies.com/contact"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
#print(soup.prettify())
for title in soup.find('title'):
    print(title)
    print(len(title))
for h1 in soup.find('h1'):
    print(h1)
