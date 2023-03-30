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
        sku=d.find_element_by_xpath("//*[@id='product-page-with-sidenav']/div[2]/div[1]/section/div/div/dl/dd[1]").text
        print(sku)
    except:
        pass


    try:
        for i in range(1, 20):
            val=d.find_element_by_xpath("//*[@id='tab-description']/ul[1]/li["+str(i)+"]").text

            save_details: TextIO = open("rag-ams2.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x]  +"\t"+ sku+"\t" + val )
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        pass


    try:
        for j in range(1, 20):
            val=d.find_element_by_xpath("//*[@id='tab-description']/ul[2]/li["+str(j)+"]").text

            save_details: TextIO = open("rag-ams2.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x]+"\t"+ sku + "\t" + val )
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        pass









if __name__ == '__main__':


     listt =['https://www.ams-samplers.com/2-x-8-plastic-liner/',
'https://www.ams-samplers.com/2-x-10-plastic-liner/',
'https://www.ams-samplers.com/3-x-10-sst-liner/',
'https://www.ams-samplers.com/3-x-12-sst-liner/',
'https://www.ams-samplers.com/2-x-8-sst-liner/',
'https://www.ams-samplers.com/2-x-10-sst-liner/',
'https://www.ams-samplers.com/1-x-6-plastic-liner/',
'https://www.ams-samplers.com/1-x-12-plastic-liner/',
'https://www.ams-samplers.com/1-x-24-plastic-liner/',
'https://www.ams-samplers.com/3-4-x-6-plastic-liner/',
'https://www.ams-samplers.com/3-4-x-12-plastic-liner/',
'https://www.ams-samplers.com/3-4-x-24-plastic-liner/',
'https://www.ams-samplers.com/1-x-12-sst-liner/',
'https://www.ams-samplers.com/1-x-24-sst-liner/',
'https://www.ams-samplers.com/3-4-x-6-sst-liner/',
'https://www.ams-samplers.com/3-4-x-12-sst-liner/',
'https://www.ams-samplers.com/3-4-x-24-sst-liner/',
'https://www.ams-samplers.com/2-x-24-plastic-liner/',
'https://www.ams-samplers.com/1-2-x-36-plastic-liner/',
'https://www.ams-samplers.com/1-1-2-x-2-pvc-liner/',
'https://www.ams-samplers.com/1-1-2-x-5-pvc-liner-box-of-48/',
'https://www.ams-samplers.com/1-1-2-x-2-pvc-liner-sold-per-case-of-96/',
'https://www.ams-samplers.com/2-x-48-plastic-liner/',
'https://www.ams-samplers.com/2-1-2-x-12-plastic-liner/',
'https://www.ams-samplers.com/2-x-36-plastic-liner/',
'https://www.ams-samplers.com/1-3-8-x-12-plastic-liner/',
'https://www.ams-samplers.com/1-3-8-x-6-plastic-liner/',
'https://www.ams-samplers.com/2-1-2-x-6-plastic-liner/',
'https://www.ams-samplers.com/1-1-2-x-12-plastic-liner/',
'https://www.ams-samplers.com/1-4-plastic-end-cap/',
'https://www.ams-samplers.com/3-plastic-end-cap/',
'https://www.ams-samplers.com/2-plastic-end-cap/',
'https://www.ams-samplers.com/1-3-8-plastic-end-caps/',
'https://www.ams-samplers.com/1-plastic-end-caps/',
'https://www.ams-samplers.com/3-4-plastic-end-caps/',
'https://www.ams-samplers.com/1-1-2-plastic-end-cap/',
'https://www.ams-samplers.com/finger-ring-for-qc/',
'https://www.ams-samplers.com/repair-kit-for-qc/',
'https://www.ams-samplers.com/female-tee-jack-adapter-3-4-thread/',
'https://www.ams-samplers.com/big-foot-removal-jack/',
'https://www.ams-samplers.com/gp-2-pull-cap-for-big-foot-jack/',
'https://www.ams-samplers.com/jackjaw-u-pickett-sign-post-grounding-rod-extractor/',
'https://www.ams-samplers.com/jackjaw-tent-stake-extractor-29-3-16-1/',
'https://www.ams-samplers.com/jackjaw-tent-stake-ext-adj-base-fold-handle-ext-3-4-1-1-4/',
'https://www.ams-samplers.com/jackjaw-505-super-round-sign-post-extractor-handle-extension-grip-width-2-1-4-3/',
'https://www.ams-samplers.com/tee-jack-adapter/',
'https://www.ams-samplers.com/removal-jack/',
'https://www.ams-samplers.com/1-plated-heavy-duty-replaceable-tip/',
'https://www.ams-samplers.com/1-1-4-plated-replacement-tip-for-soil-recovery-probe/',
'https://www.ams-samplers.com/2-1-4-sludge-valved-core-tip/',
'https://www.ams-samplers.com/2-1-4-sludge-valved-auger-tip/',
'https://www.ams-samplers.com/3-1-4-sludge-valved-auger-tip/',
'https://www.ams-samplers.com/3-1-4-sludge-valved-core-tip/',
'https://www.ams-samplers.com/sludge-auger-tip-no-valve-3-1-4/',
'https://www.ams-samplers.com/sludge-core-tip-no-valve-3-1-4/',
'https://www.ams-samplers.com/sludge-auger-tip-no-valve-2-1-4/',
'https://www.ams-samplers.com/sludge-core-tip-no-valve-2-1-4/',
'https://www.ams-samplers.com/hollowstem-replacement-tip/',
'https://www.ams-samplers.com/2-flighted-auger-tip-sst/',
'https://www.ams-samplers.com/2-5-8-carbide-tip/',
'https://www.ams-samplers.com/2-5-8-hard-surfaced-tip/',
'https://www.ams-samplers.com/2-carbide-tip-1/',
'https://www.ams-samplers.com/2-hard-surfaced-tip/',
'https://www.ams-samplers.com/1-7-8-tip-only-flighted-aug/',
'https://www.ams-samplers.com/1-1-4-serrated-rep-tip/',
'https://www.ams-samplers.com/1-serrated-rep-tip/',
'https://www.ams-samplers.com/1-1-4-clay-rep-tip/',
'https://www.ams-samplers.com/1-clay-rep-tip/',
'https://www.ams-samplers.com/1-1-4-regular-oversized-rep-tip/',
'https://www.ams-samplers.com/1-1-4-mud-rep-tip/',
'https://www.ams-samplers.com/1-mud-rep-tip/',
'https://www.ams-samplers.com/1-regular-oversized-rep-tip/',
'https://www.ams-samplers.com/sbs-internal-drive-tip/',
'https://www.ams-samplers.com/replaceable-sand-probe-tip/',
'https://www.ams-samplers.com/2-carbide-tip/',
'https://www.ams-samplers.com/tip-hard-surfaced-2/',
'https://www.ams-samplers.com/2-quick-connect-carbide-tip/',
'https://www.ams-samplers.com/aluminum-2-ms-sludge-core-tip/',
'https://www.ams-samplers.com/safety-liner-splitter/',
'https://www.ams-samplers.com/2-sst-scoop-w-rubber-grip/',
'https://www.ams-samplers.com/3-sst-scoop-w-rubber-grip/',
'https://www.ams-samplers.com/6-sst-scoop-w-rubber-grip/',
'https://www.ams-samplers.com/8-sst-scoop-w-rubber-grip/',
'https://www.ams-samplers.com/12-sst-scoop-w-rubber-grip/',
'https://www.ams-samplers.com/sst-spade-shovel/']

     for x in range(0,10000):
         print(x)
         print(listt[x])
         get_details(listt[x])

