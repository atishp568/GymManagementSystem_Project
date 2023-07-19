import tkinter as tk
import tkinter.messagebox as mb
import random
import tkinter.ttk as ttk
import mysql.connector

db_connection= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '')
db_cursor= db_connection.cursor(buffered= True)


class EmployeeWindow(tk.Toplevel):
        def __init__(self,parent):
            super().__init__(parent)
            self.original_frame = parent
            self.geometry("1366x768")
            self.title("EmployeeWindow")
            self.configure(bg="lightblue")
            self.lblHeading= tk.Label(self,text= "Employee Login", font= ("Helvetica", 16), bg= "yellow",fg="blue")
            self.photo=tk.PhotoImage(file="loginlogo.png")
            self.label=tk.Label(self,image=self.photo)
            self.label.image=self.photo
            self.label.place(x=20,y=150)

            self.lblemail= tk.Label(self,text= "Enter Email ID: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.lblpsswd= tk.Label(self,text= "Enter Password: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.txtemail= tk.Entry(self,width=60)
            self.txtpasswd= tk.Entry(self,width=60, show= "*")
            self.btn_login= tk.Button(self, text= "Login",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.login)
            self.btn_clear= tk.Button(self, text= "Clear",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.clear_form)
            self.btn_signup= tk.Button(self, text= "Sign Up",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.open_employeeregistration_window)
            self.btn_exit= tk.Button(self, text= "Exit",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.exit)

            self.lblHeading.place(relx= 0.52, rely= 0.089, height=41,width=2500,anchor="center")
            self.lblemail.place(relx= 0.242, rely= 0.289, height=21, width= 106)
            self.lblpsswd.place(relx= 0.242, rely= 0.378, height=21, width= 102)
            self.txtemail.place(relx= 0.417, rely= 0.289, height=20, relwid= 0.273)
            self.btn_clear.place(relx= 0.54, rely= 0.489, height=24, width=100)
            self.btn_signup.place(relx= 0.400, rely= 0.489, height=24, width=100)
            self.txtpasswd.place(relx= 0.417, rely= 0.378, height=20, relwidth= 0.273)
            self.btn_login.place(relx= 0.242, rely= 0.489, height=24, width=100)
            self.btn_exit.place(relx= 0.70, rely= 0.489, height=24, width=100)

        def open_login_success_window(self):
            self.withdraw()
            window2=Admission(self)
            window2.grab_set()

        def login(self):
            print("hello")
            if db_connection.is_connected() ==False:
                db_connection.connect()
            
            #db_cursor.execute("CREATE DATABASE IF NOT EXISTS tanveer2")
            #db_cursor.execute("use gymdata")
            #db_cursor.execute("Create table if not exists Employee(email VARCHAR(30) NOT NULL PRIMARY KEY,password VARCHAR(30), name VARCHAR(30)")
            #db_connection.commit()
            
            try:
                global email
                email = str(self.txtemail.get())
                passwd = str(self.txtpasswd.get())
                if email == "" :
                    mb.showinfo('Information','Please Enter Email id')
                    self.txtemail.focus_set()
                    return
                if passwd== "":
                    mb.showinfo('Information','Please Enter Password')
                    self.txtpasswd.focus_set()
                    return

                print(email)
                print(passwd)
                query= "SELECT * FROM Employee WHERE email= '" + email + "' AND password= '" + passwd + "'"
                print(query)
                db_cursor.execute('Use gymdata')
                db_cursor.execute(query)
                rowcount= db_cursor.rowcount
                print(rowcount)
                if db_cursor.rowcount == 1:
                    mb.showinfo('Information','Loggedin Successfully')
                    self.open_login_success_window()
                    
                else:
                    mb.showinfo('Information','Login Invalid Email id or Password. Try again!')
            except:
                db_connection.disconnect()


        def clear_form(self):
            self.txtemail.delete(0, tk.END)
            self.txtpasswd.delete(0, tk.END)

        def exit(self):
            Msgbox = mb.askquestion('Exit Application','Are you sure you want to exit the application?',icon= 'warning')

            if Msgbox == 'yes':
                self.destroy()

        def open_employeeregistration_window(self):
             window1=EmployeeRegistrationWindow(self)
             window1.grab_set()
        


class EmployeeRegistrationWindow(tk.Toplevel):
        def __init__(self,parent):
            super().__init__(parent)
            self.original_frame = parent
            self.geometry("1366x768")
            self.title("EmployeeWindow")
            self.configure(bg="lightblue")
            self.lblHeading= tk.Label(self,text= "Employee Registration Form", font= ("Helvetica", 16), bg= "yellow",fg="blue")
            self.photo=tk.PhotoImage(file="loginlogo.png")
            self.label=tk.Label(self,image=self.photo)
            self.label.image=self.photo
            self.label.place(x=20,y=150)

            self.lblname= tk.Label(self,text= "Enter Name: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.lblemail= tk.Label(self,text= "Enter Email ID: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.lblpsswd= tk.Label(self,text= "Enter Password: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.txtname= tk.Entry(self,width=60)
            self.txtemail= tk.Entry(self,width=60)
            self.txtpasswd= tk.Entry(self,width=60, show= "*")
            self.btn_login= tk.Button(self, text= "Login",font= ("Helvetica", 11), bg= "yellow",fg="blue")
            self.btn_clear= tk.Button(self, text= "Clear",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.clear_form)
            self.btn_signup= tk.Button(self, text= "Sign Up",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.register)
            self.btn_exit= tk.Button(self, text= "Exit",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.exit)

            self.lblHeading.place(relx= 0.52, rely= 0.089, height=41,width=2500,anchor="center")
            self.lblname.place(relx= 0.242, rely= 0.210, height=21, width= 106)
            self.lblemail.place(relx= 0.242, rely= 0.289, height=21, width= 106)
            self.lblpsswd.place(relx= 0.242, rely= 0.378, height=21, width= 102)
            self.txtname.place(relx= 0.417, rely= 0.210, height=20, relwid= 0.273)
            self.txtemail.place(relx= 0.417, rely= 0.289, height=20, relwid= 0.273)
            self.btn_clear.place(relx= 0.54, rely= 0.489, height=24, width=100)
            self.btn_signup.place(relx= 0.400, rely= 0.489, height=24, width=100)
            self.txtpasswd.place(relx= 0.417, rely= 0.378, height=20, relwidth= 0.273)
            self.btn_login.place(relx= 0.242, rely= 0.489, height=24, width=100)
            self.btn_exit.place(relx= 0.70, rely= 0.489, height=24, width=100)

        def register(self):
        
            if db_connection.is_connected()== False:
                db_connection.connect()
            db_cursor.execute("CREATE DATABASE IF NOT EXISTS gymdata")
            db_cursor.execute("use gymdata")
            db_cursor.execute("Create table if not exists Employee(email VARCHAR(30) NOT NULL PRIMARY KEY,password VARCHAR(30), name VARCHAR(30))")
            db_connection.commit()
                
            name= self.txtname.get()
            email= self.txtemail.get()
            pwd= self.txtpasswd.get()

            if name== "":
                mb.showinfo('Information','Please Enter Your Name: ')
                self.txtname.focus_set()
                return
            if email== "":
                mb.showinfo('Information','Please Enter Email id: ')
                self.txtemail.focus_set()
                return
            if pwd== "":
                mb.showinfo('Information','Please Enter Password: ')
                self.txtpasswd.focus_set()
                return
            

            db_cursor.execute('Use gymdata')
            query= "INSERT INTO Employee (email,password,name) VALUES ('%s','%s','%s')" %(email,pwd,name)
            print(query)
            try:
                db_cursor.execute(query)
                mb.showinfo('Information', "Data inserted successfully")
                db_connection.commit()
            except:
                mb.showinfo('Information', "Data inserted failed")
                db_connection.rollback()
                db_connection.close()

        def onClose(self):
            self.destroy()
            self.original_frame.show()

        def clear_form(self):
            self.txtemail.delete(0, tk.END)
            self.txtpasswd.delete(0, tk.END)
            self.txtname.delete(0, tk.END)

        def exit(self):
            Msgbox = mb.askquestion('Exit Application','Are you sure you want to exit the application?',icon= 'warning')

            if Msgbox == 'yes':
                self.destroy()

class Admission(tk.Toplevel): 
    def __init__(self,parent):
            super().__init__(parent)
            self.original_frame = parent
            self.title("POWERHUB GYM - MEMBER ADMISSION FORM")
            self.geometry("1366x768")
            self.configure(bg="lightblue")
            self.lblHeading= tk.Label(self,text= "Member Admission Form", font= ("Helvetica", 16), bg= "yellow",fg="blue")
            self.photo=tk.PhotoImage(file="loginimage.png")
            self.label=tk.Label(self,image=self.photo)
            self.label.image=self.photo
            self.label.place(x=10,y=100)
            self.lblHeading.place(relx= 0.52, rely= 0.089, height=41,width=2500,anchor="center")


            self.label_1=tk.Label(self,text="NAME",anchor="w",width=10,font=("bold",15))
            self.label_1.place(x=155,y=100)
            self.entry_1=tk.Entry(self,bg="pink",width=30,font=("bold",15))
            self.entry_1.place(x=300,y=100)

            self.label_2=tk.Label(self,text="ADDRESS",anchor="w",width=10,font=("bold",15))
            self.label_2.place(x=155,y=150)
            self.entry_2=tk.Entry(self,width=30,bg="pink",font=("bold",15))
            self.entry_2.place(x=300,y=150)

            self.label_3=tk.Label(self,text="AGE",anchor="w",width=10,font=("bold",15))
            self.label_3.place(x=155,y=200)
            self.entry_3=tk.Entry(self,width=30,bg="pink",font=("bold",15))
            self.entry_3.place(x=300,y=200)

            self.label_4=tk.Label(self,text="EMAIL ID",anchor="w",width=10,font=("bold",15))
            self.label_4.place(x=155,y=250)
            self.entry_4=tk.Entry(self,width=30,bg="pink",font=("bold",15))
            self.entry_4.place(x=300,y=250)

            self.label_5=tk.Label(self,text="MOBILE",anchor="w",width=10,font=("bold",15))
            self.label_5.place(x=155,y=300)
            self.entry_5=tk.Entry(self,width=30,bg="pink",font=("bold",15))
            self.entry_5.place(x=300,y=300)

            self.label_6=tk.Label(self,text="DIET",anchor="w",width=10,font=("bold",15))
            self.label_6.place(x=155,y=350)
            food_list=["Veg","Non Veg"]
            self.ft=tk.StringVar()
            self.food_type=tk.OptionMenu(self,self.ft, *food_list)
            self.food_type.config(width=20,bg="pink",font=("bold",15))
            self.ft.set("Select Food Type")
            self.food_type.place(x=300,y=350)

            self.label_7=tk.Label(self,text="GENDER",anchor="w",width=10,font=("bold",15))
            self.label_7.place(x=155,y=400)
            self.gen=tk.StringVar()
            self.R1=tk.Radiobutton(self,text="Male",font=("bold",15),variable=self.gen,value="Male").place(x=300,y=400)
            self.R2=tk.Radiobutton(self,text="Female",font=("bold",15),variable=self.gen,value="Female").place(x=400,y=400)
            self.R3=tk.Radiobutton(self,text="Others",font=("bold",15),variable=self.gen,value="Others").place(x=500,y=400)
            self.gen.set(False)

            self.label_8=tk.Label(self,text="COURSE",anchor="w",width=10,font=("bold",15))
            self.label_8.place(x=155,y=450)
            course_list=["Cardio Running","Cardio Stairs Climber","Cardio Jumping Rope","Cardio Kettlebells","Cardio Cycling","Cardio Sprinting"]
            self.cr=tk.StringVar()
            self.course=tk.OptionMenu(self,self.cr,*course_list)
            self.course.config(width=20,bg="pink",font=("bold",15))
            self.cr.set("Select Course Type")
            self.course.place(x=300,y=450)

            self.label_9=tk.Label(self,text="COST",anchor="w",width=10,font=("bold",15))
            self.label_9.place(x=155,y=500)
            self.entry_9=tk.Entry(self,width=30,bg="pink",font=("bold",15))
            self.entry_9.place(x=300,y=500)

            self.label_10=tk.Label(self,text="SLOT",anchor="w",width=10,font=("bold",15))
            self.label_10.place(x=155,y=550)
            timeslot_list=["9-10 AM","10-11 AM","11-12 AM","4-5 PM","5-6 PM","6-7 PM"]
            self.slot=tk.StringVar()
            self.timeslot=tk.OptionMenu(self,self.slot,*timeslot_list)
            self.timeslot.config(width=20,bg="pink",font=("bold",15))
            self.slot.set("Select Slot")
            self.timeslot.place(x=300,y=550)

            self.label_11=tk.Label(self,text="TRAINER",anchor="w",width=10,font=("bold",15))
            self.label_11.place(x=155,y=600)
            self.entry_11=tk.Entry(self,width=30,bg="pink",font=("bold",15))
            self.entry_11.place(x=300,y=600)

            self.btn_submit= tk.Button(self, text= "Submit",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.submit)
            self.btn_clear= tk.Button(self, text= "Clear",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.clear_form)
            self.btn_exit= tk.Button(self, text= "Exit",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.exit)

            self.btn_submit.place(x=300,y=650, height=30, width=100)
            self.btn_clear.place(x=450,y=650, height=30, width=100)
            self.btn_exit.place(x=600,y=650, height=30, width=100)


    def submit(self):
        if db_connection.is_connected()== False:
            db_connection.connect()
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS gymdata")
        db_cursor.execute("use gymdata")
        db_cursor.execute("Create table if not exists Member(ID INTEGER PRIMARY KEY AUTO_INCREMENT, NAME TEXT NOT NULL, ADDRESS CHAR(50), AGE INT NOT NULL, EMAIL TEXT NOT NULL, MOBILE INT NOT NULL, FOOD_TYPE TEXT NOT NULL, GENDER TEXT NOT NULL, COURSE TEXT NOT NULL, COST INT NOT NULL, SLOT TEXT NOT NULL, TRAINER_NAME TEXT NOT NULL)")
        db_connection.commit()

        name= self.entry_1.get()
        address= self.entry_2.get()
        age= self.entry_3.get()
        email= self.entry_4.get()
        mobile= self.entry_5.get()
        food= self.ft.get()
        gender= self.gen.get()
        course= self.cr.get()
        cost= self.entry_9.get()
        slot= self.slot.get()
        trainer= self.entry_11.get()


        if name== "":
            mb.showinfo('Information','Please Enter Your Name: ')
            self.entry_1.focus_set()
            return
        if address== "":
            mb.showinfo('Information','Please Enter Your Address: ')
            self.entry_2.focus_set()
            return
        if age== "":
            mb.showinfo('Information','Please Enter Your Age: ')
            self.entry_3.focus_set()
            return
        if email== "":
            mb.showinfo('Information','Please Enter Email id: ')
            self.entry_4.focus_set()
            return
        if mobile== "":
            mb.showinfo('Information','Please Enter Your Mobile no: ')
            self.entry_5.focus_set()
            return
        if food== "":
            mb.showinfo('Information','Please Select Your Food Type: ')
            self.ft.focus_set()
            return
        if gender== "":
            mb.showinfo('Information','Please Select Your Gender: ')
            self.gen.focus_set()
            return
        if course== "":
            mb.showinfo('Information','Please Select Your Course: ')
            self.cr.focus_set()
            return
        if cost== "":
            mb.showinfo('Information','Please Enter The Cost: ')
            self.entry_9.focus_set()
            return
        if slot== "":
            mb.showinfo('Information','Please Select Your Slot: ')
            self.slot.focus_set()
            return
        if trainer== "":
            mb.showinfo('Information','Please Enter Your Trainer Name: ')
            self.entry_11.focus_set()
            return
        
        
            

        db_cursor.execute('Use gymdata')
        query= "INSERT INTO Member (NAME, ADDRESS, AGE, EMAIL, MOBILE, FOOD_TYPE, GENDER, COURSE, COST, SLOT, TRAINER_NAME) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(name,address,age,email,mobile,food,gender,course,cost,slot,trainer)
        print(query)
        try:
            db_cursor.execute(query)
            mb.showinfo('Information', "Data inserted successfully")
            db_connection.commit()
        except:
            mb.showinfo('Information', "Data inserted failed")
            db_connection.rollback()
            db_connection.close()

    
    def clear_form(self):
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.entry_3.delete(0, tk.END)
        self.entry_4.delete(0, tk.END)
        self.entry_5.delete(0, tk.END)
        self.ft.set("Select Food Type")
        self.gen.set(False)
        self.cr.set("Select Course Type")
        self.entry_9.delete(0, tk.END)
        self.slot.set("Select Slot")
        self.entry_11.delete(0, tk.END)

    def exit(self):
            Msgbox = mb.askquestion('Exit Application','Are you sure you want to exit the application?',icon= 'warning')

            if Msgbox == 'yes':
                self.destroy()

class AdminWindow(tk.Toplevel):
        def __init__(self,parent):
            super().__init__(parent)
            self.original_frame = parent
            self.geometry("1366x768")
            self.title("AdminWindow")
            self.configure(bg="lightblue")
            self.lblHeading= tk.Label(self,text= "Administrator Login", font= ("Helvetica", 16), bg= "yellow",fg="blue")
            self.photo=tk.PhotoImage(file="loginlogo.png")
            self.label=tk.Label(self,image=self.photo)
            self.label.image=self.photo
            self.label.place(x=20,y=150)

            self.lblemail= tk.Label(self,text= "Enter Email ID: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.lblpsswd= tk.Label(self,text= "Enter Password: ", font= ("Helvetica", 10), bg= "blue",fg="yellow")
            self.txtemail= tk.Entry(self,width=60)
            self.txtpasswd= tk.Entry(self,width=60, show= "*")
            self.btn_login= tk.Button(self, text= "Login",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.login)
            self.btn_clear= tk.Button(self, text= "Clear",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.clear_form)
            self.btn_exit= tk.Button(self, text= "Exit",font= ("Helvetica", 11), bg= "yellow",fg="blue",command=self.exit)

            self.lblHeading.place(relx= 0.52, rely= 0.089, height=41,width=2500,anchor="center")
            self.lblemail.place(relx= 0.242, rely= 0.289, height=21, width= 106)
            self.lblpsswd.place(relx= 0.242, rely= 0.378, height=21, width= 102)
            self.txtemail.place(relx= 0.417, rely= 0.289, height=20, relwid= 0.273)
            self.btn_clear.place(relx= 0.54, rely= 0.489, height=24, width=100)
            self.btn_login.place(relx= 0.400, rely= 0.489, height=24, width=100)
            self.txtpasswd.place(relx= 0.417, rely= 0.378, height=20, relwidth= 0.273)
            self.btn_exit.place(relx= 0.70, rely= 0.489, height=24, width=100)

        def login(self):
            email = str(self.txtemail.get())
            passwd = str(self.txtpasswd.get())
            if email == "" :
                    mb.showinfo('Information','Please Enter Email id')
                    self.txtemail.focus_set()
                    return
            if passwd== "":
                    mb.showinfo('Information','Please Enter Password')
                    self.txtpasswd.focus_set()
                    return
            
            if email=="admin@gmail.com" and passwd=="12345":
                mb.showinfo('Information','Loggedin Successfully')
                self.open_management_window()
            else:
                mb.showinfo('Information','Login Invalid Email id or Password. Try again!')

        def clear_form(self):
            self.txtemail.delete(0, tk.END)
            self.txtpasswd.delete(0, tk.END)

        def exit(self):
            Msgbox = mb.askquestion('Exit Application','Are you sure you want to exit the application?',icon= 'warning')

            if Msgbox == 'yes':
                self.destroy()

        def open_management_window(self):
            self.withdraw()
            window2=GymApp(self)
            window2.grab_set()


db_cursor = db_connection.cursor(buffered=True)
class GymApp(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.original_frame = parent
        self.title("Student Management System")
        self.geometry("800x650+351+174")
        self.lblTitle = tk.Label(self, text="Gym Management System", font=("Helvetica", 16), bg="yellow", fg="green")
        
        self.lblSelect = tk.Label(self, text="List of registered members", font=("Helvetica", 10), bg="blue", fg="yellow")
        self.lblSearch = tk.Label(self, text="Please Member ID:",font=("Helvetica", 10), bg="blue", fg="yellow")

        
        self.entSearch = tk.Entry(self)


       
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="yellow", fg="blue",
                                    command=self.delete_student_data)
        self.btn_show_all = tk.Button(self, text="Show All", font=("Helvetica", 11), bg="yellow", fg="blue",
                                   command=self.load_student_data)
        self.btn_search = tk.Button(self, text="Search", font=("Helvetica", 11), bg="yellow", fg="blue",
                                   command=self.show_search_record)
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 16), bg="yellow", fg="blue",command=self.exit)
        #NAME, ADDRESS, AGE, EMAIL, MOBILE, FOOD_TYPE, GENDER, COURSE, COST, SLOT, TRAINER_NAME
        columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12")
        self.tvStudent= ttk.Treeview(self,show="headings",height="5", columns=columns)
        self.tvStudent.heading('#1', text='ID', anchor='center')
        self.tvStudent.column('#1', width=60, anchor='center', stretch=False)
        self.tvStudent.heading('#2', text='Name', anchor='center')
        self.tvStudent.column('#2', width=60, anchor='center', stretch=False)
        self.tvStudent.heading('#3', text='Address', anchor='center')
        self.tvStudent.column('#3', width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#4', text='Age', anchor='center')
        self.tvStudent.column('#4',width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#5', text='Email', anchor='center')
        self.tvStudent.column('#5',width=10, anchor='center', stretch=True)
        self.tvStudent.heading('6', text='Mobile', anchor='center')
        self.tvStudent.column('#6',width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#7', text='Food type', anchor='center')
        self.tvStudent.column('#7', width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#8', text='Gender', anchor='center')
        self.tvStudent.column('#8', width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#9', text='Course', anchor='center')
        self.tvStudent.column('#9', width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#10', text='Cost', anchor='center')
        self.tvStudent.column('#10', width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#11', text='Slot', anchor='center')
        self.tvStudent.column('#11', width=10, anchor='center', stretch=True)
        self.tvStudent.heading('#12', text='Trainer name', anchor='center')
        self.tvStudent.column('#12', width=10, anchor='center', stretch=True)

        #Scroll bars are set up below considering placement position(x&y) ,height and width of treeview widget
        vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvStudent.yview)
        vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)
        self.tvStudent.configure(yscroll=vsb.set)
        hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvStudent.xview)
        hsb.place(x=40 , y=310+200+1, width=620 + 20)
        self.tvStudent.configure(xscroll=hsb.set)
        self.tvStudent.bind("<<TreeviewSelect>>")

        self.lblTitle.place(x=280, y=30,  height=27, width=300)
        self.lblSelect.place(x=150, y=280, height=23, width=400)
        self.lblSearch.place(x=174, y=560, height=23, width=134)

        self.entSearch.place(x=310, y=560, height=21, width=186)
        self.btn_delete.place(x=680, y=558, height=25, width=76)
        self.btn_show_all.place(x=580, y=558, height=25, width=76)
        self.btn_search.place(x=498, y=558, height=26, width=60)
        self.btn_exit.place(x=320, y=610,  height=31, width=60)
        self.tvStudent.place(x=40, y=310, height=200, width=640)
        self.load_student_data()

    def delete_student_data(self):
      MsgBox = mb.askquestion('Delete Record', 'Are you sure! you want to delete selected student record', icon='warning')
      if MsgBox == 'yes':
          if db_connection.is_connected() == False:
              db_connection.connect()
          db_cursor.execute("use gymdata")  # Interact with Student Database
          # deleteing selected student record
          Delete = "delete from member where ID='%s'" % (Id)
          db_cursor.execute(Delete)
          db_connection.commit()
          mb.showinfo("Information", "Student Record Deleted Succssfully")
          self.load_student_data()
          
    def show_search_record(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        global Id
        Id = self.entSearch.get()  # Retrieving entered first name
        print(Id)
        if  Id == "":
            mb.showinfo('Information', "Please Member Id")
            self.entSearch.focus_set()
            return
        self.tvStudent.delete(*self.tvStudent.get_children())  # clears the treeview tvStudent
        # Inserting record into student_master table of student database
        db_cursor.execute("use gymdata")  # Interact with Bank Database
        sql = "SELECT ID, NAME, ADDRESS, AGE, EMAIL, MOBILE, FOOD_TYPE, GENDER, COURSE, COST, SLOT, TRAINER_NAME FROM member where ID='" + Id + "'"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        #if total ==0:
            #mb.showinfo("Info", "Nothing To Display,Please add data")
            #return
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()

        Id = ""
        Name = ""
        Address = ""
        Age = ""
        Email = ""
        Mobile = ""
        Foodtype =""
        Gender =""
        Course=""
        Cost=""
        Slot=""
        Trainer=""
        for row in rows:
            Id = row[0]
            Name = row[1]
            Address = row[2]
            Age = row[3]
            Email = row[4]
            Mobile = row[5]
            Foodtype = row[6]
            Gender = row[7]
            Course = row[8]
            Cost = row[9]
            Slot = row[10]
            Trainer = row[11]
            print( Mobile)
            self.tvStudent.insert("", 'end', text=Id, values=(Id, Name, Address, Age, Email, Mobile, Foodtype, Gender, Course, Cost, Slot, Trainer))
        return Id

    def load_student_data(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        self.tvStudent.delete(*self.tvStudent.get_children())  # clears the treeview tvStudent
        # Inserting record into student_master table of student database
        db_cursor.execute("use gymdata")  # Interact with Bank Database
        sql = "SELECT ID, NAME, ADDRESS, AGE, EMAIL, MOBILE, FOOD_TYPE, GENDER, COURSE, COST, SLOT, TRAINER_NAME FROM member"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
        #if total ==0:
            #mb.showinfo("Info", "Nothing To Display,Please add data")
            #return
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()

        Id = ""
        Name = ""
        Address = ""
        Age = ""
        Email = ""
        Mobile = ""
        Foodtype =""
        Gender =""
        Course=""
        Cost=""
        Slot=""
        Trainer=""
        for row in rows:
            Id = row[0]
            Name = row[1]
            Address = row[2]
            Age = row[3]
            Email = row[4]
            Mobile = row[5]
            Foodtype = row[6]
            Gender = row[7]
            Course = row[8]
            Cost = row[9]
            Slot = row[10]
            Trainer = row[11]
            print( Mobile)
            self.tvStudent.insert("", 'end', text=Id, values=(Id, Name, Address, Age, Email, Mobile, Foodtype, Gender, Course, Cost, Slot, Trainer))



    def exit(self):
      MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
      if MsgBox == 'yes':
        self.destroy()


            
            
class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Homepage")
        self.geometry("1366x768")
        self.configure(bg="white")
        self.lblHeading= tk.Label(self,text= "***Welcome To Powerhub Gym***", font= ("Helvetica", 16), bg= "pink",fg="blue")
        self.img=tk.PhotoImage(file="gymlogo.png")
        self.label=tk.Label(self,image=self.img)
        self.label.image=self.img
        self.label.place(x=590,y=150)

        self.btn_employee= tk.Button(self, text= "Employee",font= ("Helvetica", 16), bg= "yellow",fg="blue",command=self.open_employee_window)
        self.btn_admin= tk.Button(self, text= "Admin",font= ("Helvetica", 16), bg= "yellow",fg="blue",command=self.open_admin_window)
        self.btn_exit= tk.Button(self, text= "Exit",font= ("Helvetica", 16), bg= "yellow",fg="blue",command=self.exit)

        self.lblHeading.place(relx= 0.52, rely= 0.089, height=41,width=2500,anchor="center")
        self.btn_employee.place(relx= 0.48, rely= 0.600, height=50, width= 150)
        self.btn_admin.place(relx= 0.48, rely= 0.700, height=50, width= 150)
        self.btn_exit.place(relx= 0.48, rely= 0.800, height=50, width= 150)

    def exit(self):
            Msgbox = mb.askquestion('Exit Application','Are you sure you want to exit the application?',icon= 'warning')

            if Msgbox == 'yes':
                self.destroy()
    
    def open_employee_window(self):
        #self.withdraw()
        window= EmployeeWindow(self)
        window.grab_set()

    def open_admin_window(self):
        #self.withdraw()
        window= AdminWindow(self)
        window.grab_set()

    
        

if __name__ == "__main__":
    app= HomePage()
    app.mainloop()