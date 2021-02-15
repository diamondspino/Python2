import sqlite3
from os import close, name, system
from sqlite3.dbapi2 import connect
conn = sqlite3.connect(r"C:\Users\GGG\Desktop\งาน\งาน อ.หลิน\Week5\work6.db")
#c = conn.cursor()
#c.execute ('''CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT,
    #fname varchar(100) NOT NULL,
    #lName varchar(100) NOT NULL,
    #email varchar(100) NOT NULL,
    #Sex varchar(100) NOT NULL,
    #Age varchar(100) NOT NULL)''')
#conn.commit()
#conn.close()
def pick():
    global pick_no
    pick_no = input('\tกรุณาใส่หมายเลขนักเรียนที่ต้องการแก้ไข : ')
def pick1():
    global number
    number = input('\tกรุณาใส่หมายเลขนักเรียนที่ต้องลบ : ')
def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
def menu():
    global main
    print('*'*40,'\n','\tเพิ่มนักเรียน  [a]\n','\tแสดงข้อมูลนักเรียน [s]\n','\tแก้ไขข้อมูลนักเรียน [e]\n','\tลบข้อมูลนักเรียน   [d]\n','\tออกจากโปรแกรม  [x]\n','*'*40,'')
    main = str(input(' กรุราใส่รายการที่ต้องการ :'))
def database():
    global fname,lName,email,gender,Age,data1
    print('\n\t\t*** เพิ่มนักเรียน ***\n')
    data2 = []
    data1 = input('input fname,lName,email,gender,Age : ')
    data2 = data1.split(",")
    fname = data2[0]
    lName = data2[1]
    email = data2[2]
    gender = data2[3]
    Age = data2[4]
def database1():
    global fname,lName,email,gender,Age,data1
    print('\n\t*** เพิ่มข้อมูลนักเรียนที่ต้องการแก้ไข   ***\n')
    data2 = []
    data1 = input('input fname,lName,email,gender,Age : ')
    data2 = data1.split(",")
    fname = data2[0]
    lName = data2[1]
    email = data2[2]
    gender = data2[3]
    Age = data2[4]
def insert (fname,lName,email,gender,Age) :
    try :
        conn = sqlite3.connect (r"C:\Users\GGG\Desktop\งาน\งาน อ.หลิน\Week5\work6.db")
        c = conn.cursor()

        sql = '''INSERT INTO users (fname,lname,email,gender,Age) VALUES (?,?,?,?,?)'''
        data = (fname,lName,email,gender,Age)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed try again : ',e)
    finally :

        if conn :
            conn.close ()
def show():
    print('\n\t\t\t*** แสดงข้อมูลนักเรียน ***\n')
    print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5}\n'.format('No','fname','lname','email','gender','Age'))
    with sqlite3.connect(r"C:\Users\GGG\Desktop\งาน\งาน อ.หลิน\Week5\work6.db") as con:
        con.row_factory = sqlite3.Row
        show1="SELECT * FROM users "
        for row in con.execute(show1):
            print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5}'.format(row["no"],row["fname"],row["lname"],row["email"],row["gender"],row["Age"]))
def edit() :
    pick()
    database1()
    conn = sqlite3.connect (r"C:\Users\GGG\Desktop\งาน\งาน อ.หลิน\Week5\work6.db")
    c = conn.cursor()
    update_data = (fname,lName,email,gender,Age,pick_no)
    c.execute ('''UPDATE users SET fname = ?,lName = ?,email = ?,gender = ?,Age = ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
def delete():
    pick1()
    conn = sqlite3.connect(r"C:\Users\GGG\Desktop\งาน\งาน อ.หลิน\Week5\work6.db")
    c = conn.cursor()
    c.execute('''DELETE FROM users WHERE No = ?''',number)
    conn.commit()
    conn.close()
while True:
    menu()
    if main == 'a':
        database()
        insert(fname,lName,email,gender,Age)
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif main == 's':
        show()
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif main == 'e':
        edit()
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif main == 'd':
        delete()
        print('\n\tทำรายการเสร็จสิ้น\n')
    elif main == 'x':
        print('\tออกจากดปรแกรม')
        e=str(input('\tต้องการออกจาระบบหรือไม่ yes/no : '))
        if e == 'yes':
            clear()
            break
    else:
        print('\n\tError try again\n')