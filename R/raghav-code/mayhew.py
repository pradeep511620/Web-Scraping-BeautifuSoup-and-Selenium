import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.remote.webelement


def get_details(url):
        #current_date: object = datetime.now()
        #save_details: TextIO = open("Product_Details1.txt", "a+")
        #save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
        #save_details.close()
        #print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

        #print("Please wait. Program will work in background.\n")

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
        driver.get(url)
        time.sleep(5)


        try:
            img1 = driver.find_element_by_class_name("zoomImg").get_attribute("src")
            print("img1 : " + img1)
        except:
            img1 = " "
        try:
            img2 = driver.find_element_by_class_name("flex-active").get_attribute("src")
            print("img2 : " + img2)
        except:
            img2=" "
        try:
            img3 = driver.find_element_by_xpath("//div[@class='woocommerce-product-gallery woocommerce-product-gallery--with-images woocommerce-product-gallery--columns-4 images']//li[2]//img[1]").get_attribute("src")
            print("img3 : " + img3)
        except:
            img3=" "

        try:
            brand_name = driver.find_element_by_xpath("//*[@id='tab-description']/p[1]").text
            print("Brand Name : " + brand_name)
        except:
            brand_name = " "




        save_details: TextIO = open("mayhew.txt", "a+", encoding="utf-8")
        save_details.write("\n" + url+"\t"+img1+"\t"+img2+"\t"+img3+"\t" + brand_name )
        save_details.close()
        print("\n**Record stored into Product_Details.txt file.**")


        driver.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list=['10600',	'62214',	'61019',	'66008',	'66012',	'66080',	'66016',	'66010',	'66006',	'50501',	'50502',	'50503',	'50504',	'50506',	'50508',	'50509',	'50511',	'50512',	'50514',	'50516',	'50518',	'50519',	'50520',	'50522',	'50523',	'50524',	'50526',	'50541',	'50543',	'50544',	'50546',	'50550',	'50551',	'50553',	'50555',	'50556',	'50558',	'50559',	'50560',	'50561',	'50562',	'50563',	'50564',	'50565',	'50566',	'50568',	'50569',	'50570',	'50571',	'50573',	'50574',	'50575',	'50576',	'50577',	'50578',	'50579',	'50545',	'61080',	'62277',	'62010',	'62060',	'62080',	'60150',	'61306',	'41280',	'41285',	'60003',	'75101',	'75008',	'75005',	'75003',	'40102',	'76284',	'61366',	'17615',	'17750',	'17755',	'17150',	'17765',	'17770',	'17680',	'17705',	'17715',	'17720',	'17730',	'45046',	'17605',	'17810',	'17830',	'17845',	'41104',	'66900',	'66901',	'66902',	'37331',	'37003',	'37343',	'40022',	'40023',	'12311',	'12312',	'60007',	'66004',	'61365',	'61350',	'62258',	'66000',	'66002',	'80040',	'41102',	'41100',	'75125',	'75126',	'75127',	'40024',	'40106',	'40108',	'40113',	'66104',	'66106',	'66107',	'66122',	'66124',	'66475',	'66907',	'10505',	'10605MAY',	'10207',	'10213',	'10215',	'10219',	'10222',	'21601',	'21401',	'21500',	'25001',	'25008',	'25009',	'25010',	'25011',	'25015',	'25017',	'25019',	'25021',	'25023',	'25027',	'25029',	'61511',	'62077',	'61341',	'61340',	'62252',	'62254',	'46170',	'46174',	'46178',	'46000',	'46002',	'46004',	'46022',	'46026',	'46030',	'46034',	'46054',	'46056',	'46060',	'46064',	'46084',	'46088',	'46114',	'46118',	'46122',	'46140',	'46142',	'46168',	'17025',	'17055',	'17065',	'17600',	'17610',	'24548',	'24549',	'24550',	'24551',	'10403',	'10404',	'10405',	'10500',	'10501',	'10502MAY',	'10504',	'10605',	'94505',	'66260',	'62082',	'40111',	'70216',	'70205',	'75000',	'20301',	'21707',	'71501',	'74001',	'12310',	'61005',	'40101',	'70200',	'71500',	'70212',	'22012',	'70207',	'71504',	'71503',	'71502',	'70213',	'80205',	'10401',	'10402MAY',	'10200',	'10202MAY',	'10205',	'10209',	'10210',	'10212',	'10216',	'10220',	'10221',	'12002',	'70201',	'70209',	'70210',	'70217',	'70220',	'70221',	'10805',	'12205',	'10604',	'12300',	'12302',	'30202',	'31970',	'31972',	'31974',	'31986',	'31978',	'31980',	'40150',	'40152',	'40154',	'40001',	'40003',	'75004',	'40110',	'24000',	'24001',	'24002',	'74002',	'74003',	'74004',	'24301',	'22005',	'22010',	'22021',	'72010',	'21001',	'21002',	'21003',	'21004',	'21005',	'21019',	'21100',	'21104',	'21105',	'21219',	'21501',	'21502',	'21503',	'21504',	'71000',	'71001',	'71002',	'71004',	'71005',	'23001',	'23003',	'73002',	'20002',	'20005',	'20105',	'36019',	'41300',	'75006',	'40100',	'40104',	'76295',	'13080',	'14176',	'14177',
]
    for z in range(0,150):
        url = "https://mayhew.com/product/model-"+list[z]
        get_details(url)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/