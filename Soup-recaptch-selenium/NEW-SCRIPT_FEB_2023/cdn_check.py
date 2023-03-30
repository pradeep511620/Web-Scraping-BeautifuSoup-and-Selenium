# import cssutils

from bs4 import BeautifulSoup
import requests
import re

li = ['https://www.raptorsupplies.com/',
      'https://www.raptorsupplies.com/c/abrasive-mandrels',
      'https://www.raptorsupplies.com/p/merit/bore-polisher-extension-mandrel',
      'https://www.raptorsupplies.com/pd/merit/08834154463']
for fetch in li:
    page = requests.get(fetch)
    soup = BeautifulSoup(page.content,'html.parser')

    cssList=soup.find_all('link',{'href':re.compile('.css')})

    for css in cssList:
        css = css['href']
        print(css)
    print('--')
    """css_response = requests.get(css, verify=True,timeout=2)
        soup1 = (css_response.content, 'lxml')
        soup1 = str(soup1)
        b = (re.findall(r'(https?://\S+)',soup1))
        for x in b:
            st_img= (x.split(')')[0])
    
            page1 = requests.get(st_img)
    
            print(st_img)
            print(css)
"""