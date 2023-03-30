from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("SELECT url,id FROM `faq_url_json` WHERE id>970 and check_data IS NULL ")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    id = fetch[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    s = []
    data = dict()
    for x in soup.find_all('script')[-1]:
        z = str(x)

        y = z.split('\t')
        a = "".join(y)
        j = a.split('\n')
        j1 = "".join(j)
        b = j1.split('[    {')[1]
        c = ''.join(b)
        d = c.split('\n')
        e = ''.join(d)
        f = e.split('","')
        g = '","'.join(f)
        h = g.split('"@type": "Question",     "name": "')
        i = ''
        count = 0
        ques = []
        ans = []

        for i in h:
            count += 1
            k = i.split('"acceptedAnswer": {      "@type": "Answer",      "text": "')[0]

            m = i.split('"acceptedAnswer": {      "@type": "Answer",      "text": "')[1:]
            m1 = ''.join(m)
            m2 = m1.replace('"    }  }  ,    {', '').replace('"    }  }  ]}', '')

            if m2 != '':
                ques.append(len(k))
                ans.append(len(m2))
                # print(ques)
                # print(ans)

            # print(k)
            # print(m2)

        sql = ("UPDATE `faq_url_json` SET check_data ='" + str(ques) + "' , check_data_ans = '" + str(
            ans) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

    print('---next data check---')
