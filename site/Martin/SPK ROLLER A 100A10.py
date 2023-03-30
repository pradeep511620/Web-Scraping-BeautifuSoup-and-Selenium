import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe")
url = 'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=100A10&Website_CategoryName=Sprockets&Website_Code=SP1'
driver.get(url)
driver.maximize_window()

a=0
for e in driver.find_element(By.TAG_NAME,'div').find_elements( by = By.TAG_NAME, value = 'div'):
    a += 1
    if a == 2:
        print(e.text)
print('\n\n\n')
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Misc Info").click()
b = 0
for f in driver.find_element(By.TAG_NAME,'div').find_elements( by = By.TAG_NAME, value = 'div'):
    b += 1
    if b ==2:
        print(f.text)
print('\n\n\n')
time.sleep(3)


# print("1")
# for e in driver.find_elements(By.CLASS_NAME,'Head'):
#     print(e.text)
# time.sleep(3)
# print("2")
# a = 0
# for e in driver.find_elements(By.TAG_NAME,'Span'):
#     a += 1
#     if a in range(2,4):
#         print(e.text)
# print("3")


