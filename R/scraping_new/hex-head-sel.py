from selenium import webdriver
from selenium.webdriver.chrome.options import Options


myresult=['https://www.grainger.com/search/fasteners/bolts/hex-head-bolts/standard-hex-head-cap-screws?filters=webParentSkuKey&webParentSkuKey=WP13467676&gwwRemoveElement=true']

for row in myresult:
 print(row)
 opts = Options()
 #opts.headless = True
 d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)

 d.get(row)

 try:
     trs=d.find_elements_by_class_name("_3OJ8zd")
     print(len(trs))





 except AttributeError:

   pass
