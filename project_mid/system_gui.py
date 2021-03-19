from tkinter import * # นำเข้าโมดูลทั้งหมดใน tkinter  (เป็น library ที่มีคนทำไว้อยู่แล้ว)
from tkinter import messagebox 
import sqlite3 
from datetime import datetime
import socket # โมดูลสำหรับ ip 
import os
import sys



# Array Variable #
global script_dir
script_dir = sys.path[0]

Variable_font = {
    "ButtonFont": ("Bahnschrift",14),
    "LabelFont": ("Bahnschrift",14),
    "EntryFont": ("Bahnschrift",13),
    "Main_Entry": ("Bahnschrift",22),
    "AccountNumberFont": ("Bahnschrift",36),
    "BalanceFont": ("Bahnschrift",22),
    "User_POP_Font": ("Bahnschrift",26),
    "Deposit_Font": ("Bahnschrift",40),
    "HistoryFont": ("Bahnschrift",18),
    "UserFont": ("Bahnschrift",24)
}

def main_scren_func(): # mainscreen login gui
    mainscreen = Tk() # window  ต้อง import tkinter ก่อน
    mainscreen.geometry("1000x800") 
    mainscreen.title("Patrick & Diamond Bank")
    
    bg = PhotoImage(file= os.path.join(script_dir, '[img]\main_screen.png')) # import os 
    Label(mainscreen , image=bg).pack()
    
    username_from_entry = StringVar()
    password_from_entry = StringVar()
    
    Entry(mainscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["Main_Entry"],justify="center", textvariable= username_from_entry,bd=0).place(relx=0.363, rely=0.455,anchor='w', width="280", height="40")
    Entry(mainscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["Main_Entry"],justify="center",  show="*" ,textvariable= password_from_entry,bd=0).place(relx=0.363, rely=0.545,anchor='w', width="280", height="40")
    

    loginbtn_img = PhotoImage(file =os.path.join(script_dir, '[img]\login_btn.png')) 
    regisbtn_img = PhotoImage(file=os.path.join(script_dir, '[img]\\registermain_btn.png'))
    Button(mainscreen, text="Login", height="2", width="30",font=Variable_font["Main_Entry"],  command=lambda: login_system(username_from_entry.get(),password_from_entry.get(),mainscreen),image = loginbtn_img ,bd=0).place(relx=0.50, rely=0.7, anchor='s', width="200", height="50")
    Button(mainscreen, text="Register", height="2", width="30",font=Variable_font["Main_Entry"], command=lambda: register_screen_func(mainscreen),image=regisbtn_img,bd=0).place(relx=0.50, rely=0.78, anchor='s', width="200", height="50")
    
    lockscreen(mainscreen)
    mainscreen.eval('tk::PlaceWindow . center')
    mainscreen.mainloop()


######## LOGIN SYSTEM ########
def login_system(u,p,frame):
    try:
        
        if(u and p): 
            conn = connect_database()
            data = conn.cursor()
            data.execute("""SELECT id_account,username,first_name,last_name,phone,balance FROM user WHERE username=? AND password=?""", (u,p,)) #สร้าง cursor และ execute เพื่อดึงข้อมูลที่เราต้องการออกมา
            callback_data = data.fetchall() # เรียกใช้คำสั่ง fetchall เพื่อที่จะดึงข้อมูลที่กำหนดออกมา เก็บไว้ใน callbackdata เพื่อนำไปเช็คต่อ
            conn.commit()
            if( check_data_is_none(callback_data) ):#True
                
                messagebox.showinfo("Patrick & Diamond Bank", ("Login Successful : "+callback_data[0][1]+" "+callback_data[0][2]))
                backup=callback_data[0] 
                data_user = {
                    "id_account":backup[0], #callback_data[0][0]
                    "user":backup[1],
                    "f_name":backup[2],
                    "l_name":backup[3],
                    "phone":backup[4],
                    "balance":backup[5]
                }
                login_success_screen_func(data_user,frame)
            else:
                messagebox.showerror("Patrick & Diamond Bank : Error", "Username or Password Wrong ?!") 
                
            data.close()
        else:
            if(not u and not p):
                messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter The Username AND Password")
                
            elif(not p):
                messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter The Password !")
            else:
                messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter The Username !")
            
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table : ", error)


############### Insert register info to database ##########################
def insertregister (username_from_regis,password_from_regis,firstname_from_regis,lastname_from_regis,phone_from_regis,frame):
    try :
        conn = connect_database()
        sql = ''' INSERT INTO user (username,password,first_name,last_name,phone) VALUES (?,?,?,?,?) '''
        data = (username_from_regis,password_from_regis,firstname_from_regis,lastname_from_regis,phone_from_regis)
        c = conn.cursor()
        c.execute(sql,data)
        conn.commit()
        c.close()
        messagebox.showinfo("Successfull", "Congratulations. Register is complete.")
        deposit_for_register(500,fetch_all_data(username_from_regis),frame)

    except sqlite3.IntegrityError as e:
        print(e)
         


######################################## FRAME #######################################

def register_system(u,p,f_name,l_name,phone,frame):
    # CASE OF NULL ENTRY
    if(not u):
        messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter The Username")
        return
    else:
        if(len(u) > 20 or len(u) < 10):
            messagebox.showwarning("Patrick & Diamond Bank : Warning", "Username Must Have More Than 10 and Must Have Least Than 20 !")
            return

    conn = connect_database()
    data = conn.cursor()
    data.execute("""SELECT username FROM user WHERE username=?""", (u,))
    callback_data = data.fetchall()
    conn.commit()
    if( check_data_is_none(callback_data) ):
        messagebox.showerror("Patrick & Diamond Bank", "This USERNAME Is Already Taken!")
        conn.close()
        return
    else:
        conn.close()

    if(not p):
        messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter The Password")
        return
    else:
        if(len(p) > 30 or len(p) < 10):
            messagebox.showwarning("Patrick & Diamond Bank : Warning", "Password Must Have More Than 10 and Must Have Least Than 30 !")
            return
        letter_count=0
        numeric_count=0
        for character in p:
            if(character.isalpha()):
                letter_count+=1
            if(character.isnumeric()):
                numeric_count+=1
        
        if(letter_count<2):
            messagebox.showwarning("Patrick & Diamond Bank : Warning", "Error : Must have at least two English letter !")
            return
        elif(numeric_count<2):
            messagebox.showwarning("Patrick & Diamond Bank : Warning", "Error : Must have at least two Numeric !")
            return

    if(not f_name):
        messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter First Name")
        return
    if(not l_name):
        messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter Last Name")
        return

    if(not phone):
        messagebox.showwarning("Patrick & Diamond Bank : Warning", "Please Enter Phone")
        return

                
    if(len(phone) != 10):
        messagebox.showwarning("Patrick & Diamond Bank : Warning", "Phone Number Must have only 10 degits !")
        return
    
    insertregister (u,p,f_name,l_name,phone,frame)



######## CONNECT TO DATABASE SYSTEM ########
def connect_database():
    try:
        # Join various path components
        return sqlite3.connect(os.path.join(script_dir, 'bankkk.db'))
    except sqlite3.Error as error:
        print("\n\n\n\nFailed to Connection : ",error)



def check_data_is_none(data):
    try:
        data[0] # if data not Null it's gonna return TRUE meaning have this customer and user pass correct !
        return True
    except:
        return False


######################################## FRAME #######################################

def logout_system(frame,data,isLogout): #logout_popup,data,True
    if(isLogout):
        frame.destroy()
        main_scren_func()
    else:
        login_success_screen_func(data,frame)
        

def logout_popup(frame,data):
    frame.destroy()
    logout_popup = Tk()
    logout_popup.geometry("400x200")
    logout_popup.title("Logout !")
    bg = PhotoImage(file= os.path.join(script_dir, '[img]\logout_popup.png'))
    Label(logout_popup , image=bg , borderwidth=0).pack()

    yes_pop = PhotoImage(file = os.path.join(script_dir, '[img]\yes_pop.png'))
    no_pop = PhotoImage(file =os.path.join(script_dir, '[img]\\no_pop.png'))
    Label(logout_popup, font=Variable_font["User_POP_Font"], text=data["user"], bg="#07071f",fg="#fff").place(relx=0.65, rely=0.075, anchor='n')
    Button(logout_popup, text="YES", height="2", width="30",font=Variable_font["Main_Entry"], image=yes_pop ,fg="#a10000",command=lambda: logout_system(logout_popup,data,True),bd=0).place(relx=0.25, rely=0.78, anchor='s', width="150", height="50")
    Button(logout_popup, text="NO", height="2", width="30",font=Variable_font["Main_Entry"], image=no_pop ,fg="#fff",command=lambda: logout_system(logout_popup,data,False),bd=0).place(relx=0.75, rely=0.78, anchor='s', width="150", height="50")
    logout_popup.protocol("WM_DELETE_WINDOW",lambda: logout_system(logout_popup,data,False))

    lockscreen(logout_popup)
    logout_popup.eval('tk::PlaceWindow . center')

    logout_popup.mainloop()


def registerscreen_out(frame):
    ask = messagebox.askquestion('Exit Register','Back to Login Screen ?',icon = 'warning')

    if(ask=='yes'):
        frame.destroy()
        main_scren_func()
    else:
        return


def transfer_screen(data, frame):
    frame.destroy()
    balance = "${:,.2f}".format(data["balance"])
    transferscreen = Tk()
    transferscreen.geometry("1000x800")
    transferscreen.title("TRANSFER")

    amount_of_transfer = DoubleVar()
    number_of_transfer = StringVar()
    number_of_transfer.set("0")

    bg=PhotoImage(file=os.path.join(script_dir, '[img]\\transfer_screen.png'))
    Label(transferscreen, image=bg , borderwidth=0).pack()
    Label(transferscreen, font=Variable_font["BalanceFont"], text=balance, bg="#39394c",fg="#fff700").place(relx=0.8185, rely=0.178, anchor='n')
    Entry(transferscreen, bg="#050517", fg="#fff", font=Variable_font["Deposit_Font"], justify="center",textvariable=number_of_transfer,bd=0).place(relx=0.03, rely=0.35,anchor='w', width="600", height="80")
    Entry(transferscreen, bg="#050517", fg="#2aff00", font=Variable_font["Deposit_Font"], justify="center",textvariable=amount_of_transfer,bd=0).place(relx=00, rely=0.814,anchor='w', width="1000", height="80")
    Button(transferscreen, text="TRANSFER", height="2", width="30",bg="#07071f",fg="#fffc00",font=Variable_font["Main_Entry"], command=lambda: transfer_system(amount_of_transfer.get(), data, number_of_transfer.get(),transferscreen),bd=0).place(relx=0.85, rely=0.975, anchor='s', width="200", height="50")
    Button(transferscreen, text="BACK", height="2", width="30",bg="#07071f",fg="#d80303",font=Variable_font["Main_Entry"], command=lambda: login_success_screen_func(fetch_all_data(data["user"]),transferscreen),bd=0).place(relx=0.14, rely=0.975, anchor='s', width="200", height="50")
    transferscreen.protocol("WM_DELETE_WINDOW",lambda: login_success_screen_func(fetch_all_data(data["user"]),transferscreen))
    lockscreen(transferscreen)
    transferscreen.eval('tk::PlaceWindow . center')

    transferscreen.mainloop()


def deposit_screen(data, frame):
    frame.destroy()
    balance = "${:,.2f}".format(data["balance"])
    depositscreen = Tk()
    depositscreen.geometry("1000x800")
    depositscreen.title("DEPOSIT")

    amount_of_deposit = DoubleVar()
    
    bg=PhotoImage(file=os.path.join(script_dir, '[img]\deposit_screen.png'))
    Label(depositscreen, image=bg , borderwidth=0).pack()
    Label(depositscreen, font=Variable_font["BalanceFont"], text=balance, bg="#39394c",fg="#fff700").place(relx=0.5, rely=0.3, anchor='n')
    Entry(depositscreen, bg="#050517", fg="#2aff00", font=Variable_font["Deposit_Font"], justify="center",textvariable=amount_of_deposit,bd=0).place(relx=00, rely=0.807,anchor='w', width="1000", height="80")
    Button(depositscreen, text="DEPOSIT", height="2", width="30",bg="#07071f",fg="#0bff05",font=Variable_font["Main_Entry"], command=lambda: deposit_system(amount_of_deposit.get(),data,depositscreen),bd=0).place(relx=0.85, rely=0.95, anchor='s', width="200", height="50")
    Button(depositscreen, text="BACK", height="2", width="30",bg="#07071f",fg="#d80303",font=Variable_font["Main_Entry"], command=lambda: login_success_screen_func(fetch_all_data(data["user"]),depositscreen),bd=0).place(relx=0.14, rely=0.95, anchor='s', width="200", height="50")
    depositscreen.protocol("WM_DELETE_WINDOW",lambda: login_success_screen_func(fetch_all_data(data["user"]),depositscreen))
    lockscreen(depositscreen)
    depositscreen.eval('tk::PlaceWindow . center')
    depositscreen.mainloop()


def withdraw_screen(data, frame):
    frame.destroy()
    balance = "${:,.2f}".format(data["balance"])
    whithdrawscreen = Tk()
    whithdrawscreen.geometry("1000x800")
    whithdrawscreen.title("WITHDRAW")

    amount_of_withdraw = DoubleVar()
    
    bg=PhotoImage(file=os.path.join(script_dir, '[img]\withdraw_screen.png'))
    Label(whithdrawscreen, image=bg , borderwidth=0).pack()
    Label(whithdrawscreen, font=Variable_font["BalanceFont"], text=balance, bg="#39394c",fg="#fff700").place(relx=0.495, rely=0.3, anchor='n')
    Entry(whithdrawscreen, bg="#050517", fg="#2aff00", font=Variable_font["Deposit_Font"], justify="center",textvariable=amount_of_withdraw,bd=0).place(relx=00, rely=0.807,anchor='w', width="1000", height="80")
    Button(whithdrawscreen, text="WITHDRAW", height="2", width="30",bg="#07071f",fg="#0bff05",font=Variable_font["Main_Entry"], command=lambda: withdraw_system(amount_of_withdraw.get(),data,whithdrawscreen),bd=0).place(relx=0.85, rely=0.95, anchor='s', width="200", height="50")
    Button(whithdrawscreen, text="BACK", height="2", width="30",bg="#07071f",fg="#d80303",font=Variable_font["Main_Entry"], command=lambda: login_success_screen_func(fetch_all_data(data["user"]),whithdrawscreen),bd=0).place(relx=0.14, rely=0.95, anchor='s', width="200", height="50")
    whithdrawscreen.protocol("WM_DELETE_WINDOW",lambda: login_success_screen_func(fetch_all_data(data["user"]),whithdrawscreen))
    lockscreen(whithdrawscreen)
    whithdrawscreen.eval('tk::PlaceWindow . center')
    whithdrawscreen.mainloop()

def update_database(where_value,where,value): #"balance","username",(data["balance"],data["user"])
    try:
        sqliteConnection = connect_database()
        cursor = sqliteConnection.cursor()
        sql = ''' UPDATE user SET '''+where_value+''' = ? WHERE '''+where+''' = ?'''
        cursor = sqliteConnection.cursor()
        cursor.execute(sql, value)#ดำเนินการ
        sqliteConnection.commit()

    except sqlite3.Error as error:
        sqliteConnection.close()


def insert_database(where_value,value,how_many): # "history(id_account,amount,date_time,from_name,type)",(data["id_account"], str(amount) , str_date , data["user"] , "DEPOSIT") , ?????
    try:
        sqliteConnection = connect_database()
        cursor = sqliteConnection.cursor()
        sql = ''' INSERT INTO '''+where_value+''' VALUES('''+how_many+''') ''' 
        cursor = sqliteConnection.cursor()
        cursor.execute(sql, value)
        sqliteConnection.commit() #doit
#howmany = ?,?,?,?,? 
    except sqlite3.Error as error:
        sqliteConnection.close()
    

def withdraw_system(amount,data,frame): #amount_of_withdraw.get(),data,whithdrawscreen
    if(amount>0):
        if(amount <= data["balance"]):
            ask = messagebox.askquestion('CONFIRMATION','WITHDRAW AMOUNT : '+str(amount),icon = 'info')
            if(ask=="yes"):

                from_ip = socket.gethostbyname(socket.gethostname())
                data["balance"]-=amount
                str_date = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")

                update_database("balance","username",(data["balance"],data["user"])) 
                insert_database( "history(id_account,amount,date_time,from_name,type,ip)",(data["id_account"], str(amount) , str_date , data["user"] , "WITHDRAW", from_ip) , "?,?,?,?,?,?") ## WTF ERRORRRRRR KUY PONG TAI SUS MAE YED

                messagebox.showinfo("Patrick & Diamond Bank", "Withdraw Successfully Amount "+str(amount)+" \n[ DATE "+str(str_date)+" ]")

                login_success_screen_func(fetch_all_data(data["user"]),frame)
        else:
            messagebox.showerror("Patrick & Diamond Bank", "Your balance has "+str("${:,.2f}".format(data["balance"]))+"$")
    else:
        messagebox.showerror("Patrick & Diamond Bank", "Cannot Withdraw 0$ or less than 0$")


def transfer_system(amount,data,data_to,frame): #(amount_of_transfer.get(), data, number_of_transfer.get(),transferscreen, ))
    if(data_to != "0"):
        if(data_to != str(data['id_account'])):
            data_to = fetch_all_data_bykey(data_to) #ม่อน
            if(data_to):
                if(amount>0):
                    if(amount <= data["balance"]):
                        ask = messagebox.askquestion('CONFIRMATION','TRANSFER AMOUNT : '+str(amount)+"$\n ID|"+str(data_to["id_account"])+" USER|"+ data_to["user"],icon = 'info')
                        if(ask=="yes"):
                            data["balance"]-=amount
                            data_to["balance"]+=amount
                            str_date = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")

                            #USER UPDATE
                            update_database("balance","username",(data["balance"],data["user"])) 
                            insert_database( "history(id_account,amount,date_time,from_name,type)",(data["id_account"], str(amount) , str_date , data_to["user"] , "TRANSFER") , "?,?,?,?,?") ## WTF ERRORRRRRR KUY PONG TAI SUS MAE YED
                            
                            #TO USER UPDATE
                            update_database("balance","username",(data_to["balance"],data_to["user"])) 
                            insert_database( "history(id_account,amount,date_time,from_name,type)",(data_to["id_account"], str(amount) , str_date , data["user"] , "RECIEVE") , "?,?,?,?,?") ## WTF ERRORRRRRR KUY PONG TAI SUS MAE YED

                            messagebox.showinfo("Patrick & Diamond Bank", "Transfer Successfully Amount "+str(amount)+"\nID|"+str(data_to["id_account"])+" USER|"+data_to["user"]+" \n[ DATE "+str(str_date)+" ]")
                            login_success_screen_func(fetch_all_data(data["user"]),frame)
                    else:
                        messagebox.showerror("Patrick & Diamond Bank", "Your balance has "+str("${:,.2f}".format(data["balance"]))+"$")
                else:
                    messagebox.showerror("Patrick & Diamond Bank", "Cannot Transfer With 0$ or less than 0$")
            else:
                messagebox.showerror("Patrick & Diamond Bank", "Not Found Account Number  ")
        else:
            messagebox.showerror("Patrick & Diamond Bank", "Cannot Transfer to your self !!!")
    else:
            messagebox.showerror("Patrick & Diamond Bank", "Insert Account Number for Transfer to !")
        

def deposit_system(amount,data,frame):
    if(amount>0):
        ask = messagebox.askquestion('CONFIRMATION','DEPOSIT AMOUNT : '+str(amount))
        if(ask=="yes"):
            data["balance"]+=amount
            str_date = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")

            update_database("balance","username",(data["balance"],data["user"])) 
            insert_database( "history(id_account,amount,date_time,from_name,type)",(data["id_account"], str(amount) , str_date , data["user"] , "DEPOSIT") , "?,?,?,?,?") ## WTF ERRORRRRRR KUY PONG TAI SUS MAE YED

            messagebox.showinfo("Patrick & Diamond Bank", "Deposit Successfully Amount "+str(amount)+" \n[ DATE "+str(str_date)+" ]")

            login_success_screen_func(fetch_all_data(data["user"]),frame) 
    else:
        messagebox.showerror("Patrick & Diamond Bank", "Cannot Deposit 0$ or less than 0$")

def deposit_for_register(amount,data,frame):
    data["balance"]+=amount
    str_date = datetime.now().strftime("%d-%m-%Y : %H:%M:%S")
    
    update_database("balance","username",(data["balance"],data["user"]))  # UPDATE BALANCE IN USER TABLE
    insert_database( "history(id_account,amount,date_time,from_name,type)",(data["id_account"], str(amount) , str_date , data["user"] , "DEPOSIT") , "?,?,?,?,?") ## WTF ERRORRRRRR KUY PONG TAI SUS MAE YED
    messagebox.showinfo("Patrick & Diamond Bank", "Deposit Successfully Amount "+str(amount)+" \n[ DATE "+str(str_date)+" ]")

    login_success_screen_func(fetch_all_data(data["user"]),frame)

def fetch_all_data(username): # data['user']
    conn = connect_database()
    data = conn.cursor()
    data.execute("""SELECT id_account,username,first_name,last_name,phone,balance FROM user WHERE username=?""", (username,))
    callback_data = data.fetchall()
    conn.commit()
    if( check_data_is_none(callback_data) ):
        backup=callback_data[0]
        data_user = {
            "id_account":backup[0],# callbackdata[0][0]
            "user":backup[1],
            "f_name":backup[2],
            "l_name":backup[3],
            "phone":backup[4],
            "balance":backup[5] # [0][5]
        }
        
        return data_user

def fetch_all_data_bykey(key):
    conn = connect_database()
    data = conn.cursor()
    data.execute("""SELECT id_account,username,first_name,last_name,phone,balance FROM user WHERE id_account=?""", (int(key),))
    callback_data = data.fetchall()
    conn.commit()
    if( check_data_is_none(callback_data) ):
        backup=callback_data[0]
        data_user = {
            "id_account":backup[0],
            "user":backup[1],
            "f_name":backup[2],
            "l_name":backup[3],
            "phone":backup[4],
            "balance":backup[5]
        }
        return data_user


def pull_deposit_history(key):
    conn = connect_database()
    data = conn.cursor()
    data.execute("""SELECT amount,date_time,from_name,type,ip FROM history WHERE id_account=?""", (key,))
    callback_data = data.fetchall()
    conn.commit()
    if( check_data_is_none(callback_data) ):
        return callback_data
            
            

def lockscreen(frame):
    frame.resizable(width=False, height=False)


def login_success_screen_func(data,frame):

    '''
        "id_account" : callback_data[0][0] = backup[0]
        "user"
        "f_name"
        "l_name"
        "phone"
        "balance"
        key : value
    '''
    frame.destroy()
    loginscreen = Tk()

    
    loginscreen.geometry("1000x800")
    loginscreen.title("Patrick & Diamond Bank")


    deposit_btn = PhotoImage(file=os.path.join(script_dir, '[img]\deposit_btn.png'))
    withdraw_btn = PhotoImage(file=os.path.join(script_dir, '[img]\withdraw_btn.png'))
    tranfer_btn = PhotoImage(file=os.path.join(script_dir, '[img]\\transfer_btn.png'))
    logout_btn = PhotoImage(file=os.path.join(script_dir, '[img]\logout_btn.png'))
    bg = PhotoImage(file=os.path.join(script_dir, '[img]\login_screen.png'))
    Label(loginscreen , image=bg ).pack()
    Label(loginscreen, font=Variable_font["AccountNumberFont"], text=data["id_account"], bg="#07071f",fg="#e60553").place(relx=0.363, rely=0.018, anchor='n')
    Label(loginscreen, font=Variable_font["UserFont"], text= data["user"], bg="#07071f",fg="#e60553").place(relx=0.42, rely=0.174, anchor='n')
    Label(loginscreen, font=Variable_font["UserFont"], text= (data["f_name"],data["l_name"]), bg="#07071f",fg="#e60553").place(relx=0.44, rely=0.234, anchor='n')
    Label(loginscreen, font=Variable_font["UserFont"], text= data["phone"], bg="#07071f",fg="#e60553").place(relx=0.40, rely=0.287, anchor='n')
    Label(loginscreen, font=Variable_font["BalanceFont"], text= "${:,.2f}".format(data["balance"]), bg="#39394c",fg="#fff700").place(relx=0.811, rely=0.175, anchor='n')
    Button(loginscreen, image=deposit_btn,bd=0, command= lambda:deposit_screen(data,loginscreen)).place(relx=0.135, rely=0.555, anchor='s', width="200", height="50")
    Button(loginscreen, image=withdraw_btn,bd=0, command=lambda:withdraw_screen(data,loginscreen)).place(relx=0.355, rely=0.555, anchor='s', width="200", height="50")
    Button(loginscreen, image=tranfer_btn,bd=0 , command=lambda: transfer_screen(data , loginscreen )).place(relx=0.575, rely=0.555, anchor='s', width="200", height="50")
    Button(loginscreen, image=logout_btn,bd=0 , command=lambda: logout_popup(loginscreen,data)).place(relx=0.865, rely=0.555, anchor='s', width="200", height="50")


    history_scrollbar = Scrollbar(loginscreen,bd=0)
    history_scrollbar.pack(side=TOP, fill= Y)

    history_box = Listbox(loginscreen, yscrollcommand=history_scrollbar.set , bg="#07071f", fg="#fff", font= Variable_font["HistoryFont"] )
    data_history_pulled = pull_deposit_history( str(data["id_account"] )) 
    if(data_history_pulled): # มารูปแบบตาราง
        for his in data_history_pulled: 
            if his[3] == "DEPOSIT": # row ก่อน (แนวนอน)
                history_box.insert(END, "DEPOSIT 🏐 | 💲 : "+"${:,.2f}".format(his[0])+"          🕜 | "+his[1])  
            elif his[3] == "TRANSFER":
                history_box.insert(END, "TRANSFER | 💲 : "+str(his[0])+"      ▶️"+his[2]+"          🕜 | "+his[1]) 
            elif his[3] == "RECIEVE":
                history_box.insert(END, "RECIEVE | 💲 : "+str(his[2])+"      ◀️"+his[2]+"          🕜 | "+his[1])  
            elif his[3] == "WITHDRAW":
                history_box.insert(END, "WITHDRAW | 💲 : "+str(his[0])+"      🌎"+his[4]+"          🕜 | "+his[1])  

    else:
        history_box.insert(END, "🏐 NOTHING HISTORY")  



    history_box.place(relx=0.5, rely=0.96, anchor='s', width="940", height="300")
    # history_scrollbar.config(command=history_box) #.yview
    loginscreen.protocol("WM_DELETE_WINDOW",lambda: logout_popup(loginscreen,data))

    lockscreen(loginscreen)
    loginscreen.eval('tk::PlaceWindow . center')
    loginscreen.mainloop()




def register_screen_func(frame):
    frame.destroy()
    
    registerscreen = Tk()
    registerscreen.geometry("800x400")
    registerscreen.title("Register")
    
    bg = PhotoImage(file= os.path.join(script_dir, '[img]\\register_screen.png') )
    Label(registerscreen , image=bg ).pack()

    username_from_regis = StringVar()
    password_from_regis = StringVar()
    firstname_from_regis = StringVar()
    lastname_from_regis = StringVar()
    phone_from_regis = StringVar()

    Entry(registerscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["EntryFont"], justify="center",bd=0,textvariable= username_from_regis).place(relx=0.37, rely=0.355,anchor='w', width="200", height="30")
    Entry(registerscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["EntryFont"], show="*",bd=0, justify="center",textvariable= password_from_regis).place(relx=0.375, rely=0.455,anchor='w', width="200", height="30")
    Entry(registerscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["EntryFont"], justify="center",bd=0,textvariable= firstname_from_regis).place(relx=0.375, rely=0.55,anchor='w', width="150", height="30")
    Entry(registerscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["EntryFont"], justify="center",bd=0,textvariable=lastname_from_regis).place(relx=0.69, rely=0.555,anchor='w', width="150", height="30")
    Entry(registerscreen, bg="#1d1d1d", fg="#fff", font=Variable_font["EntryFont"], justify="center",bd=0,textvariable= phone_from_regis).place(relx=0.335, rely=0.655,anchor='w', width="170", height="30")

    
    btn_img = PhotoImage(file = os.path.join(script_dir, '[img]\\register_btn.png')) 
    Button(registerscreen, command=lambda: register_system( 
        username_from_regis.get(),
        password_from_regis.get(),
        firstname_from_regis.get(),
        lastname_from_regis.get(),
        phone_from_regis.get(),
        registerscreen
    )
    ,image = btn_img,bd=2).place(relx=0.55, rely=0.975, anchor='s', width="200", height="40")

    Button(registerscreen, text="BACK", height="2", width="30",bg="#07071f",fg="#d80303",font=Variable_font["Main_Entry"], command=lambda: registerscreen_out(registerscreen),bd=2).place(relx=0.15, rely=0.95, anchor='s', width="200", height="30")

    registerscreen.protocol("WM_DELETE_WINDOW",lambda: registerscreen_out(registerscreen))

    lockscreen(registerscreen)
    registerscreen.eval('tk::PlaceWindow . center')
    registerscreen.mainloop()
    


