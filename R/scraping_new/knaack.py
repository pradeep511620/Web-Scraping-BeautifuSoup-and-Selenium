import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.remote.webelement


def get_details(url):
    global d
    #current_date: object = datetime.now()
    #save_details: TextIO = open("Destacoo.txt", "a+")
    #save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
    #save_details.close()
    #print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

    print("Please wait. Program will work in background.\n")

    opts = Options()
    opts.headless = True
    opts.add_argument("user-agent=""")
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.get(url)
    time.sleep(5)



    try:
                ele=d.find_element_by_xpath("//*[@id='productTitle']/span").text
                print(ele)

    except:
                pass
    try:
        image=d.find_element_by_xpath("//*[@id='zooomr']").get_attribute("href")
        print(image)
    except:
        pass
    try:
        bread1=d.find_element_by_xpath("//*[@id='details-app']/div/div[1]/div/span/a[1]").text
        print(bread1)
    except:
        pass
    try:
        bread2=d.find_element_by_xpath("//*[@id='details-app']/div/div[1]/div/span/a[2]").text
        print(bread2)
    except:
        pass
    try:
        bread3 = d.find_element_by_xpath("//*[@id='details-app']/div/div[1]/div/span/a[3]").text
        print(bread3)
    except:
        pass
    try:
        vl=d.find_elements_by_class_name("video-icon")
        list=[]
        for v in vl:
            list.append(v.get_attribute("href"))
        print(list)
    except:
        pass
    try:
        pdf=d.find_elements_by_class_name("fa-file-pdf-o")

        list2=[]
        for p in range(2,len(pdf)+2):
            wow=d.find_element_by_xpath("//*[@id='resources']/ul/li["+str(p)+"]/a")
            list2.append(wow.get_attribute("href"))
        print(list2)
    except:
        pass
    try:
        img=d.find_elements_by_class_name("product-accessories__list-item-inner")
        print(len(img))
        list3=[]
        for m in range(1,len(img)+1):
            hello=d.find_element_by_xpath("//*[@id='accessories']/div/div/div/div/div/div["+str(m)+"]/div/a/div[2]/span/span")
            list3.append(hello.text)
        print(list3)
    except:
        pass
    try:
        list4=[]
        for i in range(6,16):
            list4.append(d.find_element_by_xpath("//*[@id='details-app']/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div["+str(i)+"]/div/a/img").get_attribute("src"))
        print(list4)
    except:
        pass



    try:
                elemwnt=d.find_element_by_class_name("product-expandable-panel__toggle")
                elemwnt.click()
                tabl=d.find_elements_by_tag_name("td")
                for tab in range(1,len(tabl)+1):
                    if tab % 2 != 0:
                        att=tabl[tab-1].text
                        print(att)
                        val=tabl[tab].text
                        print(val)
                        save_details: TextIO = open("knaack-done1.txt", "a+", encoding="utf-8")
                        save_details.write("\n"+listtt[x]+"\t"+ele+"\t"+image+"\t"+bread1+" > "+bread2+" > "+bread3+" > "+ele+"\t"+"  ,  ".join(list)+"\t"+"  ,  ".join(list2)+"\t"+"  ,  ".join(list3)+"\t"+"  ,  ".join(list4)+"\t"+"rp_"+att+"\t"+"rp_"+val )
                        save_details.close()
                        print("\n**Record stored into txt file.**")


    except:
                pass





if __name__ == '__main__':

     listtt =['https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/89',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-01',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/PT-01',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-SK-01',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/4824',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/4830',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-03',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/42',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/109',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/60',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/36',
'https://www.knaack.com/products/jobsite-storage-equipment/hand-held-boxes/SpecialtyChestSeries/30',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/CastersSeries/695',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/FieldStationSeries/119-02',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/90',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/32',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/2472',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/44',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/79',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/91',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/112',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-02',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/69',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/100',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/4830-D',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/89-D',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/79-D',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/111',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/49',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/129',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/FieldStationSeries/118-M',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-05',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/FieldStationSeries/118-01',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/99',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/ChestSeries/1010',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/40',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-MT',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-SK',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/1020',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/63',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/33',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/1000',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/R-72',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/59',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/47',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-04',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-06',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/WorkStationSeries/CA-07',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/62',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/58',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/45',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/100-MT',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/38',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/RollingSeries/35',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/89-H',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/89-DH',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/129-MT',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-SK-02',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-SK-03',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-SK-03C',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/CabinetSeries/139-SK-03S',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/79-H',
'https://www.knaack.com/products/jobsite-storage-solution/jobsite-boxes/PianoSeries/79-DH',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/SKDoorSeries/SKC-01L',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/SKDoorSeries/SKC-01R',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/SKDoorSeries/SKS-01L',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/SKDoorSeries/SKS-01R',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/SKDoorSeries/SKV-01L',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/SKDoorSeries/SKV-01R',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/ShelfDoorSeries/492',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/ShelfDoorSeries/494',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/ShelfDoorSeries/493',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/CastersSeries/516',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/CastersSeries/497',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/CastersSeries/600',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/CastersSeries/505',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/CastersSeries/495',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/DrawersSeries/471-3',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/TraySeries/31',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/DrawersSeries/472-3',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/DrawersSeries/476-3',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/DrawersSeries/477-3',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/TraySeries/41',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/TraySeries/21',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/TraySeries/51',
'https://www.knaack.com/products/jobsite-storage-equipment/accessories/DrawersSeries/474-3',
'https://www.knaack.com/products/jobsite-storage-equipment/hand-held-boxes/SpecialtyChestSeries/28',
'https://www.knaack.com/products/jobsite-storage-equipment/hand-held-boxes/ToolBoxSeries/743',
'https://www.knaack.com/products/jobsite-storage-equipment/hand-held-boxes/ToolBoxSeries/741']
     for x in range(0,10000):
         print(x)
         print(listtt[x])
         get_details(listtt[x])
