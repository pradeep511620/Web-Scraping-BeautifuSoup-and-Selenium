import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("sample test case started")

driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (1)//chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.raptorsupplies.com/')
driver.find_element_by_name("q").send_keys("PAC-CVR-C2")
time.sleep(1)
driver.find_element_by_id("searchBtn").send_keys(Keys.ENTER)

time.sleep(1)
driver.close()
print("sample test case successfully complete")



