
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("sample test case started")

driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (1)//chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.raptorsupplies.co.uk/')
driver.find_element_by_xpath('/html/body/div[1]/header/div/section/header/div[4]/ul/li[4]/a').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_id("email").send_keys('sanjayarya@nextgenesolutions.com')
driver.find_element_by_id('pass').send_keys('Sanjay@123')
driver.find_element_by_id('send2').send_keys(Keys.ENTER)


#driver.find_element_by_id("searchBtn").send_keys(Keys.ENTER)


time.sleep(1)

print("sample test case successfully complete")




