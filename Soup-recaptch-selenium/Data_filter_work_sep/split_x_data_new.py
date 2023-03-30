import mysql.connector

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor()
cur.execute("SELECT  attr_name,attr_value,brand,model_no,id FROM `helicoil_chrislynn_split` WHERE attr_value  NOT LIKE '%#%' AND attr_value LIKE '%x%' AND attr_name !='Drill Size' ")
myresult = cur.fetchall()
# print(myresult)
for fetch in myresult:

    attr_name = fetch[0]
    attr_value = fetch[1]
    brand = fetch[2]
    model_no = fetch[3]
    id = fetch[4]

    if attr_name :
        s111 = attr_value.replace('M', '')
        s11 = s111.split(' x ')[0]
        s1 = attr_value.split(' x ')[1]
        s2 = "rp_" + s1
        s = s11 + 'mm'
        z = 'Thread Dia.'
        z1 = 'Thread Pitch'
        print(z, s)
        print(z1, s2)
        print(id)
        # dc = 'mm'

        c = 'Done'
        sql = ("UPDATE `helicoil_chrislynn_split` SET remarks_5 ='" + str(c) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

        sql = "INSERT INTO `helicoil_chrislynn_split` (new_attr_value,new_attr_name,model_no,brand,attr_name,attr_value) VALUES (%s, %s ,%s ,%s, %s,%s) "
        val = (s, z, model_no, brand, attr_name, attr_value)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")

        sql = "INSERT INTO `helicoil_chrislynn_split` (new_attr_value,new_attr_name,model_no,brand,attr_name,attr_value) VALUES (%s, %s ,%s ,%s, %s,%s) "
        val = (s2, z1, model_no, brand, attr_name, attr_value)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        print(id)
