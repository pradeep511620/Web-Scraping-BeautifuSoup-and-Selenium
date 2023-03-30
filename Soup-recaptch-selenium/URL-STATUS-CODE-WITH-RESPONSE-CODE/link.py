import bs4
import requests


url="https://www.raptorsupplies.com"
data=requests.get(url)
soup = bs4.BeautifulSoup(data.text, "html.parser")
print(soup.prettify())
for links in soup.find_all('a'):
    link=links.get('href')
    print(link)


