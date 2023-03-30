import time
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe')
url=["https://www.raptorsupplies.co.uk/l1/material-handling",'https://www.raptorsupplies.com/l1/material-handling',"https://www.raptorsupplies.com.sg/l1/material-handling"]
for s in url:
    driver.get(s)
    time.sleep(2)
    p_element = driver.find_elements_by_tag_name('script')
    for s in p_element:
        p=s.get_attribute('src')
        time.sleep(2)
        print(p)
    print('-------')