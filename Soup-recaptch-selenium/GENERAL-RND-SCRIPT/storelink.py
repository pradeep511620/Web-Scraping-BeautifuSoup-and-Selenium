from bs4 import BeautifulSoup
import requests
import csv
url="https://www.grainger.com/category/abrasives?analytics=nav"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'lxml')
url1 = soup.find('a',class_="route categories__link").get("href")
name = soup.find_all("p",class_="categories__category-name")

dataset = [(x, y.text) for x,y in zip(url1,name)]

with open("output.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in dataset[:150]:
        writer.writerow(data)