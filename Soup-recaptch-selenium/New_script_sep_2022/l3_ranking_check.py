from bs4 import BeautifulSoup
import mysql.connector
import requests
import csv

file = open('C:\\Users\Rahul\Documents\l3_header_raptor.csv','r')
csvreader = csv.reader(file)
b = 0
c = []
for row in csvreader:
    x = row[8]

    if '/c/circular-chart-recorders' in x:
        # print(row)
        page = requests.get(x)
        soup = BeautifulSoup(page.content, "html.parser")
        for y in soup.find('div', class_='filterGridRight').find_all('h2', class_='category_l2_title')[0:7]:
            b += 1
            c.append(y.text)
            # exit()
print(c)
#

# for x in soup.find('div', class_='filterGridRight').find_all('h2', class_='category_l2_title')[0:7]:
#     b += 1
#     c.append(x.text)
#
# for i, y in zip(c, a):
#     j = i.strip('\n')
#     if j == y:
#         print("header same", j)
#     else:
#         print("header not same", j)
