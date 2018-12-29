import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


accountno = 0
card_no = 0
balance = 0
limit = 0
name = str()


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

    def getTuple(self):
        global accountno
        query = f'select * from atm where accountno = {accountno};'
        self.cnx._execute_query(query)

    def getCash(self, cash):
        global accountno, balance, limit
        limit = limit - 1
        balance = balance - cash
        query = f'update atm set balance = {balance} where accountno = {accountno};'
        self.cnx._execute_query(query)
        self.cnx.commit()

    def transfer(self, cash, to):
        global accountno, balance, limit
        limit = limit - 1
        query = f'select * from atm where cardNo = {to};'
        self.cnx._execute_query(query)
        dummy = self.getResultSet()
        if accountno != dummy[1]:
            query = f'update atm set balance = balance + {cash} where accountno = {to};'
            self.cnx._execute_query(query)
            self.cnx.commit()
            balance = balance - cash
            query = f'update atm set balance = {balance} where AccountNo = {accountno};'
            self.cnx._execute_query(query)
            self.cnx.commit()
            messagebox.showinfo(message = "Transfer Complete")
        else:
            messagebox.showerror(message = "You cannot tranfer money to the same account")

    def login(self, cardNo, pin):
        print(cardNo, pin)
        query = 'select * from atm where cardNo = \"' + str(cardNo)+'\" and pin = \"' + str(pin)+'\";'
        self.cnx._execute_query(query)

    def getResultSet(self):
        em = []
        for i in self.cursor:
            em.append(list(i))
        print(em[0])
        return em[0]



class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.iconbitmap(self, default="usericon.ico")
        Tk.wm_title(self, "Automatic Teller Machine")

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

        for F in (MainPage, Options, Balance, Withdrawal, Transfer, Details):
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

        self.card = StringVar()
        self.pin = StringVar()

        Frame.__init__(self, master)
        title_label = ttk.Label(self, text="THE FTS ATM", anchor=CENTER, font="Mistral  30").place(x=120, y=100, width=560, height=50)
        name_label = ttk.Label(self, text="CARD # :", anchor=E).place(x=200, y=200, width=100,
                                                                                 height=50)
        name_entry = ttk.Entry(self, text="card", textvariable = self.card).place(x=300, y=210, width=200, height=30)
        password_label = ttk.Label(self, text="PIN :", anchor=E).place(x=200, y=300, width=100,
                                                                                         height=50)
        password_entry = ttk.Entry(self, text="pin", show="*", textvariable = self.pin).place(x=300, y=310, width=200, height=30)
        ok_button = ttk.Button(self, text="Enter!",  command = self.login).place(x=200, y=500, width=350, height=50)


    def login(self):
        global accountno, balance, limit, name, card_no
        self.mysql.login(self.card.get(), self.pin.get())
        dummy = self.mysql.getResultSet()
        accountno = dummy[1]
        balance = dummy[7]
        limit = dummy[5]
        card_no = dummy[2]
        name = dummy[9]
        print(name)
        self.controller.show_frame(Options)




class Options(Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        self.mysql = SQLconnector()
        Frame.__init__(self, master)


        bal_button = ttk.Button(self, text="Balance Enquiry",  command = lambda :controller.show_frame(Balance)).place(x=200, y=100, width=350, height=50)
        cash_button = ttk.Button(self, text="Cash Withdrawal",  command = lambda:controller.show_frame(Withdrawal)).place(x=200, y=200, width=350, height=50)
        trans_button = ttk.Button(self, text="Money Transfer",  command = lambda:controller.show_frame(Transfer)).place(x=200, y=300, width=350, height=50)
        details_button = ttk.Button(self, text="Card Details", command = lambda:controller.show_frame(Details)).place(x=200, y=400, width=350, height=50)
        exit_button = ttk.Button(self, text="Exit", command = lambda : exit(1)).place(x=300, y=500, width=150, height=30)



class Balance(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        bal_Label = ttk.Label(self, text ="Account Balance (PKR)",  font="Verdana 20").place(x=200, y=100, width=350, height=50)
        amount_Label = ttk.Label(self, text ="XXXX",  font="Verdana 20", anchor = CENTER).place(x=200, y=200, width=350, height=50)
        refresh_button = ttk.Button(self, text="Refresh", command = lambda:self.refresh(master, controller)).place(x=300, y=400, width=150, height=30)
        return_button = ttk.Button(self, text="Return", command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150, height=30)

    def refresh(self, master, controller):
        global balance
        amount_label = Label(self, text = "PKR " + str(balance) + " Only", font = "Verdana 20").place(x=200, y=200, width=350, height=50)



class Withdrawal(Frame):
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        self.mysql = SQLconnector()
        Frame.__init__(self, master)
        self.cash = StringVar()
        bal_Label = ttk.Label(self, text="Minimum amount of Cash Withdraw is 500", anchor=CENTER).place(x=200, y=100,
                                                                                                    width=350,
                                                                                                    height=20)
        bal_Label = ttk.Label(self, text="Maximum amount of Cash Withdraw is 10000", anchor=CENTER).place(x=200, y=120,
                                                                                                      width=350,
                                                                                                      height=20)

        amount_Entry = ttk.Entry(self, text="0.0", font=20, textvariable = self.cash).place(x=200, y=300, width=350, height=50)

        ok_button = ttk.Button(self, text="Withdraw", command = self.withdrawCash).place(x=200, y=400, width=350,
                                                                                     height=50)
        return_button = ttk.Button(self, text="Return", command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                     height=30)

    def withdrawCash(self):
        global balance
        req = int(self.cash.get())
        if req <= balance and limit > 0 and (req >= 500 and req <= 10000):
            self.mysql.getCash(req)
            messagebox.showinfo(message = "Press OK if you recieved cash")
            self.controller.show_frame(Options)
        elif req >= 500 and req <= 10000:
            messagebox.showerror(message="Please enter a value between 500 and 10000")
        elif limit == 0:
            messagebox.showerror(message = "Limit of transaction crossed")
        else:
            messagebox.showerror(message = "Not enough Balance")


class Transfer(Frame):
    def __init__(self, master, controller):
        self.amount = StringVar()
        self.to = StringVar()

        self.controller = controller
        self.master = master
        self.mysql = SQLconnector()

        Frame.__init__(self, master)

        bal_Label = ttk.Label(self, text="Minimum amount of Cash Withdraw is 500", anchor=CENTER).place(x=200, y=100,
                                                                                                    width=350,
                                                                                                    height=20)
        bal_Label = ttk.Label(self, text="Maximum amount of Cash Withdraw is 10000", anchor=CENTER).place(x=200, y=120,
                                                                                                      width=350,
                                                                                                      height=20)

        account_label = ttk.Label(self, text="Send to (Acc #) :", anchor=E, font=" 20").place(x=200, y=200, width=150,
                                                                                          height=50)
        account_entry = ttk.Entry(self, text="Acc #", textvariable = self.to).place(x=350, y=200, width=200, height=50)

        amount_label = ttk.Label(self, text="Amount :", anchor=E, font="20").place(x=200, y=300, width=150,
                                                                               height=50)
        amount_entry = ttk.Entry(self, text="Amount", textvariable = self.amount).place(x=350, y=300, width=200, height=50)

        return_button = ttk.Button(self, text="Transfer",command=self.transferCash).place(x=200, y=400, width=350,
                                                                                     height=50)
        return_button = ttk.Button(self, text="Return",command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                     height=30)

    def transferCash(self):
        global balance
        #print(self.amount.get())
        req = int(self.amount.get())
        if req <= balance and limit > 0 and (req >= 500 and req <= 10000):
            self.mysql.transfer(req, self.to.get())
            self.controller.show_frame(Options)
        elif req >= 500 and req <= 10000:
            messagebox.showerror(message="Please enter a value between 500 and 10000")
        elif limit == 0:
            messagebox.showerror(message = "Limit of transaction crossed")
        else:
            messagebox.showerror(message = "Not enough Balance")

class Details(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        name_Label = ttk.Label(self, text="Name : ", anchor=W, font=20).place(x=200, y=100, width=200, height=50)
        acc_label = ttk.Label(self, text="Account no : ", anchor=W, font=20).place(x=200, y=200, width=200,
                                                                                      height=50)
        limit_label = ttk.Label(self, text="Limit : ", anchor=W, font=20).place(x=200, y=300, width=200, height=50)
        refresh_button = ttk.Button(self, text="Refresh", command=lambda: self.refresh(master, controller)).place(x=300,
                                                                                                                  y=430,
                                                                                                                  width=150,
                                                                                                                  height=30)
        nme = ttk.Label(self, text= "XXXX", font=20).place(x=400, y=100, width=100, height=50)
        acc = ttk.Label(self, text= "XXXX", font=20).place(x=400, y=200, width=200, height=50)
        lim = ttk.Label(self, text= "XXXX", font=20).place(x=400, y=300, width=350, height=50)

        return_button = ttk.Button(self, text="Return", command=lambda: controller.show_frame(MainPage)).place(x=300, y=500, width=150,
                                                                                      height=30)

    def refresh(self, master, controller):
        global accountno, limit, name
        print(name)
        nme = ttk.Label(self, text= name, font=20).place(x=400, y=100, width=300, height=50)
        acc = ttk.Label(self, text= accountno, font=20).place(x=400, y=200, width=200, height=50)
        lim = ttk.Label(self, text= limit,  font=20).place(x=400, y=300, width=350, height=50)




class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.mainloop()