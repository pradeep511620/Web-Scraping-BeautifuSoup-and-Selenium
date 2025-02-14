import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re


myresult=['https://www.grainger.com/product/1KA29',
'https://www.grainger.com/product/1KA42',
'https://www.grainger.com/product/1KA80',
'https://www.grainger.com/product/1KA82',
'https://www.grainger.com/product/1KA84',
'https://www.grainger.com/product/1KB30',
'https://www.grainger.com/product/1KB73',
'https://www.grainger.com/product/1KB74',
'https://www.grainger.com/product/1RMY1',
'https://www.grainger.com/product/1XE85',
'https://www.grainger.com/product/1XU41',
'https://www.grainger.com/product/1XU74',
'https://www.grainger.com/product/22A706',
'https://www.grainger.com/product/2BE98',
'https://www.grainger.com/product/2BY65',
'https://www.grainger.com/product/2BY67',
'https://www.grainger.com/product/2BY80',
'https://www.grainger.com/product/2CB68',
'https://www.grainger.com/product/2CB84',
'https://www.grainger.com/product/2CU39',
'https://www.grainger.com/product/2CU42',
'https://www.grainger.com/product/2UPR2',
'https://www.grainger.com/product/2UPR4',
'https://www.grainger.com/product/30Z149',
'https://www.grainger.com/product/30Z150',
'https://www.grainger.com/product/30Z158',
'https://www.grainger.com/product/30Z159',
'https://www.grainger.com/product/30Z160',
'https://www.grainger.com/product/30Z188',
'https://www.grainger.com/product/30Z193',
'https://www.grainger.com/product/30Z203',
'https://www.grainger.com/product/30Z224',
'https://www.grainger.com/product/30Z228',
'https://www.grainger.com/product/30Z251',
'https://www.grainger.com/product/30Z262',
'https://www.grainger.com/product/30Z276',
'https://www.grainger.com/product/30Z347',
'https://www.grainger.com/product/30Z354',
'https://www.grainger.com/product/30Z409',
'https://www.grainger.com/product/30Z432',
'https://www.grainger.com/product/30Z433',
'https://www.grainger.com/product/30Z435',
'https://www.grainger.com/product/30Z436',
'https://www.grainger.com/product/30Z440',
'https://www.grainger.com/product/30Z442',
'https://www.grainger.com/product/30Z444',
'https://www.grainger.com/product/30Z450',
'https://www.grainger.com/product/30Z452',
'https://www.grainger.com/product/30Z454',
'https://www.grainger.com/product/30Z457',
'https://www.grainger.com/product/30Z458',
'https://www.grainger.com/product/30Z463',
'https://www.grainger.com/product/30Z469',
'https://www.grainger.com/product/30Z473',
'https://www.grainger.com/product/30Z475',
'https://www.grainger.com/product/30Z481',
'https://www.grainger.com/product/30Z483',
'https://www.grainger.com/product/30Z492',
'https://www.grainger.com/product/30Z493',
'https://www.grainger.com/product/30Z502',
'https://www.grainger.com/product/30Z505',
'https://www.grainger.com/product/30Z506',
'https://www.grainger.com/product/30Z507',
'https://www.grainger.com/product/30Z508',
'https://www.grainger.com/product/30Z509',
'https://www.grainger.com/product/30Z511',
'https://www.grainger.com/product/30Z513',
'https://www.grainger.com/product/30Z525',
'https://www.grainger.com/product/30Z530',
'https://www.grainger.com/product/30Z535',
'https://www.grainger.com/product/30Z551',
'https://www.grainger.com/product/30Z572',
'https://www.grainger.com/product/30Z574',
'https://www.grainger.com/product/30Z575',
'https://www.grainger.com/product/30Z576',
'https://www.grainger.com/product/30Z583',
'https://www.grainger.com/product/30Z585',
'https://www.grainger.com/product/30Z593',
'https://www.grainger.com/product/30Z595',
'https://www.grainger.com/product/30Z610',
'https://www.grainger.com/product/30Z619',
'https://www.grainger.com/product/30Z623',
'https://www.grainger.com/product/30Z631',
'https://www.grainger.com/product/30Z634',
'https://www.grainger.com/product/30Z637',
'https://www.grainger.com/product/30Z639',
'https://www.grainger.com/product/30Z641',
'https://www.grainger.com/product/30Z642',
'https://www.grainger.com/product/30Z643',
'https://www.grainger.com/product/30Z652',
'https://www.grainger.com/product/30Z653',
'https://www.grainger.com/product/30Z659',
'https://www.grainger.com/product/30Z660',
'https://www.grainger.com/product/30Z670',
'https://www.grainger.com/product/30Z676',
'https://www.grainger.com/product/30Z681',
'https://www.grainger.com/product/30Z682',
'https://www.grainger.com/product/30Z685',
'https://www.grainger.com/product/30Z690',
'https://www.grainger.com/product/30Z692',
'https://www.grainger.com/product/30Z699',
'https://www.grainger.com/product/30Z701',
'https://www.grainger.com/product/30Z704',
'https://www.grainger.com/product/30Z708',
'https://www.grainger.com/product/30Z711',
'https://www.grainger.com/product/30Z736',
'https://www.grainger.com/product/30Z742',
'https://www.grainger.com/product/30Z757',
'https://www.grainger.com/product/30Z765',
'https://www.grainger.com/product/30Z768',
'https://www.grainger.com/product/30Z769',
'https://www.grainger.com/product/30Z770',
'https://www.grainger.com/product/30Z777',
'https://www.grainger.com/product/30Z784',
'https://www.grainger.com/product/30Z785',
'https://www.grainger.com/product/30Z816',
'https://www.grainger.com/product/30Z821',
'https://www.grainger.com/product/30Z822',
'https://www.grainger.com/product/30Z824',
'https://www.grainger.com/product/30Z826',
'https://www.grainger.com/product/30Z857',
'https://www.grainger.com/product/30Z861',
'https://www.grainger.com/product/30Z875',
'https://www.grainger.com/product/30Z876',
'https://www.grainger.com/product/30Z881',
'https://www.grainger.com/product/30Z891',
'https://www.grainger.com/product/30Z908',
'https://www.grainger.com/product/30Z916',
'https://www.grainger.com/product/30Z921',
'https://www.grainger.com/product/30Z923',
'https://www.grainger.com/product/30Z924',
'https://www.grainger.com/product/3EPH2',
'https://www.grainger.com/product/446V57',
'https://www.grainger.com/product/446V58',
'https://www.grainger.com/product/446V59',
'https://www.grainger.com/product/446V60',
'https://www.grainger.com/product/446V61',
'https://www.grainger.com/product/446V62',
'https://www.grainger.com/product/446V63',
'https://www.grainger.com/product/446V95',
'https://www.grainger.com/product/446V96',
'https://www.grainger.com/product/446V97',
'https://www.grainger.com/product/446V98',
'https://www.grainger.com/product/446V99',
'https://www.grainger.com/product/446W01',
'https://www.grainger.com/product/446W02',
'https://www.grainger.com/product/446W03',
'https://www.grainger.com/product/446W54',
'https://www.grainger.com/product/446W55',
'https://www.grainger.com/product/446W56',
'https://www.grainger.com/product/446W57',
'https://www.grainger.com/product/446W58',
'https://www.grainger.com/product/446W59',
'https://www.grainger.com/product/446W60',
'https://www.grainger.com/product/446W61',
'https://www.grainger.com/product/446W62',
'https://www.grainger.com/product/446W63',
'https://www.grainger.com/product/446W64',
'https://www.grainger.com/product/446W65',
'https://www.grainger.com/product/446W66',
'https://www.grainger.com/product/446W67',
'https://www.grainger.com/product/446X63',
'https://www.grainger.com/product/446X64',
'https://www.grainger.com/product/446X65',
'https://www.grainger.com/product/446X66',
'https://www.grainger.com/product/446X67',
'https://www.grainger.com/product/446X68',
'https://www.grainger.com/product/446X69',
'https://www.grainger.com/product/446X70',
'https://www.grainger.com/product/446X71',
'https://www.grainger.com/product/446X72',
'https://www.grainger.com/product/446X73',
'https://www.grainger.com/product/446X74',
'https://www.grainger.com/product/446X75',
'https://www.grainger.com/product/446X76',
'https://www.grainger.com/product/446Y43',
'https://www.grainger.com/product/446Y44',
'https://www.grainger.com/product/446Y45',
'https://www.grainger.com/product/446Y46',
'https://www.grainger.com/product/446Y47',
'https://www.grainger.com/product/446Y48',
'https://www.grainger.com/product/446Y49',
'https://www.grainger.com/product/446Y50',
'https://www.grainger.com/product/446Y51',
'https://www.grainger.com/product/446Y52',
'https://www.grainger.com/product/446Y53',
'https://www.grainger.com/product/446Y54',
'https://www.grainger.com/product/446Y55',
'https://www.grainger.com/product/446Y56',
'https://www.grainger.com/product/446Y57',
'https://www.grainger.com/product/446Y58',
'https://www.grainger.com/product/446Y59',
'https://www.grainger.com/product/446Z37',
'https://www.grainger.com/product/446Z38',
'https://www.grainger.com/product/446Z39',
'https://www.grainger.com/product/446Z40',
'https://www.grainger.com/product/446Z41',
'https://www.grainger.com/product/446Z42',
'https://www.grainger.com/product/446Z43',
'https://www.grainger.com/product/446Z44',
'https://www.grainger.com/product/446Z45',
'https://www.grainger.com/product/446Z46',
'https://www.grainger.com/product/446Z47',
'https://www.grainger.com/product/446Z48',
'https://www.grainger.com/product/446Z49',
'https://www.grainger.com/product/446Z50',
'https://www.grainger.com/product/446Z51',
'https://www.grainger.com/product/446Z52',
'https://www.grainger.com/product/446Z53',
'https://www.grainger.com/product/447A23',
'https://www.grainger.com/product/447A24',
'https://www.grainger.com/product/447A25',
'https://www.grainger.com/product/447A26',
'https://www.grainger.com/product/447A27',
'https://www.grainger.com/product/447A28',
'https://www.grainger.com/product/447A29',
'https://www.grainger.com/product/447A30',
'https://www.grainger.com/product/447A31',
'https://www.grainger.com/product/447A32',
'https://www.grainger.com/product/447A33',
'https://www.grainger.com/product/447A34',
'https://www.grainger.com/product/447A35',
'https://www.grainger.com/product/447A36',
'https://www.grainger.com/product/447A37',
'https://www.grainger.com/product/447A38',
'https://www.grainger.com/product/447A39',
'https://www.grainger.com/product/447A81',
'https://www.grainger.com/product/447A82',
'https://www.grainger.com/product/447A83',
'https://www.grainger.com/product/447A84',
'https://www.grainger.com/product/447A85',
'https://www.grainger.com/product/447A86',
'https://www.grainger.com/product/447A87',
'https://www.grainger.com/product/447A88',
'https://www.grainger.com/product/447C28',
'https://www.grainger.com/product/447C29',
'https://www.grainger.com/product/447C30',
'https://www.grainger.com/product/447C31',
'https://www.grainger.com/product/447C32',
'https://www.grainger.com/product/447C33',
'https://www.grainger.com/product/447C34',
'https://www.grainger.com/product/447C35',
'https://www.grainger.com/product/447C36',
'https://www.grainger.com/product/447C37',
'https://www.grainger.com/product/447C84',
'https://www.grainger.com/product/447C85',
'https://www.grainger.com/product/447C86',
'https://www.grainger.com/product/447C87',
'https://www.grainger.com/product/447C88',
'https://www.grainger.com/product/447C89',
'https://www.grainger.com/product/447C90',
'https://www.grainger.com/product/447C91',
'https://www.grainger.com/product/447C92',
'https://www.grainger.com/product/447C93',
'https://www.grainger.com/product/447C94',
'https://www.grainger.com/product/447C95',
'https://www.grainger.com/product/447F66',
'https://www.grainger.com/product/447F67',
'https://www.grainger.com/product/447F68',
'https://www.grainger.com/product/447F69',
'https://www.grainger.com/product/447F70',
'https://www.grainger.com/product/447F71',
'https://www.grainger.com/product/447F72',
'https://www.grainger.com/product/447F73',
'https://www.grainger.com/product/447F74',
'https://www.grainger.com/product/447F75',
'https://www.grainger.com/product/447F76',
'https://www.grainger.com/product/447F77',
'https://www.grainger.com/product/447F78',
'https://www.grainger.com/product/447F79',
'https://www.grainger.com/product/447G78',
'https://www.grainger.com/product/447G79',
'https://www.grainger.com/product/447G80',
'https://www.grainger.com/product/447G81',
'https://www.grainger.com/product/447G82',
'https://www.grainger.com/product/447G83',
'https://www.grainger.com/product/447G84',
'https://www.grainger.com/product/447G85',
'https://www.grainger.com/product/447G86',
'https://www.grainger.com/product/447G87',
'https://www.grainger.com/product/447G88',
'https://www.grainger.com/product/447G89',
'https://www.grainger.com/product/447G90',
'https://www.grainger.com/product/447H44',
'https://www.grainger.com/product/447H45',
'https://www.grainger.com/product/447H46',
'https://www.grainger.com/product/447H47',
'https://www.grainger.com/product/447H48',
'https://www.grainger.com/product/447H49',
'https://www.grainger.com/product/447H50',
'https://www.grainger.com/product/447H51',
'https://www.grainger.com/product/447H52',
'https://www.grainger.com/product/447H53',
'https://www.grainger.com/product/447H54',
'https://www.grainger.com/product/447H55',
'https://www.grainger.com/product/447H56',
'https://www.grainger.com/product/447J10',
'https://www.grainger.com/product/447J11',
'https://www.grainger.com/product/447J12',
'https://www.grainger.com/product/447J13',
'https://www.grainger.com/product/447J14',
'https://www.grainger.com/product/447J15',
'https://www.grainger.com/product/447J16',
'https://www.grainger.com/product/447J17',
'https://www.grainger.com/product/447J18',
'https://www.grainger.com/product/447J19',
'https://www.grainger.com/product/447J20',
'https://www.grainger.com/product/447J21',
'https://www.grainger.com/product/4RVH1',
'https://www.grainger.com/product/4XLL2',
'https://www.grainger.com/product/4XLN7',
'https://www.grainger.com/product/4XLP1',
'https://www.grainger.com/product/4YJF3',
'https://www.grainger.com/product/4YJR8',
'https://www.grainger.com/product/4YJU2',
'https://www.grainger.com/product/4YLT6',
'https://www.grainger.com/product/5HAC7',
'https://www.grainger.com/product/5HAH2',
'https://www.grainger.com/product/5HCH0',
'https://www.grainger.com/product/5HCV3',
'https://www.grainger.com/product/5KEH3',
'https://www.grainger.com/product/5KEH4',
'https://www.grainger.com/product/5KEJ4',
'https://www.grainger.com/product/5KEJ5',
'https://www.grainger.com/product/5KEK3',
'https://www.grainger.com/product/5KEK4',
'https://www.grainger.com/product/5KEK5',
'https://www.grainger.com/product/5KEP1',
'https://www.grainger.com/product/5KEP2',
'https://www.grainger.com/product/5KGJ4',
'https://www.grainger.com/product/5KGJ5',
'https://www.grainger.com/product/5KGL9',
'https://www.grainger.com/product/5KGP7',
'https://www.grainger.com/product/5KGT6',
'https://www.grainger.com/product/5KGT7',
'https://www.grainger.com/product/5KGU9',
'https://www.grainger.com/product/5KGV3',
'https://www.grainger.com/product/5MWU1',
'https://www.grainger.com/product/5MWU6',
'https://www.grainger.com/product/5NYY7',
'https://www.grainger.com/product/6AB92',
'https://www.grainger.com/product/6AB93',
'https://www.grainger.com/product/6AB95',
'https://www.grainger.com/product/6AE56',
'https://www.grainger.com/product/6AE57',
'https://www.grainger.com/product/6AE58',
'https://www.grainger.com/product/6AE62',
'https://www.grainger.com/product/6AU55',
'https://www.grainger.com/product/6AV74',
'https://www.grainger.com/product/6AY10',
'https://www.grainger.com/product/6AY11',
'https://www.grainger.com/product/6AY54',
'https://www.grainger.com/product/6AY76',
'https://www.grainger.com/product/6AY98',
'https://www.grainger.com/product/6BA12']

for row in myresult:

 try:

    product_url = row

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+result.status_code)

    #a = (result.content.decode())


    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())

    title = soup.find("div",class_="sidebar__discontinued-product")
    aa=title.text.strip()
    print(aa)

    save_details: TextIO = open("current.txt", "a+", encoding="utf-8")
    save_details.write("\n"+product_url+"\t"+aa)
    save_details.close()
    print("\n**Record stored into txt file.**")






 except AttributeError:

   pass
