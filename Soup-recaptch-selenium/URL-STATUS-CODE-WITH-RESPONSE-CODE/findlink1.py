import httplib2
from bs4 import BeautifulSoup
import requests
http = httplib2.Http()
url="https://www.raptorsupplies.com/p/morse-drum/below-hook-drum-lifter"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'lxml')
with open('urlfind.csv','w') as f:
    for links in soup.find_all("link"):
        link = links.get('href')
        print(link)
        f.write(link+'\n')