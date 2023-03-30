import urllib.parse
from datetime import datetime
from typing import TextIO
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.remote.webelement


def get_details(url):
    current_date: object = datetime.now()
    save_details: TextIO = open("acc(eaton).txt", "a+")
    save_details.write("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")
    save_details.close()
    print("\nScrapping Started at : " + current_date.strftime("%B %d, %Y - %H:%M:%S") + "\n")

    print("Please wait. Program will work in background.\n")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
    driver.get(url)
    time.sleep(5)

    try:

        brands: list[selenium.webdriver.remote.webelement.WebElement] = driver.find_elements_by_class_name('details')




    except:
        print("More products not found.")
        driver.close()

    #  print("Brand List: ")
    # for brand in brands:
    #     print(brand.text)

    time.sleep(5)

    try:
        v=1
        for product in brands:
            try:

                v = str(v)
                hello = driver.find_element_by_xpath(
                        "//*[@id='model-group']/ul/li[" + v + "]/a").get_attribute("href")
               # print("hi")
                v = int(v)
                v = v + 1
                brand = product.text

                new = brand.split(' ')
                print(new[0])
                start = brand.index('(')
                end = brand.index(')', start + 1)
                substring = brand[start + 1:end]
                subs = int(substring)
                print(subs)
                sub = int(subs / 12)
                print(sub)
            except:
                continue

                brand_url = total_products_string = hyperlink = ''
                seller = seller_rating = quality = product_quality = service_quality = ''

                # print("Site URL : "+url)
            for i in range(0, sub + 1):

                    i = i + 1

                    j = str(i)
                    print(j)
                    brand_url = hello+  "?p=" + j
                    print("Brand URL : " + brand_url)

                    try:
                        d = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
                        d.get(brand_url)
                        time.sleep(5)
                        # products = d.find_elements_by_class_name('product-item-link')
                        # print("fffffffffffff")
                        # for p in products:
                        # print(p)
                        product_name = price = link = image = ''
                        # chrome_options = Options()
                        # chrome_options.add_argument("--headless")
                        # dri = webdriver.Chrome("C:/chromedriver.exe", options=chrome_options)
                        # dri.get(p.get_attribute('href'))
                        # time.sleep(5)

                        print("\n----------------------------------------------------------\n")
                        for z in range(0, 12):
                            try:
                                z = int(z)
                                z = z + 1
                                z = str(z)
                                product_name = d.find_element_by_xpath(
                                    "//*[@id='product-grid']/li[" + z + "]/div[2]/div/h3/a").text
                                print("Product Name : " + product_name)
                            except:
                                pass
                            try:
                                price = d.find_element_by_xpath(
                                    "//*[@id='product-grid']/li[" + z + "]/div[2]/div/div/span").text
                                print("Price : " + price)
                            except:
                                pass

                            try:
                                image = d.find_element_by_xpath(
                                    "//*[@id='product-grid']/li[" + z + "]/div[1]/a/span/span/img").get_attribute('src')
                                print("Product Image URL: " + image)
                            except:
                                print("Error : " + str(sys.exc_info()))
                                pass
                            try:
                                link = d.find_element_by_xpath("//*[@id='product-grid']/li["+z+"]/div[2]/div/h3/a").get_attribute('href')
                                print(" URL: " + link)
                            except:
                                print("Error : " + str(sys.exc_info()))
                                pass
                            save_details: TextIO = open("acc(eaton).txt", "a+", encoding="utf-8")
                            save_details.write("\n" + product_name + "\t" + price + "\t" + image + "\t" + link)
                            save_details.close()
                            print("\n**Record stored into txt file.**")
                    except:
                        pass


    except:
        d.close()


if __name__ == '__main__':
    url = "https://www.coasttocoastbreaker.com/accessories/eaton.html"
    get_details(url)


