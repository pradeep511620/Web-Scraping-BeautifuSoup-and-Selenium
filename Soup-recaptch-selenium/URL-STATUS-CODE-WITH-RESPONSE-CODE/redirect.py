import requests
url="https://www.raptorsupplies.com.sg/approved-vendor/000044"
r=requests.get(url)
"""
print(r.status_code)
print(r.url)
print(r.history)"""
for i,response in enumerate(r.history,1):
    print(i,response.url)
    print(r.status_code,r.url,r.history)