import matplotlib
matplotlib.use("TKAgg")

from tkinter import *
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        Tk.iconbitmap(self, default="usericon.ico")
        Tk.wm_title(self, "Fund Transfer Service")

        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "Start Page", font = LARGE_FONT)
        label.pack(padx = 10, pady =10)

        button1 = ttk.Button(self, text = "Visit Page 1", command = lambda : controller.show_frame(PageOne))
        button1.pack()



class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "Page One", font = LARGE_FONT)
        label.pack(padx = 10, pady =10)

        button1 = ttk.Button(self, text = "Go Back", command = lambda : controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "Page Two", font = LARGE_FONT)
        label.pack(padx = 10, pady =10)

        button1 = ttk.Button(self, text = "Go Back", command = lambda : controller.show_frame(PageOne))
        button1.pack()

app = SeaofBTCapp()
app.mainloop()
