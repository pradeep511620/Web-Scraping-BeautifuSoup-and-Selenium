from bs4 import BeautifulSoup

import requests


url='https://www.raptorsupplies.com/pd/morse-drum/86'

page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
data=dict()
data1=dict()
b = 0
parData = soup.find("div", class_="productDetailsLeft half-collomn").find_all("table")[0]
rowData = parData.find_all("tr")
for row in rowData:
    colData = row.find_all("td")
    data[colData[0].text] = colData[1].text
print(data)
parData1 = soup.find("div", class_="productDetailsLeft half-collomn").find_all("table")[1]
rowData1 = parData1.find_all("tr")
for row1 in rowData1:
    colData1 = row1.find_all("td")
    data1[colData1[0].text] = colData1[1].text
print(data1)











