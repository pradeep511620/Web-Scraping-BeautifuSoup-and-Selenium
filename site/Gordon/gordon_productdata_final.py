import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from typing import TextIO

myresults=[
'https://www.gordonelectricsupply.com/p/Appleton-Lr58-1-1-2-Conduit-Body/5742662?ID=/Appleton-Electric/mfr-1ICG',
'https://www.gordonelectricsupply.com/p/Appleton-Blll8Wgwnbu-Bll-19Klm-Ww-Cg-Wd-Bu/6123159?ID=/Appleton-Electric/mfr-1ICG',
'https://www.gordonelectricsupply.com/p/Appleton-Kpcl2510J248L-Mercmaster-Iii/6111839?ID=/Appleton-Electric/mfr-1ICG']
# 'https://www.gordonelectricsupply.com/p/Appleton-Mledna172P1Bh-Mm-Led-175W-Type-1-Bh-3-4In-Pen/6122059?ID=/Appleton-Electric/mfr-1ICG',
# 'https://www.gordonelectricsupply.com/p/Appleton-Ibhll3Cgnnbuf-Ibhl-38Klm-Cw-Cg-Nar-Bu-F/6123214?ID=/Appleton-Electric/mfr-1ICG',
# 'https://www.gordonelectricsupply.com/p/Appleton-Kpsl10150J5Mte-Mmiii-St25-Hps-100W/6117869?ID=/Appleton-Electric/mfr-1ICG',
# 'https://www.gordonelectricsupply.com/p/Appleton-Kpap1710G348-Mmiii-With-8-Globe/6121261?ID=/Appleton-Electric/mfr-1ICG']

for result in myresults:
    try:
        url = result
        opts = Options()
        opts.headless = True
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe", chrome_options=opts)
        driver.get(url)
        reqs = requests.get(url)
        # soup = BeautifulSoup(reqs.text, 'lxml')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.maximize_window()
        time.sleep(3)
        print("###########Title############")
        s = soup.find('h1')
        TITLE = s.text.strip()
        print(TITLE)
        print("###########part no ############")
        for s in driver.find_elements(By.XPATH, '//*[@id="product_content"]/div[1]/form/div[2]/p[3]'):
            part = s.text.split(': ')[1].strip()
            print(part)
        print("###########Breadcrumb############")
        for s in soup.find_all('div', {'id': 'breadcrumb'}):
            breadcrumb = s.text.strip()
            print(breadcrumb)
        print("###########Price############")
        for s in soup.find_all('div', {'class': 'price-box'}):
            # print(s.text)
            price = s.text.split('$')[1].split('/')[0].strip()
            print(price)
        print("###########Image############")
        for s in soup.find_all('a', {'id': 'big-image'}):
            image = s['href']
            print(image)
        print("###########Resources############")
        resources = soup.find('div', {'id': 'resourcetable'}).find('ul').find_all('li')
        for r in resources:
            re = r.find('a')
            print(re['href'])
        time.sleep(3)
        i = 0
        prod = soup.find_all("tr")
        print(prod)
        # i = 0
        #
        # while i < len(prod):
        #     z = (prod[i].text.strip() if prod else "not given")
        #     print(z)
    except AttributeError:
        pass
driver.close()