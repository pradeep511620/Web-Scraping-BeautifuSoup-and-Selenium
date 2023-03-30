import time
import mysql.connector
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32 (3)//chromedriver.exe')
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_onb"
)
# cur = mydb.cursor()
# cur.execute("SELECT DISTINCT url FROM `l3_filter_test1`")
# myresult = cur.fetchall()
# for url in myresult:
#     l3_url=url[0]
url='https://www.raptorsupplies.com/c/ac-motors'
driver.get(url)

time.sleep(4)

# print(p_element.text)
driver.execute_script("var a=document.getElementsByClassName('filters');" 
                      "for(var i = 0; i< a.length; i++){"
                      "var b = a[i].getElementsByTagName('label');" 
                      "console.log(b.length);" 
                      "for(var j = 0; j<b.length; j++){"
                      "b[j].style.display='block';"
                      "}" 
                      "}")
data = dict()
parentContainer = driver.find_elements_by_class_name("filters")
a=0
for selector in parentContainer:
    attribute = selector.find_elements_by_class_name("filternames")

    for attr in attribute:
        a += 1
        attributeName = attr.text

        option = selector.find_elements_by_tag_name("label")
        data[attributeName] = dict()
        count = 0
        for optn in option:

            # data[attributeName][count] = optn.text
            count+=1
        data[attributeName] = count
        attr_name=attributeName
        attr_value=(count)
        mycursor = mydb.cursor()

        sql = "INSERT INTO `l3_filter_count` (url, attr_name,attr_count) VALUES (%s, %s,%s)"

        mycursor.execute(sql, (url, attr_name, attr_value,))

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")




# for s in myresult:
#     for d in data:
#         if (s[0]==d):
#             print('match found'+s[0]+"::"+d)
#             if(s[1]==data[d]):
#                 print('count matched '+str(s[1])+" :: "+str(data[d]))
#             else:
#                 print('count not matched ' + str(s[1]) + " :: " + str(data[d]))
#                 #print(l3_url)




