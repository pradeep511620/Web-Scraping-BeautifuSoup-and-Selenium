import requests
import webbrowser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url = 'https://www.grainger.com/category/fasteners/bolts/hex-head-bolts/standard-hex-head-cap-screws'
res = requests.get(url, headers = headers)
page_soup = bs(res.text, "html.parser")
containers = page_soup.findAll("div", {"class": "_2jG4D-"})
print(len(containers))
shoe_colors = []
for container in containers:
    if container.find("div", {'class': 'gl-product-card__reviews-number'}) is not None:
     shoe_model = container.div.div.img["title"]
     review = container.find('div', {'class':'gl-product-card__reviews-number'})
     review = int(review.text)
options = Options()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/chromedriver.exe')
driver.get(url)
myLength = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span.gl-price"))))
while True:
    driver.execute_script("window.scrollBy(0,400)", "")
    try:
        WebDriverWait(driver, 20).until(lambda driver: len(driver.find_elements_by_css_selector("span.gl-price")) > myLength)
        titles = driver.find_elements_by_css_selector("span.gl-price")
        myLength = len(titles)
    except TimeoutException:
        break
print(myLength)
for title in titles:
    print(title.text)
driver.quit()