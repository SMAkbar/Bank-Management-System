


'''

from tkinter import *

root =  Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text = "Button 1")
button2 = Button(topFrame, text = "Button 2")
button3 = Button(topFrame, text = "Button 3")
button4 = Button(topFrame, text = "Button 4")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = RIGHT)
button4.pack(side = RIGHT)

one = Label(root, text = "One", bg = "red", fg = "white")
one.pack()
two = Label(root, text = "two", bg = "red", fg = "white")
two.pack(fill = X)
three = Label(root, text = "three", bg = "red", fg = "white")
three.pack(side = LEFT, fill = Y)


theLabel = Label(root, text="This is really easy")
theLabel.pack()
root.mainloop()

root = Tk()

label_1 = Label(root, text = "Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 0, sticky = E)  #sticky can defined with N,W,E,S = North, West, East and South
entry_1.grid(row = 0, column = 1, columnspan = 2) #columnspan tell how many columns can cell span


label_2.grid(row = 1, sticky = E)
entry_2.grid(row = 1, column = 1)



root = Tk()

def printName(event):
    print("My name is Akbar")


def printLName():
    print("Syed")


button_1 = Button(root, text = "Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

button_2 = Button(root, text = "Print my last name", command = printLName)
button_2.pack()





class AkbarButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = "Print Message", command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.printButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow! this actually worked")



root = Tk()
b = AkbarButtons(root)
root.mainloop()




# ********* mini series ****************

root = Tk()

#**** Main Menu *****

def doNothing():
    print("Do nothing")

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "file", menu = subMenu)
subMenu.add_command(label = "Now project...", command = doNothing)
subMenu.add_command(label = "Now...", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command=doNothing)

#edit = Menu(menu)
editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label="Redo", command = doNothing)

# **** Toolbar ****

toolbar = Frame(root, bg = "blue")

insertButton = Button(toolbar, text = "Insert Image", command = doNothing)
insertButton.pack(side=LEFT, padx = 2, pady = 2)
printButton = Button(toolbar, text = "Print Image", command = doNothing)
printButton.pack(side=LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)


# **** status bar *****

status = Label(root, text = "preparing to do nothing", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)




import Tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()


###########################################################

try:
    import Tkinter as tk  ## Python 2.x
except ImportError:
    import tkinter as tk  ## Python 3.x


class DestroyTest():
    def __init__(self, top):
        self.top = top
        self.top.geometry("+10+10")
        self.frame = tk.Frame(self.top)
        self.frame.grid()
        test_label = tk.Label(self.frame, text="Label")
        test_label.grid(row=1, column=0)
        destroy_button = tk.Button(self.frame, text="Destroy Frame", \
                                   command=self.destroy)
        destroy_button.grid(row=10, column=0)
        exit_button = tk.Button(self.top, text="Exit", command=top.quit)
        exit_button.grid(row=10, column=0)

    def destroy(self):
        self.frame.destroy()
        self.new_toplevel = tk.Toplevel(self.top, takefocus=True)
        self.new_toplevel.geometry("+50+50")
        self.new_toplevel.grid()
        lbl = tk.Label(self.new_toplevel, text="New Toplevel")
        lbl.grid()


root = tk.Tk()
DT = DestroyTest(root)
root.mainloop()

import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

'''


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

        for F in (MainPage, PageOne, PageTwo, Options, Balance, Withdrawal, Transfer, Details):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Start Page")
        label.pack(padx=10, pady=10)
        page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
        page_one.pack()
        page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
        page_two.pack()


class MainPage(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        title_label = Label(self, text="Automatic Teller Machine (ATM)", anchor=CENTER, font="Mistral  30",
                            fg="white", bg="black").place(x=150, y=100, width=450, height=50)

        cardID_label = Label(self, text="Card ID :", anchor=E, font=" 20").place(x=200, y=200, width=150,
                                                                                       height=50)
        cardID_entry = Entry(self, text="Card ID", font=20).place(x=350, y=200, width=200, height=50)

        Pin_label = Label(self, text="Pin :", anchor=E, font="20").place(x=200, y=300, width=150,
                                                                                         height=50)
        Pin_entry = Entry(self, text="Pin", font=20, show="*").place(x=350, y=300, width=200, height=50)

        ok_button = Button(self, text="Enter!", anchor=CENTER, font=20, command = lambda:controller.show_frame(Options)).place(x=200, y=400, width=350, height=50)



class Options(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        bal_button = Button(self, text="Balance Enquiry", anchor=CENTER, font=20, command = lambda:controller.show_frame(Balance)).place(x=200, y=100, width=350, height=50)
        cash_button = Button(self, text="Cash Withdrawal", anchor=CENTER, font=20, command = lambda:controller.show_frame(Withdrawal)).place(x=200, y=200, width=350, height=50)
        trans_button = Button(self, text="Money Transfer", anchor=CENTER, font=20, command = lambda:controller.show_frame(Transfer)).place(x=200, y=300, width=350, height=50)
        details_button = Button(self, text="Card Details", anchor=CENTER, font=20, command = lambda:controller.show_frame(Details)).place(x=200, y=400, width=350, height=50)
        return_button = Button(self, text="Return", anchor=CENTER, font = 10, command = lambda:controller.show_frame(MainPage)).place(x=300, y=500, width=150, height=20)


class Balance(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        bal_Label = Button(self, text ="Account Balance", anchor = CENTER, font=10).place(x=200, y=100, width=350, height=50)
        amount_Label = Button(self, text = 1230, anchor = CENTER, font = 10).place(x=200, y=200, width=350, height=50)

        return_button = Button(self, text="Return", anchor=CENTER, font=10,
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                      height=20)


class Withdrawal(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        bal_Label = Label(self, text="Minimum amount of Cash Withdraw is 500", anchor=CENTER).place(x=200, y=100,
                                                                                                    width=350,
                                                                                                    height=20)
        bal_Label = Label(self, text="Maximum amount of Cash Withdraw is 10000", anchor=CENTER).place(x=200, y=120,
                                                                                                      width=350,
                                                                                                      height=20)

        amount_Entry = Entry(self, text="0.0", font=20).place(x=200, y=300, width=350, height=50)

        return_button = Button(self, text="Withdraw", anchor=CENTER, font=("Courier", 20),
                               command=lambda: controller.show_frame(Options)).place(x=200, y=400, width=350,
                                                                                     height=50)
        return_button = Button(self, text="Return", anchor=CENTER, font=10,
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                     height=30)


class Transfer(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        bal_Label = Label(self, text="Minimum amount of Cash Withdraw is 500", anchor=CENTER).place(x=200, y=100,
                                                                                                    width=350,
                                                                                                    height=20)
        bal_Label = Label(self, text="Maximum amount of Cash Withdraw is 10000", anchor=CENTER).place(x=200, y=120,
                                                                                                      width=350,
                                                                                                      height=20)

        account_label = Label(self, text="Send to (Acc #) :", anchor=E, font=" 20").place(x=200, y=200, width=150,
                                                                                          height=50)
        account_entry = Entry(self, text="Acc #", font=20).place(x=350, y=200, width=200, height=50)

        amount_label = Label(self, text="Amount :", anchor=E, font="20").place(x=200, y=300, width=150,
                                                                               height=50)
        amount_entry = Entry(self, text="Amount", font=20, show="*").place(x=350, y=300, width=200, height=50)

        return_button = Button(self, text="Transfer", anchor=CENTER, font=("Courier", 20),
                               command=lambda: controller.show_frame(Options)).place(x=200, y=400, width=350,
                                                                                     height=50)
        return_button = Button(self, text="Return", anchor=CENTER, font=10,
                               command=lambda: controller.show_frame(Options)).place(x=300, y=500, width=150,
                                                                                     height=30)


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


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page One")
        label.pack(padx=10, pady=10)
        start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.pack()
        page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
        page_two.pack()


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page Two")
        label.pack(padx=10, pady=10)
        start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
        start_page.pack()
        page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
        page_one.pack()


class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.mainloop()