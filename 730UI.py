import tkinter as tk
from tkinter import ttk
  

  
class tkinterApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
         
        container = tk.Frame(self) 
        container.pack()
  

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

        file = open("live_data.csv", "r")
        lines = file.readlines()
  
        count = 0

        for line in lines:
            count += 1
            if(count != 1):
                parsed_tokens = line.strip().split(",")
                print("Timestamp: {}".format(parsed_tokens[0]))
                count2 = 0
                for token in parsed_tokens[1:150]:
                    print("Value {}: {}".format(count2, token))
                    count2 +=1
                print("Classification: {}".format(parsed_tokens[151]))

        file.close() 
   
      
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=512, width=1024, bg="#263D42")
        canvas.grid(row = 0, column = 0, padx = 10, pady = 10)
        canvas.create_text(200, 100, text="Spike Count", fill="white", font=('Helvetica 40 bold'))

        frame = tk.Frame(self, bg="white")
        frame.place(relwidth=0.5, relheight=0.5, relx=0.4, rely=0.2)

        
app = tkinterApp()
app.mainloop()
