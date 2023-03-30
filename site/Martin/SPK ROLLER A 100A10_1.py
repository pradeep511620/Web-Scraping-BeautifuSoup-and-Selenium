# https://www.martinsprocket.com/view/products/product-search?Website_Code=SP1

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\nextgenraptor\Downloads\chromedriver_win32 (3)\chromedriver.exe")
url = 'https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=100A10&Website_CategoryName=Sprockets&Website_Code=SP1'
driver.get(url)
driver.maximize_window()
################
time.sleep(3)
b_lst = []
c_lst = []
d_lst = []
e_lst = []
a = 0
for title in driver.find_elements(By.TAG_NAME,'Span'):
    a += 1
    if a == 1:
        continue
    elif a == 2:
        Title = title.text
        print(Title)
    elif a==3:
        Mpn = title.text
        print(Mpn)
    else:
        continue
#################

a = 0
for upc in driver.find_elements(By.XPATH, "/html/body/div/div[2]/div/div[2]/div"):
    a += 1
    if a == 1:
        UPC = upc.text
        print(UPC)
    elif a == 2:
        DESCRIPTION = upc.text
        print(DESCRIPTION)
    else:
        continue

###################
for image in driver.find_elements(By.TAG_NAME,'img'):
    IMAGE = image.get_attribute('src')
    print(IMAGE)
###############
time.sleep(3)
a = 0
for td in driver.find_elements(By.TAG_NAME,'td'):
    a += 1
    if a == 1:
        A = td.text
        b_lst.append(A) #print(A)
    elif a == 2:
        A_VALUE = td.text
        c_lst.append(A_VALUE) #print(A_VALUE)
    elif a == 3:
        B = td.text
        b_lst.append(B)#print(B)
    elif a == 4:
        B_VALUE = td.text
        print(B_VALUE)
    elif a == 5:
        C = td.text
        b_lst.append(C)#print(C)
    elif a == 6:
        C_VALUE = td.text
        print(C_VALUE)
    elif a == 7:
        D = td.text
        b_lst.append(D)#print(D)
    elif a == 8:
        D_VALUE = td.text
        print(D_VALUE)
    elif a == 9:
        E = td.text
        b_lst.append(E)#print(E)
    elif a == 10:
        E_VALUE = td.text
        print(E_VALUE)
    elif a == 11:
        F = td.text
        b_lst.append(F)# print(F)
    elif a == 12:
        F_VALUE = td.text
        print(F_VALUE)
    elif a == 13:
        G = td.text
        b_lst.append(G)#print(G)
    elif a == 14:
        G_VALUE= td.text
        print(G_VALUE)
    elif a == 15:
        H = td.text
        b_lst.append(H)#print(H)
    elif a == 16:
        H_VALUE = td.text
        print(H_VALUE)
    elif a == 17:
        I= td.text
        b_lst.append(I)#print(I)
    elif a == 18:
        I_VALUE = td.text
        print(I_VALUE)
    elif a == 19:
        J= td.text
        b_lst.append(J)#print(J)
    elif a == 20:
        J_VALUE = td.text
        print(J_VALUE)
    elif a == 21:
        K= td.text
        b_lst.append(K)#print(K)
    elif a == 22:
        K_VALUE = td.text
        print(K_VALUE)
    elif a == 23:
        L= td.text
        b_lst.append(L)#print(L)
    elif a == 24:
        L_VALUE = td.text
        print(L_VALUE)
    elif a == 25:
        M= td.text
        b_lst.append(M)# print(M)
    elif a == 26:
        M_VALUE = td.text
        print(M_VALUE)
    elif a == 27:
        N = td.text
        b_lst.append(A)#print(N)
    elif a== 28:
        N_VALUE = td.text
        print(N_VALUE)
    else:
        continue
##############################
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Misc Info").click()
a = 0
for td in driver.find_elements(By.TAG_NAME,'td'):
    a += 1
    if a == 29:
        b = td.text
        print(b)
    elif a== 30:
        b_value = td.text
        print(b_value)
    elif a == 31:
        c = td.text
        print(c)
    elif a== 32:
        c_value = td.text
        print(c_value)
    elif a == 33:
        d = td.text
        print(d)
    elif a== 34:
        d_value = td.text
        print(d_value)
    elif a == 35:
        e = td.text
        print(e)
    elif a== 36:
        e_value = td.text
        print(e_value)
    elif a == 37:
        f = td.text
        print(f)
    elif a== 38:
        f_value = td.text
        print(f_value)
    else:
        continue

with open("spk_roller_a_100a10.csv", 'w', encoding='UTF8') as f_out1, \
open("spk_roller_a_100a10_1.csv", 'w', encoding='UTF8') as f_out2:
    # writer1 = csv.writer(f_out1)
    # header1 = ['Title', 'Mpn', 'UPC', 'DESCRIPTION','IMAGE']
    # data1 = [Title, Mpn, UPC, DESCRIPTION, IMAGE]
    # writer1.writerow(header1)
    # writer1.writerow(data1)

    writer2 = csv.writer(f_out2)
    header2 = ['MPN', 'ATTRIBUTE', 'VALUE']
    writer2.writerow(header2)

    a = Mpn
    writer2.writerow(row[:0] + a.split('='))
    # if Mpn == Mpn:
    #     b = attr_value.split(' ')[1:]  # stainless, steel
    #     d = "Material  " + ' '.join([i for i in b])  # string stainless steel
    #     c = "Grade  " + attr_value.split(' ')[0]
    #     # print(c)
    #     # for j in d:
    #     writer.writerow(row[:6] + c.split('='))
    #     writer.writerow(row[:7] + d.split('='))
