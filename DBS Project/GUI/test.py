import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


id = 0
balance = str()


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

    def getCategory(self):
        query = 'select * from category'
        self.cnx._execute_query(query)

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
        title_label = ttk.Label(self, text="WELCOME TO THE NUST BANKING SYSTEM", anchor=CENTER, font="Mistral  30").place(x=120, y=100, width=560, height=50)
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
        details_button = ttk.Button(self, text="Personal Details",  command = lambda:controller.show_frame(Details)).place(x=200, y=200, width=350, height=50)

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


class Password(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        cur_Password = ttk.Label(self, text="Current Password :",  font=" 20").place(x=200, y=200, width=150,
                                                                            height=50)
        cur_entry = ttk.Entry(self, text="Password", show = "*", font=20).place(x=350, y=200, width=200, height=50)

        new_label = ttk.Label(self, text="Card ID :", font=" 20").place(x=200, y=300, width=150,
                                                                                 height=50)
        new_entry = ttk.Entry(self, text="Card ID", font=20).place(x=350, y=300, width=200, height=50)

        ok_button = ttk.Button(self, text="Confirmed",
                           command=lambda: controller.show_frame(Options)).place(x=200, y=500, width=350, height=50)



class Balance(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)


        global balance

        bal_Label = ttk.Label(self, text ="Account Balance (PKR)",  font="Verdana 12").place(x=200, y=100, width=350, height=50)
        #amount_Label = ttk.Label(self, textvariable = balance,  font = 10).place(x=200, y=200, width=350, height=50)
        amount = Text(self).place(x=200, y=200, width=350, height=50)

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

        cnic_no = ttk.Label(self, text="CNIC : " + "XXXX",  font=20).place(x=200, y=100, width=350, height=50)
        name = ttk.Label(self, text="Name : " + "XXXX",  font=20).place(x=200, y=175, width=350,
                                                                                      height=50)
        ph_no = ttk.Label(self, text="Phone no : " + "XXXX",  font=20).place(x=200, y=250, width=350, height=50)
        city = ttk.Label(self, text="City : " + "XXXX", font=20).place(x=200, y=325, width=350,
                                                                                       height=50)
        address = ttk.Label(self, text="Address : " + "XXXX",  font=20).place(x=200, y=400, width=350,
                                                                                       height=50)

        return_button = ttk.Button(self, text="Return",
                               command=lambda: controller.show_frame(MainPage)).place(x=300, y=500, width=150,
                                                                                      height=30)

class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.mainloop()