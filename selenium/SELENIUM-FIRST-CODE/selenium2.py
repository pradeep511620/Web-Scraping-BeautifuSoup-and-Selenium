
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("sample test case started")

driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (1)//chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.raptorsupplies.com/')
driver.find_element_by_name("q").send_keys("PAC-CVR-C2")
time.sleep(1)
p=float(70.84)
driver.find_element_by_id("searchBtn").send_keys(Keys.ENTER)
d=driver.find_element_by_xpath("//*[@id='product_addtocart_form']/div[1]/div/span[2]")
a=0
for i in driver.find_elements_by_css_selector("#productalldetailtext > div > div.col-sm-6.productdetailleft"):

    print(i.text)

    pr=float(d.text)
    if(p==pr):
        print("same")
    else:
        print("not same")


time.sleep(1)
driver.close()
print("sample test case successfully complete")




