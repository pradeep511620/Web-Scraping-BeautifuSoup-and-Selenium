
#uacode='UA-183666890-1'
import time
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe')

url=['https://www.raptorsupplies.com/l1/?gclid=1']
for s in url:
    driver.get(s)
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        s=(elem.get_attribute("href"))
        print(s.endswith('?gclid=1'))
