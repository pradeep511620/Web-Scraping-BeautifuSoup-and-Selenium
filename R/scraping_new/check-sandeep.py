import undetected_chromedriver.v2 as uc
import time
from typing import TextIO
def get_details(url):
 driver = uc.Chrome()
 driver.get(url)

 try:
  time.sleep(10)
 except:
  pass


if __name__ == '__main__':
    list=['https://parts.fleetpride.com/parts/ccrz__CCPage?pageKey=coveo&CoveoStorefront=parts#q=grote&sort=relevancy']
    for i in range(0,len(list)):
     print(i)
     print(list[i])
     get_details(list[i])