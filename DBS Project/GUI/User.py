import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


id = 0
balance = str()

#cnic_no, name, ph_no, city
cnic_no = name = ph_no = city = str()
password = str()


class SQLconnector:
    def __init__(self):
        prop = {
            "user": "root",
            'password': 'zxcvbn',
            'host': '127.0.0.1',
            'database': 'bank',

        }
        self.cnx = mysql.connector.connect(**prop)
        self.cursor = self.cnx.cursor()
    def getBalance(self):
        global id
        print(id)
        query = f'select * from userData where AccountNo = {id};'
        # where name = {name} and password = {password}
        self.cnx._execute_query(query)

    def getDetails(self):
        global id
        query = f'select * from userData where AccountNo = {id};'
        self.cnx._execute_query(query)

    def getPassword(self):
        global id
        query = f'select * from userData where AccountNo = {id};'
        self.cnx._execute_query(query)

    def changePassword(self, pas):
        global id
        #print(f'update person as p join accounts as acc using (CNIC) join address as ad using (CNIC) join card as c using (accountno) join customer as cus using (CNIC) set Passwords = \"{pas}\" where AccountNo = {id}')
        query = f'update person as p join accounts as acc using (CNIC) join address as ad using (CNIC) join card as c using (accountno) join customer as cus using (CNIC) set Passwords = \"{pas}\" where AccountNo = {id}'
        self.cnx._execute_query(query)
        self.cnx.commit()

    def login(self, name, password):
        print(name, password)
        query = 'select * from userData where name like \"' + str(name)+'\" and passwords like \"' + str(password)+'\";'
        # where name = {name} and password = {password}
        self.cnx._execute_query(query)

    def getResultSet(self):
        global id
        em = []
        for i in self.cursor:
            em.append(list(i))
        print(em[0])
        id = em[0][0]
        print(id)
        return em[0]



'''
if __name__ == '__main__':
    sql = SQLconnection()
    sql.getBalance(1)
    result = sql.getResultSet()

    print(str(result[0][7])[:4])
'''


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.iconbitmap(self, default="usericon.ico")
        Tk.wm_title(self, "Fund Transfer Service")

        #Setup Menu
        MainMenu(self)
        #Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.geometry("800x600")
        self.resizable(0, 0)
        self.frames = {}

        for F in (MainPage, Options, Balance, Details, Password):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)


    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class MainPage(Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        self.mysql = SQLconnector()

        self.name = StringVar()
        self.password = StringVar()

        Frame.__init__(self, master)
        title_label = ttk.Label(self, text="WELCOME TO THE FUND TRANSFER SYSTEM", anchor=CENTER, font="Mistral 30").place(x=100, y=100, width=600, height=50)
        name_label = ttk.Label(self, text="Name :", anchor=E).place(x=200, y=200, width=100,
                                                                                 height=50)
        name_entry = ttk.Entry(self, text="Name", textvariable = self.name).place(x=300, y=210, width=200, height=30)

        #cardID_label = ttk.Label(self, text="Card ID :", anchor=E, font=" 20").place(x=200, y=300, width=150, height=50)
        #cardID_entry = ttk.Entry(self, text="Card ID", font=20).place(x=350, y=300, width=200, height=50)

        password_label = ttk.Label(self, text="Password :", anchor=E).place(x=200, y=300, width=100,
                                                                                         height=50)
        password_entry = ttk.Entry(self, text="Password", show="*", textvariable = self.password).place(x=300, y=310, width=200, height=30)

        #mysql.login(name_entry, password_entry)
        #mysql.getResultSet()

        ok_button = ttk.Button(self, text="Enter!",  command = self.login).place(x=200, y=500, width=350, height=50)


    def login(self):
        #print(self.name.get(), self.password.get())
        self.mysql.login(self.name.get(), self.password.get())
        dummy = self.mysql.getResultSet()
        #res = result[0]
        #id = result[0][0]
        #print(id)
        self.controller.show_frame(Options)



class Options(Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        self.mysql = SQLconnector()

        Frame.__init__(self, master)

        bal_button = ttk.Button(self, text="Balance Enquiry",  command = self.gotoBalance).place(x=200, y=100, width=350, height=50)
        details_button = ttk.Button(self, text="Personal Details",  command = self.gotoDetails).place(x=200, y=200, width=350, height=50)

        #ok_button = ttk.Button(self, text="Enter!", command=self.refresh).place(x=200, y=400, width=350, height=50)


        pass_button = ttk.Button(self, text="Change Password", command=lambda: controller.show_frame(Password)).place(x=630, y=550, width=150,
                                                                                    height=30)



    def gotoBalance(self):
        global balance
        self.mysql.getBalance()
        dummy = self.mysql.getResultSet()
        balance = str(dummy[5])
        print(balance)
        #Balance.amount_Label.Refresh()
        self.controller.show_frame(Balance)

    def gotoDetails(self):
        global cnic_no, name, ph_no, city
        self.mysql.getDetails()
        dummy = self.mysql.getResultSet()
        cnic_no = dummy[1]
        name = dummy[2]
        ph_no = dummy[4]
        city = dummy[6]
        #print(balance)
        # Balance.amount_Label.Refresh()
        self.controller.show_frame(Details)


class Password(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.controller = controller
        self.mysql = SQLconnector()
        self.current = StringVar()
        self.new = StringVar()


        cur_Password = ttk.Label(self, text="Current Password :").place(x=200, y=200, width=150,
                                                                            height=50)
        cur_entry = ttk.Entry(self, text="Password", show = "*", font=20, textvariable = self.current).place(x=350, y=200, width=200, height=50)

        new_label = ttk.Label(self, text="New Password :").place(x=200, y=300, width=150,
                                                                                 height=50)
        new_entry = ttk.Entry(self, text="Password", show = "*", font=20, textvariable = self.new).place(x=350, y=300, width=200, height=50)



        ok_button = ttk.Button(self, text="Confirmed",
                           command=self.changePassword).place(x=200, y=400, width=350, height=50)


        return_button = ttk.Button(self, text="Return",
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                      height=30)


    def changePassword(self):
        global password
        self.mysql.getPassword()
        dummy = self.mysql.getResultSet()
        password = dummy[3]
        print(self.current.get() + " == " + password)
        if self.current.get() == password:
            self.mysql.changePassword(self.new.get())
            messagebox.showinfo(message = "Password has been changed! NEW PASSWORD = ")
            self.controller.show_frame(Options)
        else:
            messagebox.showerror(message="Wrong Current Password")




class Balance(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)


        global balance

        bal_Label = ttk.Label(self, text ="Account Balance (PKR)",  font="Verdana 20").place(x=200, y=100, width=350, height=50)
        #amount_Label = ttk.Label(self, textvariable = balance,  font = 10).place(x=200, y=200, width=350, height=50)
        amount_Label = ttk.Label(self, text="XXXX", font="Verdana 20", anchor=CENTER).place(x=200, y=200, width=350,
                                                                                            height=50)

        refresh_button = ttk.Button(self, text="Refresh", command = lambda:self.refresh(master, controller)).place(x=300, y=400, width=150, height=30)

        return_button = ttk.Button(self, text="Return",
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                      height=30)

    def refresh(self, master, controller):
        global balance

        amount_label = Label(self, text = "PKR " + balance + " Only", font = "Verdana 20").place(x=200, y=200, width=350, height=50)





class Details(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)


        cnic_label = ttk.Label(self, text="CNIC : ",  font=20).place(x=200, y=100, width=200, height=50)
        name_label = ttk.Label(self, text="Name : ",  font=20).place(x=200, y=175, width=200,
                                                                                      height=50)
        ph_label = ttk.Label(self, text="Phone no : ",  font=20).place(x=200, y=250, width=200, height=50)
        city_label = ttk.Label(self, text="City : ", font=20).place(x=200, y=325, width=200,
                                                                                       height=50)

        refresh_button = ttk.Button(self, text="Refresh", command=lambda: self.refresh(master, controller)).place(x=300,
                                                                                                                  y=430,
                                                                                                                  width=150,
                                                                                                                  height=30)

        return_button = ttk.Button(self, text="Return",
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                      height=30)

    def refresh(self, master, controller):
        global cnic_no, name, ph_no, city
        cnic_label = ttk.Label(self, text= cnic_no,  font=20).place(x=400, y=100, width=350, height=50)
        name_label = ttk.Label(self, text= name, font=20).place(x=400, y=175, width=200, height=50)
        ph_label = ttk.Label(self, text= ph_no, font=20).place(x=400, y=250, width=200, height=50)
        city_label = ttk.Label(self, text=city, font=20).place(x=400, y=325, width=200, height=50)




class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.mainloop()