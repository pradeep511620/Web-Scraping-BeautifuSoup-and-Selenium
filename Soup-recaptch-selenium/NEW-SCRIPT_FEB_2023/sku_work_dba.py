import mysql.connector

connection = mysql.connector.connect(
    database="PS_DOORS_onboarding",
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020"
)

arr4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
        'M', 'N', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr = arr1 = arr2 = arr3 = arr4
arr5 = ['2', '3', '4', '6', '7', '8', '9']

cursor = connection.cursor()
max_sku = "SELECT MAX(sku) as sku from rpt_m241.rpt_catalog_product_entity"
cursor.execute(max_sku)
max_sku_rp = cursor.fetchall()

for x in max_sku_rp:
    i = arr4.index(x[0][0])
    j = arr4.index(x[0][1])
    k = arr5.index(x[0][2])
    l = arr4.index(x[0][3])
    m = arr4.index(x[0][4])
    n = arr4.index(x[0][5]) + 1

    if n == 23:
        m += 1
        n = 0
    print(i, j, k, l, m, n)
    sql_total = "SELECT DISTINCT entity_id FROM rpt_catalog_product_entity ORDER BY entity_id  "
    cursor.execute(sql_total)
    sql_total_count = cursor.fetchall()

    if sql_total_count:
        for x in sql_total_count:
            y = x[0]
            res = sql_total_count
            seq = arr[i] + arr1[j] + arr5[k] + arr2[l] + arr3[m] + arr4[n]
            print(seq, y)
            n += 1
            if n == 23:
                m += 1
                n = 0

            if m == 23:
                l += 1
                m = 0
                n = 0

            if l == 23:
                k += 1
                l = 0
                m = 0
                n = 0

            if k == 7:
                j += 1
                k = 0
                l = 0
                m = 0
                n = 0

            if j == 23:
                i += 1
                j = 0
                k = 0
                l = 0
                m = 0
                n = 0

            if i == 23:
                print("series Over")
                exit()


