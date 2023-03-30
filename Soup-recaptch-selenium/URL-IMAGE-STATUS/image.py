from bs4 import BeautifulSoup
import requests

url="https://www.grainger.com/category"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page=requests.get(url,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")
#test=(soup.find_all("div",class_="prdtls_wrp"),soup.find("a"))
with open('graingerimg.csv','w') as f:
    for links1 in soup.find_all("img"):
        link1=links1.get('src')
        print(link1)
        f.write("https:"+link1+"\n")
