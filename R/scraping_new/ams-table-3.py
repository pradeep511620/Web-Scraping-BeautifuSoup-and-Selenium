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

            save_details: TextIO = open("rag-ams3.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x]  +"\t"+ sku+"\t" + val )
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        pass


    try:
        for j in range(1, 20):
            val=d.find_element_by_xpath("//*[@id='tab-description']/ul[2]/li["+str(j)+"]").text

            save_details: TextIO = open("rag-ams3.txt", "a+", encoding="utf-8")
            save_details.write("\n" + listt[x]+"\t"+ sku + "\t" + val )
            save_details.close()
            print("\n**Record stored into txt file.**")

    except:
        pass









if __name__ == '__main__':


     listt =['https://www.ams-samplers.com/2-sst-scoop/',
'https://www.ams-samplers.com/3-sst-scoop/',
'https://www.ams-samplers.com/6-sst-scoop/',
'https://www.ams-samplers.com/8-sst-scoop/',
'https://www.ams-samplers.com/12-sst-scoop/',
'https://www.ams-samplers.com/montana-sharp-shooter-w-rubber-coated-handle/',
'https://www.ams-samplers.com/montana-sharp-shooter/',
'https://www.ams-samplers.com/idaho-spoon/',
'https://www.ams-samplers.com/5-8-compact-slide-hammer/',
'https://www.ams-samplers.com/3-4-30-lb-slide-hammer/',
'https://www.ams-samplers.com/professional-slide-hammer/',
'https://www.ams-samplers.com/hex-quick-pin-slide-hammer/',
'https://www.ams-samplers.com/5-8-regular-slide-hammer/',
'https://www.ams-samplers.com/3-4-heavy-duty-slide-hammer/',
'https://www.ams-samplers.com/signature-slide-hammer/',
'https://www.ams-samplers.com/signature-compact-slide-hammer/',
'https://www.ams-samplers.com/signature-heavy-duty-slide-hammer/',
'https://www.ams-samplers.com/munsell-soil-binder-w-chart/',
'https://www.ams-samplers.com/mccullough-geo-guide-card-and-geotechnical-gauge/',
'https://www.ams-samplers.com/usda-soil-texturing-field-flow-chart/',
'https://www.ams-samplers.com/field-guide-for-soil-stratigraphic-analysis/',
'https://www.ams-samplers.com/2-3-4-core-catcher/',
'https://www.ams-samplers.com/ms-2-plastic-core-catcher/',
'https://www.ams-samplers.com/2-soil-core-catcher/',
'https://www.ams-samplers.com/core-catcher-1/',
'https://www.ams-samplers.com/core-catcher-1-3-8/',
'https://www.ams-samplers.com/core-catcher-2-1-2/',
'https://www.ams-samplers.com/core-catcher-3/',
'https://www.ams-samplers.com/1-1-8-soil-ejector-spoon/',
'https://www.ams-samplers.com/7-8-soil-ejector-spoon/',
'https://www.ams-samplers.com/33-soil-ejector-for-7-8-soil-probe/',
'https://www.ams-samplers.com/21-soil-ejector-for-soil-probe/',
'https://www.ams-samplers.com/nylaflow-nylon-tubing-type-t-19-id-x-1-4-od/',
'https://www.ams-samplers.com/poly-tube-3-16-id-x-1-4-od-x-500/',
'https://www.ams-samplers.com/silicone-15-tubing-x-1-5-minimum-quantity-per-order/',
'https://www.ams-samplers.com/3-8-od-x-1-4-id-x-1-polyethylene-tubing/',
'https://www.ams-samplers.com/gp-slotted-sampler-tube-4/',
'https://www.ams-samplers.com/1-4-id-x-3-8-od-x-100-flouropolymer-tubing/',
'https://www.ams-samplers.com/3-16-id-x-1-4-od-x-250-fluoropolymer-tubing/',
'https://www.ams-samplers.com/3-16-id-x-1-4-od-x-100-fluoropolymer-tubing/',
'https://www.ams-samplers.com/3-16-id-x-1-4-od-x-50-fluoropolymer-tubing/',
'https://www.ams-samplers.com/hand-pump/',
'https://www.ams-samplers.com/crescent-wrench-12/',
'https://www.ams-samplers.com/universal-slip-wrench/',
'https://www.ams-samplers.com/spanner-wrench/',
'https://www.ams-samplers.com/tee-handle-allen-wrench/',
'https://www.ams-samplers.com/pipe-wrench-12/',
'https://www.ams-samplers.com/4-sst-regular-bits/',
'https://www.ams-samplers.com/5-sst-regular-bits/',
'https://www.ams-samplers.com/1-1-2-sst-mud-bits/',
'https://www.ams-samplers.com/1-3-4-sst-mud-bits/',
'https://www.ams-samplers.com/2-3-4-sst-mud-bits/',
'https://www.ams-samplers.com/3-1-4-sst-mud-bits/',
'https://www.ams-samplers.com/4-sst-mud-bits/',
'https://www.ams-samplers.com/5-sst-mud-bits/',
'https://www.ams-samplers.com/1-1-2-sst-sand-bits/',
'https://www.ams-samplers.com/1-3-4-sst-sand-bits/',
'https://www.ams-samplers.com/2-1-4-sst-sand-bits/',
'https://www.ams-samplers.com/2-3-4-sst-sand-bits/',
'https://www.ams-samplers.com/3-1-4-sst-sand-bits/',
'https://www.ams-samplers.com/5-sst-sand-bits/',
'https://www.ams-samplers.com/2-sst-mud-bits/',
'https://www.ams-samplers.com/2-sst-sand-bits/',
'https://www.ams-samplers.com/2-sst-regular-bits/',
'https://www.ams-samplers.com/2-1-4-sst-mud-bits/',
'https://www.ams-samplers.com/4-sst-sand-bits/',
'https://www.ams-samplers.com/6-mud-bits/',
'https://www.ams-samplers.com/7-mud-bits/',
'https://www.ams-samplers.com/8-mud-bits/',
'https://www.ams-samplers.com/flighted-auger-tip-2-1-2-hex-replaceable-bits/',
'https://www.ams-samplers.com/quick-connect-female-to-5-8-female-adapter/',
'https://www.ams-samplers.com/milwaukee-no-48-08-8585-18-splined-shank-adapter/',
'https://www.ams-samplers.com/5-8threaded-male-to-sds-plus-drill-adapter/',
'https://www.ams-samplers.com/5-8threaded-male-to-sds-max-drill-adapter/',
'https://www.ams-samplers.com/sds-max-drill-adapter-to-3-4-od/',
'https://www.ams-samplers.com/slide-hammer-adapter-to-3-4-od/',
'https://www.ams-samplers.com/extension-drive-adapter-to-3-4-id/',
'https://www.ams-samplers.com/5-8threaded-male-to-ea-410-spring-drill-adapter/',
'https://www.ams-samplers.com/5-8threaded-male-to-ea-410-drill-adapter/',
'https://www.ams-samplers.com/jack-adapter-tee-male/',
'https://www.ams-samplers.com/aluminum-2-ms-sludge-core-tip-w-valve/',
'https://www.ams-samplers.com/1-1-2-hard-surfaced-tip/']

     for x in range(0,10000):
         print(x)
         print(listt[x])
         get_details(listt[x])

