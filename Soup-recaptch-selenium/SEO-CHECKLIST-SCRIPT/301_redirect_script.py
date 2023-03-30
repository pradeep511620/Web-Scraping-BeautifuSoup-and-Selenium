from bs4 import BeautifulSoup
import requests


url = ["https://www.raptorsupplies.com/protect-a-bed-bob2715-mattress-encasement-king-non-woven-pk8-439923"]

for fetch in url:
    url = fetch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    status = page.status_code
    response = page.history[0].status_code
    print(response)
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



