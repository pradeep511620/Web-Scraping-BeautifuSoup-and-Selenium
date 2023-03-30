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
    #save_details: TextIO = open("tcm1.txt", "a+")
    #save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
    #save_details.close()
    #print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

    print("Please wait. Program will work in background.\n")

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    d = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
    d.get(url)



    image   = ''

    try:
        image=d.find_element_by_xpath("//*[@id='enhanced-content__carousel-zoom-image']/div/img").get_attribute("src")
        print("Image : "+image)
    except:
        pass



    save_details: TextIO = open("img(44).txt", "a+", encoding="utf-8")
    save_details.write("\n"+list[x]+"\t"+image )

    save_details.close()
    print("\n**Record stored into txt file.**")

if __name__ == '__main__':
    list=[
'https://www.grainger.com/product/53MF86',
'https://www.grainger.com/product/53MF87',
'https://www.grainger.com/product/53MF88',
'https://www.grainger.com/product/53MF89',
'https://www.grainger.com/product/53MF90',
'https://www.grainger.com/product/53MF91',
'https://www.grainger.com/product/53MF92',
'https://www.grainger.com/product/53MF93',
'https://www.grainger.com/product/53MF94',
'https://www.grainger.com/product/53MF95',
'https://www.grainger.com/product/53MF96',
'https://www.grainger.com/product/53MF97',
'https://www.grainger.com/product/53MF98',
'https://www.grainger.com/product/53MF99',
'https://www.grainger.com/product/53MG01',
'https://www.grainger.com/product/53MG02',
'https://www.grainger.com/product/53MG03',
'https://www.grainger.com/product/53MG04',
'https://www.grainger.com/product/53MG05',
'https://www.grainger.com/product/53MG06',
'https://www.grainger.com/product/53MG07',
'https://www.grainger.com/product/53MG08',
'https://www.grainger.com/product/53MG09',
'https://www.grainger.com/product/53MG10',
'https://www.grainger.com/product/53MG11',
'https://www.grainger.com/product/53MG12',
'https://www.grainger.com/product/53MG13',
'https://www.grainger.com/product/53MG14',
'https://www.grainger.com/product/53MG15',
'https://www.grainger.com/product/53MG16',
'https://www.grainger.com/product/53MG17',
'https://www.grainger.com/product/53MG18',
'https://www.grainger.com/product/53MG19',
'https://www.grainger.com/product/53MG20',
'https://www.grainger.com/product/53MG21',
'https://www.grainger.com/product/53MG22',
'https://www.grainger.com/product/53MG23',
'https://www.grainger.com/product/53MG24',
'https://www.grainger.com/product/53MG25',
'https://www.grainger.com/product/53MG26',
'https://www.grainger.com/product/53MG27',
'https://www.grainger.com/product/53MG28',
'https://www.grainger.com/product/53MG29',
'https://www.grainger.com/product/53MG30',
'https://www.grainger.com/product/53MG31',
'https://www.grainger.com/product/53MG32',
'https://www.grainger.com/product/53MG33',
'https://www.grainger.com/product/53MG34',
'https://www.grainger.com/product/53MG35',
'https://www.grainger.com/product/53MG36',
'https://www.grainger.com/product/53MG37',
'https://www.grainger.com/product/53MG38',
'https://www.grainger.com/product/53MG39',
'https://www.grainger.com/product/53MG40',
'https://www.grainger.com/product/53MG41',
'https://www.grainger.com/product/53MG42',
'https://www.grainger.com/product/53MG43',
'https://www.grainger.com/product/53MG44',
'https://www.grainger.com/product/53MG45',
'https://www.grainger.com/product/53MG46',
'https://www.grainger.com/product/53MG47',
'https://www.grainger.com/product/53MG48',
'https://www.grainger.com/product/53MG49',
'https://www.grainger.com/product/53MG50',
'https://www.grainger.com/product/53MG51',
'https://www.grainger.com/product/53MG52',
'https://www.grainger.com/product/53MG53',
'https://www.grainger.com/product/53MG54',
'https://www.grainger.com/product/53MG55',
'https://www.grainger.com/product/53MG56',
'https://www.grainger.com/product/53MG57',
'https://www.grainger.com/product/53MG58',
'https://www.grainger.com/product/53MG59',
'https://www.grainger.com/product/53MG60',
'https://www.grainger.com/product/53MG61',
'https://www.grainger.com/product/53MG62',
'https://www.grainger.com/product/53MG63',
'https://www.grainger.com/product/53MG64',
'https://www.grainger.com/product/53MG65',
'https://www.grainger.com/product/53MG66',
'https://www.grainger.com/product/54FJ68',
'https://www.grainger.com/product/54FJ69',
'https://www.grainger.com/product/54FJ70',
'https://www.grainger.com/product/54FJ71',
'https://www.grainger.com/product/54FJ72',
'https://www.grainger.com/product/54FJ73',
'https://www.grainger.com/product/54FJ74',
'https://www.grainger.com/product/54FJ75',
'https://www.grainger.com/product/54FJ76',
'https://www.grainger.com/product/54FJ77',
'https://www.grainger.com/product/54FJ79',
'https://www.grainger.com/product/54FJ80',
'https://www.grainger.com/product/54FJ81',
'https://www.grainger.com/product/54FJ82',
'https://www.grainger.com/product/54FJ83',
'https://www.grainger.com/product/54FJ84',
'https://www.grainger.com/product/54FJ85',
'https://www.grainger.com/product/54FJ87',
'https://www.grainger.com/product/54FJ88',
'https://www.grainger.com/product/54FJ89',
'https://www.grainger.com/product/54FJ90',
'https://www.grainger.com/product/54FJ91',
'https://www.grainger.com/product/54FJ92',
'https://www.grainger.com/product/54FJ93',
'https://www.grainger.com/product/54FJ94',
'https://www.grainger.com/product/54FJ95',
'https://www.grainger.com/product/54FJ97',
'https://www.grainger.com/product/54FJ98',
'https://www.grainger.com/product/54FJ99',
'https://www.grainger.com/product/54FK01',
'https://www.grainger.com/product/54FK02',
'https://www.grainger.com/product/54FK03',
'https://www.grainger.com/product/54FK04',
'https://www.grainger.com/product/54FK05',
'https://www.grainger.com/product/54FL36',
'https://www.grainger.com/product/54FL37',
'https://www.grainger.com/product/54FL38',
'https://www.grainger.com/product/54FL39',
'https://www.grainger.com/product/54FL40',
'https://www.grainger.com/product/54FL41',
'https://www.grainger.com/product/54FL42',
'https://www.grainger.com/product/54FL43',
'https://www.grainger.com/product/54FL44',
'https://www.grainger.com/product/54FL45',
'https://www.grainger.com/product/54FL46',
'https://www.grainger.com/product/54FL47',
'https://www.grainger.com/product/54FL48',
'https://www.grainger.com/product/54FL49',
'https://www.grainger.com/product/54FL50',
'https://www.grainger.com/product/54FL51',
'https://www.grainger.com/product/54FL52',
'https://www.grainger.com/product/54FL53',
'https://www.grainger.com/product/54FL54',
'https://www.grainger.com/product/54FL55',
'https://www.grainger.com/product/54FL56',
'https://www.grainger.com/product/54FL57',
'https://www.grainger.com/product/54FL58',
'https://www.grainger.com/product/54FL59',
'https://www.grainger.com/product/54FL60',
'https://www.grainger.com/product/54FL61',
'https://www.grainger.com/product/54FL62',
'https://www.grainger.com/product/54FL63',
'https://www.grainger.com/product/54FL64',
'https://www.grainger.com/product/54FL65',
'https://www.grainger.com/product/54FL66',
'https://www.grainger.com/product/54FL67',
'https://www.grainger.com/product/54FL68',
'https://www.grainger.com/product/54FL69',
'https://www.grainger.com/product/54FL70',
'https://www.grainger.com/product/54FL71',
'https://www.grainger.com/product/54FL72',
'https://www.grainger.com/product/54FL73',
'https://www.grainger.com/product/54FL74',
'https://www.grainger.com/product/54FL75',
'https://www.grainger.com/product/54FL76',
'https://www.grainger.com/product/54FL77',
'https://www.grainger.com/product/54FL78',
'https://www.grainger.com/product/54FL79',
'https://www.grainger.com/product/54FL80',
'https://www.grainger.com/product/54FL81',
'https://www.grainger.com/product/54FL82',
'https://www.grainger.com/product/54FL83',
'https://www.grainger.com/product/54FL84',
'https://www.grainger.com/product/54FL85',
'https://www.grainger.com/product/54FL86',
'https://www.grainger.com/product/54FL87',
'https://www.grainger.com/product/54FL88',
'https://www.grainger.com/product/54FL89',
'https://www.grainger.com/product/54FL90',
'https://www.grainger.com/product/54FL91',
'https://www.grainger.com/product/54FL92',
'https://www.grainger.com/product/54FL93',
'https://www.grainger.com/product/54FL94',
'https://www.grainger.com/product/54FL95',
'https://www.grainger.com/product/54FL96',
'https://www.grainger.com/product/54FL97',
'https://www.grainger.com/product/54FL98',
'https://www.grainger.com/product/54FL99',
'https://www.grainger.com/product/54FM01',
'https://www.grainger.com/product/54FM02',
'https://www.grainger.com/product/54FM03',
'https://www.grainger.com/product/54FM04',
'https://www.grainger.com/product/54FM05',
'https://www.grainger.com/product/54FM06',
'https://www.grainger.com/product/54FM07',
'https://www.grainger.com/product/54FM08',
'https://www.grainger.com/product/54FM09',
'https://www.grainger.com/product/54FM10',
'https://www.grainger.com/product/54FM11',
'https://www.grainger.com/product/54FM12',
'https://www.grainger.com/product/54FM13',
'https://www.grainger.com/product/54FM14',
'https://www.grainger.com/product/54FM15',
'https://www.grainger.com/product/54FM16',
'https://www.grainger.com/product/54FM17',
'https://www.grainger.com/product/54FM18',
'https://www.grainger.com/product/54FM19',
'https://www.grainger.com/product/54FM20',
'https://www.grainger.com/product/54FM21',
'https://www.grainger.com/product/54FM22',
'https://www.grainger.com/product/54FM23',
'https://www.grainger.com/product/54FM32',
'https://www.grainger.com/product/54FM90',
'https://www.grainger.com/product/54FM91',
'https://www.grainger.com/product/54FM92',
'https://www.grainger.com/product/54FM93',
'https://www.grainger.com/product/54FM94',
'https://www.grainger.com/product/54FM95',
'https://www.grainger.com/product/54FM96']
    for x in range(0,5001):

     url = list[x]

     print(url)
     print(x)

     get_details(url)




