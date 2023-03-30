import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="data_filter_work"
)
cur = mydb.cursor()
cur.execute("SELECT  new_attr_name,new_attr_value,model_no,entity_id,l3_name,id,value1,unit1,value2,unit2,brand,"
            "raw_value,attr_data_type,old_attr_value,grainger FROM `58_l3_update_new_value` WHERE "
            "remarks_25='missing values'  AND attr_data_type ='Continuous' AND value1 ='' AND new_attr_name='Thread Size' AND new_attr_value LIKE '%M%'   ")
myresult = cur.fetchall()
# print(myresult)
for fetch in myresult:

    new_attr_name = fetch[0]
    new_attr_value = fetch[1]
    model_no = fetch[2]
    entity_id = fetch[3]
    l3_name = fetch[4]
    id = fetch[5]
    value1 = fetch[6]
    unit1 = fetch[7]
    value2 = fetch[8]
    unit2 = fetch[9]
    brand = fetch[10]
    raw_value = fetch[11]
    attr_data_type = fetch[12]
    old_attr_value = fetch[13]
    grainger = fetch[14]

    if new_attr_name == 'Thread Size':
        s111 = new_attr_value.replace('M', '')
        s11 = s111.split(' x ')[0]
        s1 = new_attr_value.split(' x ')[1]
        s2 = "rp_" + s1
        s = s11 + 'mm'
        z = 'Thread Dia.'
        z1 = 'Thread Pitch'
        # print(z, s)
        # print(z1, s2)
        # print(id)
        dc = 'mm'

        c = 'Done'
        sql = ("UPDATE `58_l3_update_new_value` SET remarks_25 ='" + str(c) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

        sql = "INSERT INTO `58_l3_update_new_value` (new_attr_value,new_attr_name,entity_id,model_no,l3_name,value1," \
              "unit1,value2,unit2,brand,raw_value,attr_data_type,old_attr_value,grainger) VALUES (%s, %s ,%s ,%s, %s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        val = (s, z, entity_id, model_no, l3_name, value1, dc, value2, unit2, brand, raw_value, attr_data_type,
               old_attr_value, grainger)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)
        sql = "INSERT INTO `58_l3_update_new_value` (new_attr_value,new_attr_name,entity_id,model_no,l3_name,value1," \
              "unit1,value2,unit2,brand,raw_value,attr_data_type,old_attr_value,grainger) VALUES (%s, %s ,%s ,%s, %s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        val = (s2, z1, entity_id, model_no, l3_name, value1, unit1, value2, unit2, brand, raw_value, attr_data_type,
               old_attr_value, grainger)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)
