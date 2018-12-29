from tkinter import *

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
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
        Frame.__init__(self, master)
        title_label = Label(self, text="WELCOME SIR", anchor=CENTER, font="Mistral  30",
                            fg="white", bg="black").place(x=120, y=100, width=560, height=50)
        name_label = Label(self, text="Name :", anchor=E, font=" 20").place(x=200, y=200, width=150,
                                                                                 height=50)
        name_entry = Entry(self, text="Name", font=20).place(x=350, y=200, width=200, height=50)

        Password_label = Label(self, text="Password :", anchor=E, font="20").place(x=200, y=300, width=150,
                                                                                         height=50)
        Password_entry = Entry(self, text="Password", font=20, show="*").place(x=350, y=300, width=200, height=50)

        ok_button = Button(self, text="Enter!", anchor=CENTER, font=20, command = lambda:controller.show_frame(Options)).place(x=200, y=500, width=350, height=50)





class Options(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        create_button = Button(self, text="Create New Account", anchor=CENTER, font=20, command = lambda:controller.show_frame(Balance)).place(x=200, y=100, width=350, height=50)

        pass_button = Button(self, text="Change Password", anchor=CENTER, font=10,
                             command=lambda: controller.show_frame(Password)).place(x=630, y=550, width=150,
                                                                                    height=20)

class Password(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        cur_Password = Label(self, text="Current Password :", anchor=E, font=" 20").place(x=200, y=200, width=150,
                                                                            height=50)
        cur_entry = Entry(self, text="Password", show = "*", font=20).place(x=350, y=200, width=200, height=50)

        new_label = Label(self, text="Card ID :", anchor=E, font=" 20").place(x=200, y=300, width=150,
                                                                                 height=50)
        new_entry = Entry(self, text="Card ID", font=20).place(x=350, y=300, width=200, height=50)

        ok_button = Button(self, text="Confirmed", anchor=CENTER, font=20,
                           command=lambda: controller.show_frame(MainPage)).place(x=200, y=500, width=350, height=50)



class Balance(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        bal_Label = Label(self, text ="Account Balance", anchor = CENTER, font=10).place(x=200, y=100, width=350, height=50)
        amount_Label = Label(self, text = "Total Amount (PKR) = " + "Koi bhe number" + "/=", anchor = CENTER, font = 10).place(x=200, y=200, width=350, height=50)

        return_button = Button(self, text="Return", anchor=CENTER, font=10,
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                      height=20)



class Details(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        bal_Label = Label(self, text ="Minimum amount of Cash Withdraw is 500", anchor = CENTER).place(x=200, y=100, width=350, height=50)
        bal_Label = Label(self, text ="Maximum amount of Cash Withdraw is 10000", anchor = CENTER).place(x=200, y=150, width = 350, height=50)
        amount_Entry = Entry(self, text = "0.0", font = 20).place(x=200, y=300, width=350, height=50)

        return_button = Button(self, text="Withdraw", anchor=CENTER, font = ("Courier", 20),
                               command=lambda: controller.show_frame(Options)).place(x=200, y=400, width=350,
                                                                                     height=50)
        return_button = Button(self, text="Return", anchor=CENTER, font=10,
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
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