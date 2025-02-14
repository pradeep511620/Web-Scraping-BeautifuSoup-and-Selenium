import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/hp/Downloads/chromedriver_win32 (1)//chromedriver.exe')

url = ['https://www.raptorsupplies.co.uk/c/jaw-coupling-hubs',
       'https://www.raptorsupplies.co.uk/p/lovejoy/l-type-hubs-with-keyway-inch-bores',
       'https://www.raptorsupplies.co.uk/pd/ps-doors/513033',
       'https://www.raptorsupplies.co.uk/b/raxit',
       'https://www.raptorsupplies.co.uk/b/char-lynn',
       'https://www.raptorsupplies.co.uk/c/tap-bolts/ps-doors'
       ]
a = 0
for fetch in url:
    a += 1
    if a == 1:
        print('l3 rfq check start:')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="action"]/div/div').click()
        time.sleep(5)
        driver.find_element(By.ID, 'customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element(By.ID, 'customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element(By.ID, 'customer_number_sf').send_keys('8294966962')
        driver.find_element(By.ID, 'comment').send_keys('automated test by rahul')
        driver.find_element(By.XPATH, '//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element(By.XPATH, '//*[@id="show_success_msg_rfq"]').find_element(By.TAG_NAME, 'p')
        s = (demo_div.get_attribute('textContent'))
        print(s)
        print('----l3---')
    elif a == 2:
        print('mother rfq check start:')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="4671056"]').click()
        time.sleep(5)
        driver.find_element(By.ID, 'customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element(By.ID, 'customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element(By.ID, 'customer_number_sf').send_keys('8294966962')
        driver.find_element(By.ID, 'comment').send_keys('automated test by rahul')
        driver.find_element(By.XPATH, '//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element(By.XPATH, '//*[@id="show_success_msg_rfq"]').find_element(By.TAG_NAME, 'p')
        s = (demo_div.get_attribute('textContent'))
        print(s)
        time.sleep(2)
        print('---mother---')
    elif a == 3:
        print('product rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/section[3]/div/div[2]/div[2]/div[4]/div[3]/div[2]').click()
        time.sleep(5)
        driver.find_element(By.ID, 'customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element(By.ID, 'customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element(By.ID, 'customer_number_sf').send_keys('8294966962')
        driver.find_element(By.ID, 'comment').send_keys('automated test by rahul')
        driver.find_element(By.XPATH, '//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element(By.XPATH, '//*[@id="show_success_msg_rfq"]').find_element(By.TAG_NAME, 'p')
        s = (demo_div.get_attribute('textContent'))
        print(s)
        time.sleep(2)
        print("---product---")
    elif a == 4:
        print('brand raxit rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="4551030"]').click()
        time.sleep(5)
        driver.find_element(By.ID, 'customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element(By.ID, 'customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element(By.ID, 'customer_number_sf').send_keys('8294966962')
        driver.find_element(By.ID, 'comment').send_keys('automated test by rahul')
        driver.find_element(By.XPATH, '//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element(By.XPATH, '//*[@id="show_success_msg_rfq"]').find_element(By.TAG_NAME, 'p')
        s = (demo_div.get_attribute('textContent'))
        print(s)
        time.sleep(2)
        print('---raxit----')
    elif a == 5:
        print('char lynn rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="1102185"]').click()
        time.sleep(5)
        driver.find_element(By.ID, 'customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element(By.ID, 'customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element(By.ID, 'customer_number_sf').send_keys('8294966962')
        driver.find_element(By.ID, 'comment').send_keys('automated test by rahul')
        driver.find_element(By.XPATH, '//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element(By.XPATH, '//*[@id="show_success_msg_rfq"]').find_element(By.TAG_NAME, 'p')
        s = (demo_div.get_attribute('textContent'))
        print(s)
        time.sleep(2)
        print('---char-lynn---')
    elif a == 6:
        print('brand to l3 rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="action"]/div/div').click()
        time.sleep(5)
        driver.find_element(By.ID, 'customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element(By.ID, 'customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element(By.ID, 'customer_number_sf').send_keys('8294966962')
        driver.find_element(By.ID, 'comment').send_keys('automated test by rahul')
        driver.find_element(By.XPATH, '//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element(By.XPATH, '//*[@id="show_success_msg_rfq"]').find_element(By.TAG_NAME, 'p')
        s = (demo_div.get_attribute('textContent'))
        print(s)
        time.sleep(2)
        print('---brand-l3---')

    else:
        print('url not working')

driver.close()
print("driver successfully close")
