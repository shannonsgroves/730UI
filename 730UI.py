import tkinter as tk
from tkinter import ttk
import pandas as pd

class tkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Spike counter')
        container = tk.Frame(self) 
        container.pack()
  
        # container.grid_rowconfigure(0, weight = 1)
        # container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
  
        for F in (LoginPage, Page1):
  
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(LoginPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=512, width=1024, bg="#263D42")
        canvas.place(x=0,y=0)
        canvas.create_text(500, 50, text="Login Page", fill="white", font=('Helvetica 40 bold'))

        userName = tk.StringVar()
        userNameBox = tk.Entry(self, textvariable=userName)
        userNameBox.place(x=400, y=100)

        newUser = tk.Button(self, text="Create User", padx=10, pady=5, fg="black", bg="#263D42",
        command = lambda : controller.show_frame(Page1))
        newUser.place(x=425, y=150)

        userName = tk.StringVar()
        userNameBox = tk.Entry(self, textvariable=userName)
        userNameBox.place(x=400, y=250)

        newUser = tk.Button(self, text="Login", padx=10, pady=5, fg="black", bg="#263D42",
        command = lambda : controller.show_frame(Page1))
        newUser.place(x=450, y=300)

class Page1(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=512, width=1024, bg="#263D42")
        canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
        canvas.create_text(200, 100, text="Spike Count", fill="white", font=('Helvetica 40 bold'))

        frame = tk.Frame(self, bg="white")
        frame.place(relwidth=0.5, relheight=0.5, relx=0.4, rely=0.2)

        start_button = tk.Button(self, text="Start", padx=10, pady=5, fg="black", bg="#263D42",
                          command = self.testFunc)
        start_button.place(relx = 0.05, rely=0.8)

        end_button = tk.Button(self, text="Stop", padx=10, pady=5, fg="black", bg="#263D42",
                          command=self.endCounter)
        end_button.place(relx=0.15, rely=0.8)

        reset_button = tk.Button(self, text="Reset", padx=10, pady=5, fg="black", bg="#263D42",
                               command=self.reset)
        reset_button.place(relx=0.25, rely=0.8)

    def testFunc(self):
        global num
        global flag

        num = num+1
        if flag == 1:
            num = 0
            flag = 0
            return

        str1 = tk.StringVar(value=str(num))
        counter = tk.Label(self, textvariable=str1, bg="#263D42", fg="white", font=('Helvetica 180'))
        counter.place(relx=0.15, rely=0.3)
        counter.after(1000, self.testFunc)

    def endCounter(self):
        global flag
        flag = 1
    #
    # def reset(self):
    #     self.

if __name__ == "__main__":
    flag = 0
    num = 0
    app = tkinterApp()
    app.mainloop()
