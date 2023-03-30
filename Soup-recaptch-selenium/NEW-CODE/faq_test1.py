import requests
from bs4 import BeautifulSoup
url=["http://www.raptorsupplies.de",
"http://www.raptorsupplies.fr",
"http://www.raptorsupplies.nl",
"http://gr.raptorsupplies.com",
"http://fi.raptorsupplies.com",
"http://se.raptorsupplies.com",
"http://ro.raptorsupplies.com",
"http://hu.raptorsupplies.com",
"http://no.raptorsupplies.com"]

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
