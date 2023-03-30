
from typing import TextIO
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def get_details(url):
    global d
    print("Please wait. Program will work in background.\n")

    opts = Options()
    opts.headless = True
    opts.add_argument("user-agent=""")
    d = webdriver.Chrome("C:/chromedriver.exe", chrome_options=opts)
    d.get(url)

    time.sleep(5)

    try:
        val=d.find_elements_by_class_name("card-title")
        list=[]
        for i in range(1,len(val)+1):
            ele=d.find_element_by_xpath("//*[@id='product-listing-container']/form[2]/ul[1]/ul/li["+str(i)+"]/article/div/h4/a")
            part=ele.get_attribute("href")

            save_details: TextIO = open("ams__0933link.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x] + "\t" + list2[x] + "\t" + part )
            save_details.close()
            print("\n**Record stored into txt file.**")



    except:
        pass







if __name__ == '__main__':


     list2=['Carbon Sampling',
'ESS Core N One Disposable Soil Core Sampler',
'ESS Lock N Load Disposable Soil Core Sampler',
'Multi-Stage Soil Core Sampler',
'Soil Core Samplers',
'Soil Recovery Augers',
'Split Soil Core Samplers',
'Concrete Test Hammer Type N',
'Dual Mass DCP',
'Dynamic Cone Penetrometer',
'Eijkelkamp Soil Moisture Sensor Thetaprobe',
'Field Vane Shear Tester',
'Geo Tester Penetrometer',
'Infiltration Rings',
'Pocket Penetrometer',
'Shaw Portable Core Drill',
'Static Cone Penetrometer',
'Bait Station Install Kits',
'Universal Tools',
'Sentricon',
'Trelona',
'Bailers',
'Product Interface and Water Level Meters',
'Piezometer Groundwater Sampling Kit',
'Well Protection']
     listt =['https://www.ams-samplers.com/carbon-sampling/',
'https://www.ams-samplers.com/ess-core-n-one-disposable-soil-core-sampler/',
'https://www.ams-samplers.com/ess-lock-nload-disposable-soil-core-sampler/',
'https://www.ams-samplers.com/multi-stage-soil-core-sampler/',
'https://www.ams-samplers.com/hand-tooling/soil-core-samplers/',
'https://www.ams-samplers.com/soil-recovery-augers/',
'https://www.ams-samplers.com/core-split-core-samplers/split-soil-core-samplers/',
'https://www.ams-samplers.com/concrete-test-hammer-type-n/',
'https://www.ams-samplers.com/dual-mass-dcp/',
'https://www.ams-samplers.com/dynamic-cone-penetrometer/',
'https://www.ams-samplers.com/eijkelkamp-soil-moisture-sensor-thetaprobe/',
'https://www.ams-samplers.com/field-vane-shear-tester/',
'https://www.ams-samplers.com/geo-tester-penetrometer/',
'https://www.ams-samplers.com/infiltration-rings/',
'https://www.ams-samplers.com/pocket-penetrometer/',
'https://www.ams-samplers.com/shaw-portable-core-drill/',
'https://www.ams-samplers.com/static-cone-penetrometer/',
'https://www.ams-samplers.com/bait-station-install-kits/',
'https://www.ams-samplers.com/universal-tools/',
'https://www.ams-samplers.com/sentricon/',
'https://www.ams-samplers.com/trelona/',
'https://www.ams-samplers.com/bailers/',
'https://www.ams-samplers.com/product-interface-and-water-level-meters/',
'https://www.ams-samplers.com/piezometer-groundwater-sampling-kit/',
'https://www.ams-samplers.com/well-protection/']

     for x in range(0,10000):
         print(x)
         print(listt[x])
         get_details(listt[x])
