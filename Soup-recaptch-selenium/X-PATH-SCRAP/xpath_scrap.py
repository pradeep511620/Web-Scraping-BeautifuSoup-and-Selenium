import requests
from lxml import html
url="https://staging.raptorsupplies.com/pd/vulcan-hart/00-357036-00003"
page = requests.get(url)
root = html.fromstring(page.content,'lxml')

tree = root.getroottree()
result = root.xpath('//*[@id="allheadingresp"]')
for r in result:
    print(r.text)