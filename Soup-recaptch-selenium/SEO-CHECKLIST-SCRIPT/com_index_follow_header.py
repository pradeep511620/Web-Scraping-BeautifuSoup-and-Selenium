import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
import smtplib
index_follow = ["https://www.raptorsupplies.com/",
                "https://www.raptorsupplies.com/l1/abrasives",
                "https://www.raptorsupplies.com/l2/abrasive-accessories",
                "https://www.raptorsupplies.com/c/hydraulic-filters",
                "https://www.raptorsupplies.com/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal",
                "https://www.raptorsupplies.com/b",
                "https://www.raptorsupplies.com/b/3m",
                "https://www.raptorsupplies.com/c/airline-filtration-and-co-monitors/3m",
                "https://www.raptorsupplies.com/b/char-lynn",
                "https://www.raptorsupplies.com/b/aaon",
                "https://www.raptorsupplies.com/b/raxit",
                "https://www.raptorsupplies.com/b/3m?page=2",
                "https://www.raptorsupplies.com/b/akro-mils?page=2",
                "https://www.raptorsupplies.com/c/hydraulic-filters?page=1",
                "https://www.raptorsupplies.com/c/hydraulic-filters?page=19",
                "https://www.raptorsupplies.com/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal?page=1",
                "https://www.raptorsupplies.com/p/main-filter-inc/interchange-hydraulic-filters-glass-25-micron-viton-seal?page=44",
                "https://www.raptorsupplies.com/checkout/cart",
                "https://www.raptorsupplies.com/s?q=morse",
                "https://www.raptorsupplies.com/ww-grainger-dealer",
                "https://www.raptorsupplies.com/b/mcmaster-alternatives-sourcing",
                "https://www.raptorsupplies.com/login",
                "https://www.raptorsupplies.com/request-for-quote",
                "https://www.raptorsupplies.com/vendor-registration", "https://www.raptorsupplies.com/source",
                "https://www.raptorsupplies.com/faq", "https://www.raptorsupplies.com/partners",
                "https://www.raptorsupplies.com/about-us", "https://www.raptorsupplies.com/contact",
                ]
no_index_follow = [
                   "https://www.raptorsupplies.com/c/papr-accessories?cat=83,26013&catKey=465895,73103",
                   "https://www.raptorsupplies.com/c/papr-accessories?cat=24149&catKey=2155588",
                   "https://www.raptorsupplies.com/p/main-filter-inc/interchange-hydraulic-return-line-filters-cellulose-10-micron-viton-seal?cat=22683&catKey=618868"
                   ]
# print('INDEX FOLLOW LIST =')
print("Checking Robot tag......")
li = []
li2 = []
for fetch in index_follow:
    url = fetch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for meta in soup.find_all('meta', attrs={"name": "robots"}):
        robot_tag = meta.get('content')
        page_na = url.split('com/')[1:]
        page_name = ''.join(page_na)
        if page_name == '':
            # print(url, robot_tag)
            li.append(url)
            li2.append(robot_tag)
        else:
            # print(url, " = ", robot_tag)
            li.append(url)
            li2.append(robot_tag)

# print('Checking Done Robot tag for INDEX FOLLOW')
# print('NOW Checking....Hmm ? YES')
# print('NOINDEX FOLLOW LIST = ......')
for fetch1 in no_index_follow:
    url1 = fetch1
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, 'html.parser')

    for meta in soup.find_all('meta', attrs={"name": "robots"}):
        robot_tag = meta.get('content')
        page_na = url1.split('com/')[1:]
        page_name = ''.join(page_na)
        if page_name == '':
            # print(url1, robot_tag)
            li.append(url1)
            li2.append(robot_tag)
        else:
            # print(url1, " = ", robot_tag)
            li.append(url1)
            li2.append(robot_tag)

for x,y in zip(li,li2):
    final_result= (x,y)
    receivers_mail = ['rk2153691@gmail.com', 'rksingh@nextgenesolutions.com', 'nkmishra@nextgenesolutions.com']

    msg = MIMEMultipart()
    msg['From'] = 'sales@raptorsupplies.com'
    msg['To'] = receivers_mail

    toAddress = msg['To']
    subject = "INDEX FOLLOW Header Check"
    body = final_result
    massage = "subject:{}\n\n{}".format(subject, body)
    server = smtplib.SMTP("email-smtp.eu-west-1.amazonaws.com", 587)
    server.starttls()
    server.login("AKIAROILJ6GGW4CGS57B", "BM/Jl5EwExQ/8/xER6HEJH+tiWSr9eLUW+eZUlPEqyKU")
    server.sendmail(msg['From'], toAddress, massage)
    print('send email')
    server.quit()

print('----------')
print('Test Complete Successfully')







"""receivers_mail = ['rk2153691@gmail.com','rksingh@nextgenesolutions.com','nkmishra@nextgenesolutions.com']

msg = MIMEMultipart()
msg['From'] = 'sales@raptorsupplies.com'
msg['To'] = receivers_mail


toAddress = msg['To']
subject = "INDEX FOLLOW Header Check"
body = "INDEX FOLLOW Header Check"
massage="subject:{}\n\n{}".format(subject,body)
server = smtplib.SMTP("email-smtp.eu-west-1.amazonaws.com",587)
server.starttls()
server.login("AKIAROILJ6GGW4CGS57B", "BM/Jl5EwExQ/8/xER6HEJH+tiWSr9eLUW+eZUlPEqyKU")
server.sendmail(msg['From'], toAddress, massage)
print('send email')
server.quit()"""


