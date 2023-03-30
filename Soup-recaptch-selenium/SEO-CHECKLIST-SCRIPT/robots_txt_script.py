import requests
from bs4 import BeautifulSoup

url = ["https://www.raptorsupplies.com/robots.txt",
       "https://www.raptorsupplies.co.uk/robots.txt",
       "https://www.raptorsupplies.com.sg/robots.txt",
       "https://www.raptorsupplies.com.au/robots.txt",
       "https://b2b.raptorsupplies.com/robots.txt",
       "https://gtrans.raptorsupplies.com/robots.txt",
       "https://www.raptorsupplies.de/robots.txt"]
for fetch in url:

    page = requests.get(fetch)
    soup = BeautifulSoup(page.content,'html.parser')
    s = soup.prettify()
    z = s.split("\n")
    this_d = dict()
    for x in z:
        a = x
        b = a.split(" ")
        c = " ".join(b)
        if c != "":
            d = c.split(" ")
            d1 = d[0].split(":")
            e = "".join(d1)
            this_dict = {
                            e: d[1]
                        }

            print(this_dict)
    print(fetch)






