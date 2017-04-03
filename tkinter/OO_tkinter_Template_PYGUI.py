import tkinter as tk
from tkinter import ttk

day = 1
LARGE_FONT= ("Verdana", 12)
starttext = """This Game is still in development
Please keep that in mind.
Nothing in this is the final product."""
def nextday():
    global day
    day = day + 1
    print(day)

class POSIS(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default="src/icons/icon.ico")
        tk.Tk.wm_title(self,"Piece of Sh!t Idol Manager Simulator © 2017")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, News, Girls,Staff,Infu,Events):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=starttext, font=LARGE_FONT)
        label.grid(row=1,column=2)

        button = ttk.Button(self, text="New Game",
                            command=lambda: controller.show_frame(News))
        button.grid(row=2,column=1)
        
        button = ttk.Button(self, text="Load Game\nNot Devloped",
                            command=lambda: controller.show_frame(News))
        button.grid(row=2,column=3)


class News(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Girls",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        
class Girls(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)


        

app = POSIS()
app.mainloop()
