import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe',chrome_options=options)
url = 'https://www.raptorsupplies.com/c/angular-contact-bearings'
driver.get(url)
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

# for x in soup.find('div',class_='filterGridRight').find_all('a'):
#     s = x.get('href')
a = 0
max = 0
if driver.find_elements_by_id("loadPage"):
    print('test')
    time.sleep(5)
    for links in driver.find_elements_by_xpath('//*[@id="loadPage"]/a[1]'):
        time.sleep(5)
        # li2 = links.get("href")
        print(links.text)
        # tmp = int(li2.split('=')[1])
        # if (max < tmp):
        #     max = tmp
        #     print(max)

    # for x in range(2, max + 1):
    #     url = url1
    #     url = url + "?page=" + str(x)
    #
    #     page = requests.get(url)
    #     soup = BeautifulSoup(page.content, "lxml")
    #
    #     for link in soup.find('div', class_="filterGridRight").find_all('a'):
    #         li = (link.get("href"))
    #         sql = ("INSERT INTO brandl3_url (brand_url,l3_url) VALUES (%s, %s)")
    #         val = (brand_url, li,)
    #         cur.execute(sql, val)
    #         mydb.commit()
    #         print(cur.rowcount, "record(s) affected")
else:
    print("pagination not found")
