from bs4 import BeautifulSoup
import requests
url="https://www.grainger.com/category/abrasives/abrasive-blasting?analytics=nav"

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'lxml')

for disc in soup.find('p',class_="view-more__content"):
    print(disc)

