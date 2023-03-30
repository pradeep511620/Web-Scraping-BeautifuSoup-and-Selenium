import requests
from bs4 import BeautifulSoup
import html

url='https://stage.raptorsupplies.com/c/fasteners/c3/lock-washers'

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

for x in soup.find('div',{"id":"description"}).find_all('p'):
    des = str(x)[3:-4]
    print(des)