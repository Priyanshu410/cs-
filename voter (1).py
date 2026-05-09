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
c.execute("INSERT INTO voter VALUES (1, 123456789, 'Anand Dubey', 'Rajesh Dubey', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (2, 987654321, 'Nisha Asthana', 'Amit ASthana', 22, 'Female', 'S-135')")
c.execute("INSERT INTO voter VALUES (3, 555666777, 'Siddhant', 'Vikram Singh', 23, 'Male', 'S-136')")
c.execute("INSERT INTO voter VALUES (4, 878541235, 'Kajal', 'Sanjay', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (5, 789754354, 'Shiv Prakash', 'Manish Prakash', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (6, 455489753, 'Khadak Singh', 'Rohan Singh', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (7, 564867127, 'Aman', 'Prabhat', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (8, 123867885, 'Santosh', 'Anand', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (9, 741085296, 'Raj Kumar', 'Siddharth Kumar', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (10, 802486200, 'Supriyal Sen', 'Vikram Sen', 21, 'Male', 'S-134')")
