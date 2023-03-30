
import requests
from lxml import html
from itertools import cycle
import time

def free_proxies():
    h1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    Proxy_res = requests.get('https://free-proxy-list.net/',headers = h1)
    #print(Proxy_res.status_code)
    extract_proxies = html.fromstring(Proxy_res.content)
    Proxies = set()
    proxies = extract_proxies.xpath('//tbody/tr')[:100]
    for i in proxies:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = i.xpath('.//td[1]/text()')[0] + ':' + i.xpath('.//td[2]/text()')[0]
            Proxies.add(proxy)

    #print(Proxies)
    return Proxies

proxy_list = free_proxies()
proxy_pool = cycle(proxy_list)
for i in range(5):
    try:
        proxy = next(proxy_pool)
        print(proxy)
        proxy = {
            "http": proxy,
            "https": proxy
        }
        Res = requests.get('https://development.raptorsupplies.com/',proxies=proxy)
        print(Res.status_code)
        print("Sucessful Attempt for Home page")
        time.sleep(5)
        if Res.status_code == 200:
            break
    except:
        print("Unsucessful Attempt for Home page")

#tree = html.fromstring(Res.content)
#api_key = tree.xpath('//div[@class = "g-recaptcha"]/@data-sitekey')[0]
#print(api_key)
#captcha_token = tree.xpath('//input/@value')
#print(captcha_token)
#captcha_url = 'https://www.google.com/recaptcha/api2/reload?k='+ api_key


data = {
'name': 'Rahul kumar Singh',
'email': 'rksingh@nextgenesolutions.com',
'phone': 8294966962,
'message': 'test',
'country': 'India',
'my_url': 'http://stage.raptorsupplies.com/'
}
h1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
for i in range(5):
    try:
        proxy = next(proxy_pool)
        print(proxy)
        proxy = {
            "http": proxy,
            "https": proxy
        }
        get_in_touch = requests.post('https://stage.raptorsupplies.com/home_contact_us.php',data=data,headers=h1,proxies=proxy)
        print(get_in_touch.status_code)
        print(get_in_touch.content)
        if get_in_touch.status_code == 200:
            print("Query Successfully Submitted")
            break
    except:
        print("Query not Submitted")