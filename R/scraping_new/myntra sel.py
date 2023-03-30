import time

import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



myresult=[

'https://www.myntra.com/10639344',
'https://www.myntra.com/10639350',
'https://www.myntra.com/10718328',
'https://www.myntra.com/10718330',
'https://www.myntra.com/10718334',
'https://www.myntra.com/10718340',
'https://www.myntra.com/10718344',
'https://www.myntra.com/10718354',
'https://www.myntra.com/10718446',
'https://www.myntra.com/10718456',
'https://www.myntra.com/10718480',
'https://www.myntra.com/10846544',
'https://www.myntra.com/11240480',
'https://www.myntra.com/11240486',
'https://www.myntra.com/11243142',
'https://www.myntra.com/11243148',
'https://www.myntra.com/11243150',
'https://www.myntra.com/11243154',
'https://www.myntra.com/11243156',
'https://www.myntra.com/11243162',
'https://www.myntra.com/11243164',
'https://www.myntra.com/11243166',
'https://www.myntra.com/11243174',
'https://www.myntra.com/11243176',
'https://www.myntra.com/11243178',
'https://www.myntra.com/11243182',
'https://www.myntra.com/11243184',
'https://www.myntra.com/11278412',
'https://www.myntra.com/11359314',
'https://www.myntra.com/11395656',
'https://www.myntra.com/11395658',
'https://www.myntra.com/11395664',
'https://www.myntra.com/11395666',
'https://www.myntra.com/11395668',
'https://www.myntra.com/11395676',
'https://www.myntra.com/11395678',
'https://www.myntra.com/11395684',
'https://www.myntra.com/11395688',
'https://www.myntra.com/11395704',
'https://www.myntra.com/11395710',
'https://www.myntra.com/11395716',
'https://www.myntra.com/11395720',
'https://www.myntra.com/11563980',
'https://www.myntra.com/11563982',
'https://www.myntra.com/11563986',
'https://www.myntra.com/11563992',
'https://www.myntra.com/11563996',
'https://www.myntra.com/11563998',
'https://www.myntra.com/11564000',
'https://www.myntra.com/11564014',
'https://www.myntra.com/11564020',
'https://www.myntra.com/11564022',
'https://www.myntra.com/11564026',
'https://www.myntra.com/11564030',
'https://www.myntra.com/11564032',
'https://www.myntra.com/11564036',
'https://www.myntra.com/11564038',
'https://www.myntra.com/11564042',
'https://www.myntra.com/11564046',
'https://www.myntra.com/11564054',
'https://www.myntra.com/11564058',
'https://www.myntra.com/11564060',
'https://www.myntra.com/11564064',
'https://www.myntra.com/11564072',
'https://www.myntra.com/11564074',
'https://www.myntra.com/11564078',
'https://www.myntra.com/11564080',
'https://www.myntra.com/11655924']

for row in myresult:
 print(row)
 opts = Options()
 opts.headless = True
 opts.add_argument("user-agent=""")
 d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
 d.get(row)
 CLI=d.find_element_by_xpath("//*[@id='mountRoot']/div/div/div/main/div[2]/div[1]/div[6]")
 CLI.click()
 time.sleep(3)
 data=d.find_element_by_class_name("desktop-image-zoom-primary-image").get_attribute("src")

 print(data)
 save_details: TextIO = open("myntra-shghjm.txt", "a+", encoding="utf-8")
 save_details.write("\n"+row+"\t"+data)
 save_details.close()
 print("\n**Record stored into txt file.**")





