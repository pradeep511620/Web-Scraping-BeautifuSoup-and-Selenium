from bs4 import BeautifulSoup
import mysql.connector
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe',chrome_options=options)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="neW_stage_data"
)
cur = mydb.cursor()
cur.execute("SELECT mother_url,header from `mother_url_indexer` where id=232 ")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    header = fetch[1]
    mother_url = "https://www.raptorsupplies.com/"+url
    driver.get(mother_url)
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, "html.parser")
    s = 0
    a = []
    data = dict()
    for pd in soup.find('div', {"id": "parent_"}).find_all('th')[:-1]:
        s += 1
        p = pd.text
        s1 = p.split('\n')
        j = " ".join(s1)
        data[j] = dict()
        count = 0
        for optn in soup.find('div', {"id": "parent_"}).find_all('tr')[1:]:
            count += 1
            p1 = optn.text
            p2 = p1.split('\n')
            j1 = "".join(p2)
            data[j] = count
    print(data)
    for l in driver.find_elements_by_id('num_of_pro'):
        print(l.text)







