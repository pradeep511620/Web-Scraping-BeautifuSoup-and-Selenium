import undetected_chromedriver.v2 as uc
import time
from typing import TextIO
from selenium import webdriver


def get_details(url):
 options = webdriver.ChromeOptions()
 options.headless = True

 driver = uc.Chrome(options=options)
 driver.get(url)
 driver.delete_all_cookies()
 time.sleep(5)
 #print(driver.page_source)



 try:
  ele = driver.find_element_by_class_name("header-primary--pd").text
  ele1 = (ele if ele else "not given")
  print(ele1)

 except:
  pass
 try:
  ele2=driver.find_element_by_class_name("header-secondary--pd").text
  ele3 = (ele2 if ele2 else "not given")
  print(ele3)
 except:
  pass
 try:
  price=driver.find_element_by_class_name("PrceTxt").text
  pri = (price if price else "not given")
  print(pri)
 except:
  pass
 try:
  img=driver.find_element_by_class_name("ImageContainer_img__3pace").get_attribute("src")
  image= (img if img else "not given")
  print(image)


 except:
  pass
 try:
  leng=driver.find_elements_by_class_name("attr-cell--table")
  value=driver.find_elements_by_class_name("value-cell--table")

 except:
  pass
 try:

  for i in range(0,int(len(leng)/2)):

   att=leng[i].text
   print(att)
   val=value[i].text
   print(val)
   save_details: TextIO = open("mcmaster-hi111gh.txt", "a+", encoding="latin")
   save_details.write("\n" + url + "\t" + ele1+"\t"+ele3+"\t"+pri+"\t"+image+"\t"+att+"\t"+val)
   save_details.close()
   print("\n**Record stored into txt file.**")
 except:
   pass

if __name__ == '__main__':
    list=['https://www.mcmaster.com/4464K11']
    for x in range(0,len(list)):
     print(x)
     print(list[x])
     get_details(list[x])


