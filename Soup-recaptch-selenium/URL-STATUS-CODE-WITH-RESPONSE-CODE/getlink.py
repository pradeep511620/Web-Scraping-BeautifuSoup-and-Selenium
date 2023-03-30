import bs4
import requests
url="htools/hand-toolsttps://www.grainger.com/category/"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,"html.parser")
"""for links in soup.find_all("src"):
    link=links.get("href")
    print(link)
"""
"""for links in soup.find("a",class_="route categories__link"):
    link=links.get("href")
    print(link.text)"""
print(soup.find('p',class_="view-more__content").text)