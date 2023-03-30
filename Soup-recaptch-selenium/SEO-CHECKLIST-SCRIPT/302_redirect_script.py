from bs4 import BeautifulSoup
import requests


url = ["https://www.raptorsupplies.com/l2/pneumatic-system-components?page=212"]

for fetch in url:
    url = fetch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    status = page.status_code
    response = page.history[0].status_code
    if status == 200:
        print("page url is working")
        if response == 301:
            print("page has permanently moved to a new location")
        elif response == 302:
            print("page move is only temporary")
        else:
            print("something else")
    else:
        print("page not found")



