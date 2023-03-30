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
uri ="c/hex-head-cap-screws"

driver.get('https://raptorsupplies.com/'+uri)

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
p_element = driver.find_element_by_id(id_='filtersection')
dataString = p_element.text
dataStringArray = dataString.split('See More')
data = dict()
p=0
for i in dataStringArray:
    filterOptions = ''
    filterOptionsVal = ''
    p = 0
    q = 0
    flag = 0
    options = i.split('\n')
    for j in options:
        if(p == 0 and j != ''):
            filterOptions = j
            data[filterOptions] = dict()
            flag =1
        elif(p == 1 and j != '' and flag == 0):
            filterOptions = j
            data[filterOptions] = dict()
            flag = 1
        elif(j != ''):

            filterOptionsVal = j
            data[filterOptions][q] = filterOptionsVal
            q += 1
        p+=1
    # data[filterOptions][q] = filterOptionsVal
print(data)
# cur = mydb.cursor()
# cur.execute(
#     "SELECT DISTINCT header_lebel,COUNT(DISTINCT val)AS cnt FROM `l3_filter_test` WHERE req='"+uri+"' GROUP BY cat_id,header_lebel ")
# myresult = cur.fetchall()
# for s in myresult:
#     for d in data:
#         if (s[0]==d):
#             print('match found'+s[0]+"::"+d)
#             if(s[1]==data[d]):
#                 print('count matched '+str(s[1])+" :: "+str(data[d]))
#             else:
#                 print('count not matched ' + str(s[1]) + " :: " + str(data[d]))




