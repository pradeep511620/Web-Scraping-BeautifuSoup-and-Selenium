import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe')
# driver.get('https://www.raptorsupplies.co.uk/pd/morse-drum/2-5154-a')
url = ['https://www.raptorsupplies.co.uk/c/jaw-coupling-hubs',
       'https://www.raptorsupplies.co.uk/p/lovejoy/l-type-hubs-with-keyway-inch-bores',
       'https://www.raptorsupplies.co.uk/pd/morse-drum/2-5154-a',
       'https://www.raptorsupplies.co.uk/b/raxit',
       'https://www.raptorsupplies.co.uk/b/dodge-bearings'
       ]
a = 0
for fetch in url:
    a += 1
    if a == 1:
        print('l3 rfq check start:')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="action"]/div/div').click()
        time.sleep(5)
        driver.find_element_by_id('customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element_by_id('customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element_by_id('customer_number_sf').send_keys('8294966962')
        driver.find_element_by_id('comment').send_keys('automated test by rahul')
        driver.find_element_by_xpath('//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element_by_xpath('//*[@id="show_success_msg_rfq"]').find_element_by_tag_name('p')
        print(demo_div.get_attribute('textContent'))
        print('----l3---')
    elif a == 2:
        print('mother rfq check start:')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="4671056"]').click()
        time.sleep(5)
        driver.find_element_by_id('customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element_by_id('customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element_by_id('customer_number_sf').send_keys('8294966962')
        driver.find_element_by_id('comment').send_keys('automated test by rahul')
        driver.find_element_by_xpath('//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element_by_xpath('//*[@id="show_success_msg_rfq"]').find_element_by_tag_name('p')
        print(demo_div.get_attribute('textContent'))
        time.sleep(2)
        print('---mother---')
    elif a == 3:
        print('product rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/section[3]/div/div[2]/div[2]/div[4]/div[2]/div[2]').click()
        time.sleep(5)
        driver.find_element_by_id('customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element_by_id('customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element_by_id('customer_number_sf').send_keys('8294966962')
        driver.find_element_by_id('comment').send_keys('automated test by rahul')
        driver.find_element_by_xpath('//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element_by_xpath('//*[@id="show_success_msg_rfq"]').find_element_by_tag_name('p')
        print(demo_div.get_attribute('textContent'))
        time.sleep(2)
        print("---product---")
    elif a == 4:
        print('brand raxit rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="4551030"]').click()
        time.sleep(5)
        driver.find_element_by_id('customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element_by_id('customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element_by_id('customer_number_sf').send_keys('8294966962')
        driver.find_element_by_id('comment').send_keys('automated test by rahul')
        driver.find_element_by_xpath('//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element_by_xpath('//*[@id="show_success_msg_rfq"]').find_element_by_tag_name('p')
        print(demo_div.get_attribute('textContent'))
        time.sleep(2)
        print('---raxit----')
    elif a == 5:
        print('dodge bearing rfq check start')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="1041233"]').click()
        time.sleep(5)
        driver.find_element_by_id('customer_name_sf').send_keys('Rahul Kumar Singh')
        driver.find_element_by_id('customer_email_sf').send_keys('rksingh@nextgenesolutions.com')
        driver.find_element_by_id('customer_number_sf').send_keys('8294966962')
        driver.find_element_by_id('comment').send_keys('automated test by rahul')
        driver.find_element_by_xpath('//*[@id="shipping-form"]/div/div[3]/button').click()
        time.sleep(3)
        demo_div = driver.find_element_by_xpath('//*[@id="show_success_msg_rfq"]').find_element_by_tag_name('p')
        print(demo_div.get_attribute('textContent'))
        time.sleep(2)
        print('---dodge-bearing---')

    else:
        print('url not working')

driver.close()
print("driver successfully close")








