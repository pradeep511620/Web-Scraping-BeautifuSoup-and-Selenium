import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe',chrome_options=options)
url=["https://kr.raptorsupplies.com"]
for s in url:
    driver.get(s)
    for s in driver.find_elements_by_tag_name('script'):
        p = s.get_attribute('src')
        print(p)
        # s1 = p.find('gtag')
        # if s1 == -1:
        #     print(p)
        # else:
        #     print(s1)
    print('-------')
