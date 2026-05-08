import mysql.connector as m
a=m.connect(host="localhost",user="root",password="",database="voting")
c=a.cursor()
c.execute("create table voter(serial_no int()," \
                              "EPIC_no int()," \
                              "name varchar(20)," \
                              "father_name varchar(30)," \
                              "age int()," \
                              "gender varchar(10)," \
                              "address varchar(60)")
c.execute("INSERT INTO voter VALUES (1, 123456789, 'ACD', 'AFC', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (2, 987654321, 'XYZ', 'DEF', 22, 'Female', 'S-135')")
c.execute("INSERT INTO voter VALUES (3, 555666777, 'PQR', 'LMN', 23, 'Male', 'S-136')")
