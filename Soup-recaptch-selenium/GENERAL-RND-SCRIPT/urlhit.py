from bs4 import BeautifulSoup
import requests
import httplib2

http = httplib2.Http()
url="https://www.grainger.com/category/abrasives?analytics=nav"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'lxml')
with open('urlstore.csv','w') as f:
    for links in soup.find_all('a',class_="route categories__link"):
        link = links.get('href')
        print("https://www.grainger.com"+link)
        f.write("https://www.grainger.com"+link+'\n')






