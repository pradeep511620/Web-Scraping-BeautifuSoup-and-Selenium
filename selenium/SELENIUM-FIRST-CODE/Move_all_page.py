import time
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (3)//chromedriver.exe')
driver.maximize_window()
driver.get('https://stage.raptorsupplies.com/')
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# s=driver.find_element_by_link_text('Abrasives')
# action = ActionChains(driver)
# action.click(on_element = s)
# action.perform()

time.sleep(2)
# search = driver.find_element_by_id("search").send_keys('Abrasives')
# driver.find_element_by_id("searchBtn").send_keys(Keys.ENTER)
#search.send_keys(search + Keys.RETURN)
try:
    d=driver.find_elements_by_class_name('home_top_catalogue')
    a=0
    for link in d:
        a+=1
        time.sleep(5)
        l1=(link.get_attribute('href'))


        if(a==1):
            #time.sleep(5)
            driver.get(l1)
            time.sleep(2)
            d1=driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div/section[3]/div/div/div[1]/div/h3/a')
            d2=(d1.get_attribute('href'))
            driver.get(d2)
            #time.sleep(3)
            c=driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div/section[5]/div/div/div[2]/div[1]/ul/li[1]/figcaption/a')
            c1=(c.get_attribute('href'))
            driver.get(c1)
            #time.sleep(3)
            m=driver.find_element_by_xpath('//*[@id="defaultView"]/section[1]/div[1]/div[1]/h2/a')
            m1=(m.get_attribute('href'))
            driver.get(m1)

            pd=driver.find_element_by_id('link_row1')
            pd1=(pd.get_attribute('value'))
            driver.get(pd1)
            # b=0
            # for links in d1:
            #     b+=1
            #     l2=(links.get_attribute('href'))
            # if(b==1):
            #     driver.get(l2)
            

except:
    pass

#driver.close()
