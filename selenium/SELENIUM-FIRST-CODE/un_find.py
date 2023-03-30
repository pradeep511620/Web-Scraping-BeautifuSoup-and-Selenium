
#uacode='UA-183666890-1'
import time
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe')

url=['https://www.raptorsupplies.dk/b/3m']

for s in url:
    driver.get(s)
    time.sleep(2)
    p_element = driver.find_elements_by_tag_name('script')
    flag = 0
    for s in p_element:
        d = s.get_attribute('async')
        if(d=='true'):
            p=s.get_attribute('src')
            if(p=='https://www.googletagmanager.com/gtag/js?id=UA-183666890-1'):
                flag = 1
                break

    if(flag == 1):
        print("same")
    else:
        print("different")

