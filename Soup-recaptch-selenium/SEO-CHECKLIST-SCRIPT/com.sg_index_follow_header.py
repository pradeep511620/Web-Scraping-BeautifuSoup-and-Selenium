import requests
from bs4 import BeautifulSoup

index_follow = ["https://www.raptorsupplies.com.sg/",
                "https://www.raptorsupplies.com.sg/l1/abrasives",
                "https://www.raptorsupplies.com.sg/l2/abrasive-accessories",
                "https://www.raptorsupplies.com.sg/c/hydraulic-filters",
                "https://www.raptorsupplies.com.sg/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal",
                "https://www.raptorsupplies.com.sg/b",
                "https://www.raptorsupplies.com.sg/b/3m",
                "https://www.raptorsupplies.com.sg/c/airline-filtration-and-co-monitors/3m",
                "https://www.raptorsupplies.com.sg/b/char-lynn",
                "https://www.raptorsupplies.com.sg/b/aaon",
                "https://www.raptorsupplies.com.sg/b/raxit",
                "https://www.raptorsupplies.com.sg/b/3m?page=2",
                "https://www.raptorsupplies.com.sg/b/akro-mils?page=2",
                "https://www.raptorsupplies.com.sg/c/hydraulic-filters?page=1",
                "https://www.raptorsupplies.com.sg/c/hydraulic-filters?page=19",
                "https://www.raptorsupplies.com.sg/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal?page=1",
                "https://www.raptorsupplies.com.sg/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal?page=44",
                "https://www.raptorsupplies.com.sg/checkout/cart",
                "https://www.raptorsupplies.com.sg/s?q=morse",
                "https://www.raptorsupplies.com.sg/grainger-singapore",
                "https://www.raptorsupplies.com.sg/b/mcmaster-carr-singapore",
                "https://www.raptorsupplies.com.sg/login",
                "https://www.raptorsupplies.com.sg/request-for-quote",
                "https://www.raptorsupplies.com.sg/vendor-registration", "https://www.raptorsupplies.com.sg/source",
                "https://www.raptorsupplies.com.sg/faq", "https://www.raptorsupplies.com.sg/partners",
                "https://www.raptorsupplies.com.sg/about-us", "https://www.raptorsupplies.com.sg/contact",
                ]
no_index_follow = ["https://www.raptorsupplies.com.sg/l2/hvac-motors?page=2",
                   "https://www.raptorsupplies.com.sg/l2/hvac-motors?page=97",
                   "https://www.raptorsupplies.com.sg/c/papr-accessories/3m?page=2&cat=83&catKey=465895",
                   "https://www.raptorsupplies.com.sg/c/papr-accessories?cat=24149&catKey=2155588",

                   ]
print('INDEX FOLLOW LIST =')
print("Checking Robot tag......")
print('\n')
for fetch in index_follow:
    url = fetch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for meta in soup.find_all('meta', attrs={"name": "robots"}):
        robot_tag = meta.get('content')
        page_na = url.split('com/')[1:]
        page_name = ''.join(page_na)
        if page_name == '':
            print(url, robot_tag)
        else:
            print(url, " = ", robot_tag)

print('Checking Done Robot tag for INDEX FOLLOW')
print('NOW Checking....Hmm ? YES')
print('\n')
print('NOINDEX FOLLOW LIST = ......')
for fetch1 in no_index_follow:
    url1 = fetch1
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, 'html.parser')

    for meta in soup.find_all('meta', attrs={"name": "robots"}):
        robot_tag = meta.get('content')
        page_na = url1.split('com/')[1:]
        page_name = ''.join(page_na)
        if page_name == '':
            print(url1, robot_tag)
        else:
            print(url1, " = ", robot_tag)
print('----------')
print('Test Complete Successfully')
