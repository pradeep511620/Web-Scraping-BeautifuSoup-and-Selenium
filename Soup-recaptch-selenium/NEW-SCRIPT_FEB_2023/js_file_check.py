import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:/Users/hp/Downloads//chromedriver.exe',chrome_options=options)

url = ['https://ro.raptorsupplies.com/pd/merit/08834154465']
a = 0
js = []
for fetch in url:
    a += 1
    if a == 1:
        driver.get(fetch)
        s = driver.find_elements(By.TAG_NAME, 'script')
        for x in s:
            y = x.get_attribute('src')
            if "https://cdn.raptorsupplies.com.sg" not in y:
                j = str(y)
                print(j)