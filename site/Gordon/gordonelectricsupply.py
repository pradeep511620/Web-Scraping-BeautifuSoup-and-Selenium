import requests
from bs4 import BeautifulSoup
import time
myresults = [
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=1',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=2',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=3',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=4',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=5',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=6',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=7',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=8',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=9',
'https://www.gordonelectricsupply.com/s/Appleton-Electric/mfr-1ICG?process=search&itemsperpage=60&sortby=availSort&display=thumb&fqall=&fqv=&fq=&sf=&allnstr=&ph=&pl=&qdx=0&nstr=&narrowby=&pagenum=10']

a = 0
for result in myresults:
    a += 1
    print(a)
    try:
        url = result
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')
        time.sleep(3)
        url_lst1 = []
        for s in soup.find_all('a', {'class': 'prodTitle'}):
            prod_url = s['href']
            url_lst1.append(prod_url)

    except AttributeError:
        pass
print(url_lst1)

# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'lxml')
# time.sleep(3)
# url_lst1 = []
# for s in soup.find_all('a', {'class': 'prodTitle'}):
#     prod_url = s['href']
#     url_lst1.append(prod_url)
# print(url_lst1)

