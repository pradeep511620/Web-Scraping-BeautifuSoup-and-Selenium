import mysql.connector
from fractions import Fraction

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="data_filter_work"
)
cur = mydb.cursor()
cur.execute("SELECT  new_attr_name,new_attr_value,model_no,entity_id,l3_name,id,value1 FROM `58_l3_update_new_value` WHERE remarks_25='Updated' AND new_attr_name !='Thread Size' AND new_attr_value LIKE '%.%'  ")
myresult = cur.fetchall()
# print(myresult)
for fetch in myresult:

    new_attr_name = fetch[0]
    new_attr_value = fetch[1]
    model_no = fetch[2]
    entity_id = fetch[3]
    l3_name= fetch[4]
    id = fetch[5]
    value1 = fetch[6]
    if new_attr_value :
        a = new_attr_value.strip('rp_').strip('RP_')
        b = a.replace(' ft.','').replace('"','')
        c = 'rp_' + b
        d = 'Done'
        e = 'feet'
        # print(c)
        sql = ("UPDATE `58_l3_update_new_value`  SET value1 ='" + str(
            c) + "',remarks_25 ='" + str(d) + "',unit1 ='" + str(e) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(id)
