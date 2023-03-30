import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.raptorsupplies.com/b/grainger')
soup = BeautifulSoup(r.content,'html.parser')
s = []
data = dict()
for x in soup.find_all('script')[1]:
    z = str(x)
    y = z.split('\t')
    a = "".join(y)
    b = a.split('[{')[1]
    c = ''.join(b)
    d = c.split('\n')
    e = ''.join(d)
    f = e.split('","')
    g = '","'.join(f)
    h = g.split('"@type": "Question","name": "')
    i = ''
    for i in h:
        k = i.split('","acceptedAnswer": {"@type": "Answer","text": "')[0]

        m = i.split('","acceptedAnswer": {"@type": "Answer","text": "')[1:]
        print(k)
        print('--')
        print(m)





#
# from selenium import webdriver
# driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe')
#
# driver.get('https://www.raptorsupplies.com/pd/ingersoll-rand/2545')
# for x in driver.find_elements_by_xpath('/html/body/script[2]'):
#     print(x.get_attribute('innerHTML'))
