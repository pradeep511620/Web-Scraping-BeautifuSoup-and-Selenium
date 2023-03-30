import requests
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from PIL import Image
url='https://www.zoro.com/static/cms/product/large/Independent%20Design%20Inc%20DBA%20Champion%20Tool%20Storage_FMP4121RCxxRDxxb5323b.jpg'

opts = Options()
opts.headless = False
opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
d=uc.Chrome(version_main=109)
d.get(url)
print(d.page_source)
d.save_screenshot("zoro.png")

image = Image.open("zoro.png")

image.show()





