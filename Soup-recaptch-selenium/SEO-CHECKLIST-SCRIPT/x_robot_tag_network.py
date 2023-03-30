
import requests
from bs4 import BeautifulSoup

index_follow = ["https://b2b.raptorsupplies.it/",
                "https://b2b.raptorsupplies.it/l1/abrasives",
                "https://b2b.raptorsupplies.it/l2/abrasive-accessories",
                "https://b2b.raptorsupplies.it/c/hydraulic-filters",
                "https://b2b.raptorsupplies.it/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal",
                "https://b2b.raptorsupplies.it/b",
                "https://b2b.raptorsupplies.it/b/3m",
                "https://b2b.raptorsupplies.it/c/airline-filtration-and-co-monitors/3m",
                "https://b2b.raptorsupplies.it/b/char-lynn",
                "https://b2b.raptorsupplies.it/b/aaon",
                "https://b2b.raptorsupplies.it/b/raxit",
                "https://b2b.raptorsupplies.it/ww-grainger-dealer",
                "https://b2b.raptorsupplies.it/b/mcmaster-carr-europe-uk-distributor",
                "https://b2b.raptorsupplies.it/login",
                "https://b2b.raptorsupplies.it/request-for-quote",
                "https://b2b.raptorsupplies.it/vendor-registration","https://b2b.raptorsupplies.it/source",
                "https://b2b.raptorsupplies.it/faq","https://b2b.raptorsupplies.it/partners",
                "https://b2b.raptorsupplies.it/about-us","https://b2b.raptorsupplies.it/contact",
                ]
no_index_follow = ["https://b2b.raptorsupplies.it/l2/hvac-motors?page=2",
                   "https://b2b.raptorsupplies.it/l2/hvac-motors?page=97",
                   "https://b2b.raptorsupplies.it/b/3m?page=2",
                   "https://b2b.raptorsupplies.it/b/akro-mils?page=2",
                   "https://b2b.raptorsupplies.it/c/hydraulic-filters?page=1",
                   "https://b2b.raptorsupplies.it/c/hydraulic-filters?page=19",
                   "https://b2b.raptorsupplies.it/c/papr-accessories/3m?page=2&cat=83&catKey=465895",
                   "https://b2b.raptorsupplies.it/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal?page=1",
                   "https://b2b.raptorsupplies.it/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal?page=44",
                   "https://b2b.raptorsupplies.it/checkout/cart",
                   "https://b2b.raptorsupplies.it/s?q=morse"
                   ]
print('INDEX FOLLOW LIST =')
print("Checking  X Robot tag......")
print('\n')
for fetch in index_follow:
    url = fetch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    s = page.headers['x-robots-tag']
    page_na = url.split('.it/')[1:]
    page_name = ''.join(page_na)
    if page_name == '':
        print("home =",s)
    else:
        print(page_name, " = ", s)
print('Checking Done X Robot tag for INDEX FOLLOW')
print('NOW Checking....Hmm ? YES')
print('\n')
print('NOINDEX FOLLOW LIST = ......')
for fetch1 in no_index_follow:
    url1 = fetch1
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, 'html.parser')

    s1 = page.headers['x-robots-tag']
    page_na = url1.split('com/')[1:]
    page_name = ''.join(page_na)
    if page_name == '':
        print("home =", s1)
    else:
        print(page_name, " = ", s1)
print('----------')
print('Test Complete Successfully')



