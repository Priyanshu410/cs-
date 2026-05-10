import mysql.connector as m
a=m.connect(host="localhost",user="root",password="cyberdemon_456",database="voting")

c=a.cursor()

c.execute("create database if not exists voting")

c.execute("use voting")
c.execute("create table if not exists voter(serial_no int," \
                              "EPIC_no int," \
                              "name varchar(20)," \
                              "father_name varchar(30)," \
                              "age int," \
                              "gender varchar(10)," \
                              "address varchar(60))")
c.execute("INSERT INTO voter VALUES (1, 123456789, 'Anand Dubey', 'Rajesh Dubey', 21, 'Male', 'S-134')")
c.execute("INSERT INTO voter VALUES (2, 987654321, 'Nisha Asthana', 'Amit ASthana', 22, 'Female', 'S-135')")
c.execute("INSERT INTO voter VALUES (3, 555666777, 'Siddhant', 'Vikram Singh', 23, 'Male', 'S-136')")
c.execute("INSERT INTO voter VALUES (4, 878541235, 'Kajal', 'Sanjay', 26, 'Female', 'S-137')")
c.execute("INSERT INTO voter VALUES (5, 789754354, 'Shiv Prakash', 'Manish Prakash', 20, 'Male', 'S-138')")
c.execute("INSERT INTO voter VALUES (6, 455489753, 'Khadak Singh', 'Rohan Singh', 18, 'Male', 'S-139')")
c.execute("INSERT INTO voter VALUES (7, 564867127, 'Aman', 'Prabhat', 30, 'Male', 'S-140')")
c.execute("INSERT INTO voter VALUES (8, 123867885, 'Santosh', 'Anand', 45, 'Male', 'S-141')")
c.execute("INSERT INTO voter VALUES (9, 741085296, 'Raj Kumar', 'Siddharth Kumar', 56, 'Male', 'S-142')")
c.execute("INSERT INTO voter VALUES (10, 802486200, 'Supriyal Sen', 'Vikram Sen', 60, 'Female', 'S-143')")
a.commit()

c.execute("create table if not exists party(Serial_no int," \
                              "Party_id int," \
                              "Party_name varchar(50)," \
                              "Leader_name varchar(50)," \
                              "total_members int," \
                              "Party_Symbol varchar(60))")
c.execute("INSERT INTO party VALUES (1, 101, 'Bharatiya Janta Party', 'Narendra Modi', 10000, 'Lotus')")
c.execute("INSERT INTO party VALUES (2, 102, 'Democratic Unity Party', 'Ananya Sharma', 4800, 'Handshake')")
c.execute("INSERT INTO party VALUES (3, 103, 'Peoples Freedom Party', 'Arjun Mehta', 4500, 'Roasted Nuts')")
c.execute("INSERT INTO party VALUES (4, 104, 'Green Future Party', 'Sanjay Singh', 4000, 'Green Leaf')")
c.execute("INSERT INTO party VALUES (5, 105, 'Youth Development Party', 'Manish Oberoi', 4500, 'Torch')")
c.execute("INSERT INTO party VALUES (6, 106, 'Indian National Congress Party', 'Rahul Gandhi', 2000, 'Hand')")
c.execute("INSERT INTO party VALUES (7, 107, 'National Reform Party', 'Kejriwal', 5100, 'Broomstick')")
c.execute("INSERT INTO party VALUES (8, 108, 'Citizens Welfare Party', 'Sneha Malhotra', 3500, 'Star')")
c.execute("INSERT INTO party VALUES (9, 109, 'Bharat Rising Party', 'Vikram Joshi', 4800, 'Tulip')")
c.execute("INSERT INTO party VALUES (10, 110, 'United Vision Party', 'Neha Bansal', 4600, 'Globe')")
a.commit()

c.execute("create table if not exists candidate(Serial_No int,"
          "Candidate_Id int,"
          "Candidate_Name varchar(50),"
          "Party_Name varchar(50),"
          "Age int,"
          "Position varchar(30),"
          "Gender varchar(30),"
          "Net_Worth varchar(30),"
          "Date_Of_Joining varchar(30),"
          "Votes_Received int)")
c.execute("INSERT INTO candidate VALUES (1, 12345, 'Aryan Malhotra', 'Bharatiya Janta Party', 46, 'President', 'Male', '8 Cr', '12-01-2015', 125000)")
c.execute("INSERT INTO candidate VALUES (2, 98765, 'Rohan Sethi', 'Democratic Unity Party', 43, 'Chairperson', 'Male', '6.5 Cr', '15-03-2017', 118500)")
c.execute("INSERT INTO candidate VALUES (3, 55566, 'Sanya Kapoor', 'Democratic Unity Party', 38, 'Secretary', 'Female', '4 Cr', '23-03-2016', 87500)")
c.execute("INSERT INTO candidate VALUES (4, 87854, 'Ishita Arora', 'Peoples Freedom Party', 36, 'President', 'Female', '7 Cr', '10-07-2018', 110200)")
c.execute("INSERT INTO candidate VALUES (5, 78975, 'Dev Mehta', 'Green Future Party', 40, 'Chairperson', 'Male', '5.5 Cr', '15-07-2014', 98000)")
c.execute("INSERT INTO candidate VALUES (6, 45548, 'Kunal Bhatia', 'Green Future Party', 34, 'Youth Leader', 'Male', '3 Cr', '19-11-2019', 64000)")
c.execute("INSERT INTO candidate VALUES (7, 56486, 'Riya Sharma', 'Youth Development Party', 37, 'Presient', 'Female', '4.8 Cr', '08-09-2018', 102400)")
c.execute("INSERT INTO candidate VALUES (8, 12386, 'Tanya Khurana', 'Indian National Congress Party', 45, 'chairpersom', 'Female', '6 Cr', '14-05-2020', 96500)")
c.execute("INSERT INTO candidate VALUES (9, 74108, 'Laksh Verma', 'Indian National Congress Party', 40, 'Secretary','Male', '3.2 Cr', '11-05-2019', 71000)")
c.execute("INSERT INTO candidate VALUES (10, 12868, 'Aakash Jain', 'Youth Development Party', 40, 'coordinator', 'Male', '2.5 Cr', '20-08-2021', 59000)")
c.execute("INSERT INTO candidate VALUES (11, 87923, 'Anika Gill', 'National Reform Party', 51, 'President', 'Female', '9 Cr', '27-02-2017', 121300)")
c.execute("INSERT INTO candidate VALUES (12, 75953, 'Mehak Chopra', 'Peoples Freedom Party', 49, 'Treasurer', 'Female', '3.5 Cr', '17-10-2020', 76000)")
c.execute("INSERT INTO candidate VALUES (13, 54123, 'Vivaan Das', 'National Reform Party', 38, 'spokesperson',' Male', '4.6 Cr', '18-08-2013', 83000)")
c.execute("INSERT INTO candidate VALUES (14, 12340, 'Sahil Kapoor', 'Citizens Welfare Party', 42, 'Chairperson', 'Male', '4.5 Cr', '22-01-2018', 87500)")
c.execute("INSERT INTO candidate VALUES (15, 78954, 'Kiara Malhotra', 'United Vision Party', 39, 'Chairperson', 'Female', '5.5 Cr', '04-04-2020', 93400)")
c.execute("INSERT INTO candidate VALUES (16, 2355, 'Naina Verma', 'Bharat Rising Party', 48, 'President', 'Female', '7.8 Cr', '29-09-2021', 113700)")
c.execute("INSERT INTO candidate VALUES (17, 87605, 'Arnav Joshi', 'United Vision Party', 31, 'Youth Coordinator', 'Male', '2.4 Cr', '30-06-2016', 54000)")
c.execute("INSERT INTO candidate VALUES (18, 20356, 'Yash Thakur', 'Bharat Rising Party', 37, 'Campaign Manager', 'Male', '4 Cr', '11-12-2019', 78500)")
c.execute("INSERT INTO candidate VALUES (19, 78952, 'Myra Bansal', 'Bharatiya Janta Party',41, 'Vice President','Female', '6 Cr', '19-10-2021', 100000)")
c.execute("INSERT INTO candidate VALUES (20, 54920, 'Pihu Singhania', 'Citizens Welfare Party', 33, 'Media Head', 'Female', '2.9 Cr', '07-02-2023', 62000)")
a.commit()


print("\n========== MAIN MENU ==========")
print("1. Voter Table")
print("2. Party Table")
print("3. Candidate Table")
print("4. Exit")

ch=int(input("Enter your choice: "))

if ch==1:
    print("\n----- VOTER MENU -----")
    print("1. Show All Voters")
    print("2. Search Voter")
    print("3. Insert Voter")
    print("4. Delete Voter")
    print("5. Update Voter Age")
    print("6. Back")

    v=int(input("Enter choice: "))

    if v==1:
        c.execute("select * from voter")
        data=c.fetchall()

        for i in data:
            print(i)

    elif v==2:
        epic=int(input("Enter EPIC number: "))
        c.execute("select * from voter where EPIC_no=()",(epic,))
        data=c.fetchall()

        for i in data:
            print(i)
    elif v==3:
        s=int(input("Enter serial number: "))
        e=int(input("Enter EPIC number: "))
        n=input("Enter name: ")
        f=input("Enter father name: ")
        age=int(input("Enter age: "))
        g=input("Enter gender: ")
        ad=input("Enter address: ")

        c.execute("insert into voter values((),(),(),(),(),(),())",
                                            (s,e,n,f,age,g,ad))

        a.commit()

        print("Record inserted")

    elif v==4:
        epic=int(input("Enter EPIC number: "))

        c.execute("delete from voter where EPIC_no=()",(epic,))

        a.commit()

        print("Record deleted")

    elif v==5:
        epic=int(input("Enter EPIC number: "))
        age=int(input("Enter new age: "))

        c.execute("update voter set age=() where EPIC_no=()",(age,epic))

        a.commit()

        print("Record updated")

    elif v==6:
            pass

    else:
        print("Invalid choice")
elif ch==2:


            print("\n----- PARTY MENU -----")
            print("1. Show All Parties")
            print("2. Search Party")
            print("3. Insert Party")
            print("4. Delete Party")
            print("5. Update Members")
            print("6. Back")

            p=int(input("Enter choice: "))

            if p==1:

                c.execute("select * from party")

                data=c.fetchall()

                for i in data:
                    print(i)

            elif p==2:

                pid=int(input("Enter Party ID: "))

                c.execute("select * from party where Party_id=()",(pid,))

                data=c.fetchall()

                for i in data:
                    print(i)

            elif p==3:

                s=int(input("Enter serial number: "))
                pid=int(input("Enter Party ID: "))
                pn=input("Enter party name: ")
                ln=input("Enter leader name: ")
                tm=int(input("Enter total members: "))
                ps=input("Enter symbol: ")

                c.execute("insert into party values((),(),(),(),(),())",
                          (s,pid,pn,ln,tm,ps))

                a.commit()

                print("Record inserted")

            elif p==4:

                pid=int(input("Enter Party ID: "))

                c.execute("delete from party where Party_id=()",(pid,))

                a.commit()

                print("Record deleted")

            elif p==5:

                pid=int(input("Enter Party ID: "))
                tm=int(input("Enter new total members: "))

                c.execute("update party set total_members=() where Party_id=()",
                          (tm,pid))

                a.commit()

                print("Record updated")

            elif p==6:
                pass

            else:
                print("Invalid choice")
elif ch==3:


            print("\n----- CANDIDATE MENU -----")
            print("1. Show All Candidates")
            print("2. Search Candidate")
            print("3. Delete Candidate")
            print("4. Update Votes")
            print("5. Back")

            cd=int(input("Enter choice: "))

            if cd==1:

                c.execute("select * from candidate")

                data=c.fetchall()

                for i in data:
                    print(i)

            elif cd==2:

                cid=int(input("Enter Candidate ID: "))

                c.execute("select * from candidate where Candidate_Id=()",(cid,))

                data=c.fetchall()

                for i in data:
                    print(i)

            elif cd==3:

                cid=int(input("Enter Candidate ID: "))

                c.execute("delete from candidate where Candidate_Id=()",(cid,))

                a.commit()

                print("Record deleted")

            elif cd==4:

                cid=int(input("Enter Candidate ID: "))
                vote=int(input("Enter new votes: "))

                c.execute("update candidate set Votes_Received=() where Candidate_Id=()",
                          (vote,cid))

                a.commit()

                print("Record updated")

            elif cd==5:
                pass

            else:
                print("Invalid choice")


elif ch==4:

        print("Program ended")
        pass

else:
        print("Invalid choice")        

            