
import requests
from bs4 import BeautifulSoup
url=["http://vn.raptorsupplies.com","http://kr.raptorsupplies.com","http://tw.raptorsupplies.com","http://th.raptorsupplies.com","http://tr.raptorsupplies.com","http://jp.raptorsupplies.com","http://www.raptorsupplies.it",
"http://www.raptorsupplies.es","http://www.raptorsupplies.pl","http://www.raptorsupplies.dk"]
for url1 in url:
    link1=url1+'/b/akro-mils'

    response = requests.get(link1)
    soup = BeautifulSoup(response.content, 'lxml')
    a=0
    for title in soup.find('ul', class_='col-sm-6').find_all("a"):
        a+=1
        url=title.get('href')
        if(a==2):
            links=(url)
            response = requests.get(links)
            print(response)
            print(links)

            # mc_url=links.split('/b/')
            # url2=(mc_url[0])
            # final_url1 = url
            # if (url2 == ''):
            #     final_link = (link1 +"/b/"+ mc_url[1])
            #     print(final_link)
            # elif(url2 !=" "):
            #     print(final_url1)

