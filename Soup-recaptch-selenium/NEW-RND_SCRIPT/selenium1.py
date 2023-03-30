import time
from selenium import webdriver

driver = webdriver.Chrome('C://Users//ashish//Downloads//chromedriver_win32 (1)//chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://b2b.raptorsupplies.com/b/strong-hold');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Service Counters')
lnks=driver.find_elements_by_tag_name("a")
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk.get_attribute('href'))
search_box.submit()

time.sleep(5) # Let the user actually see something!
driver.quit()