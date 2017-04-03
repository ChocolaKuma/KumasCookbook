from tkinter import *
from tkinter import ttk
import os
import webbrowser

ZoomAMT = 30 #10 small, 20 med, 30 large logoSize
DeBug = False
LOGO_ON = False #enables logo (put logo in "img" folder(make folder if not there)name logo:"logo.png")
ICON_ON = False #enables icon (put icon in "img" folder(make folder if not there)name icon:"icon.ico")

DEBUG = DeBug

errCodes = {1:"Error Code Here",2:"ERROR img/logo.png not found",3:"ERROR img/icon.ico not found"}


def help_HelpDocs():
    webbrowser.open_new("https://github.com/ChocolaKuma/KumaTemplates")
   
    
def buttion(event):
    if (DEBUG == True):
        print("Opening")   
    try:
        print("try")
    except:
        messagebox.showinfo('ERROR 404',errCodes[4])


        

root = Tk()
r = root
var = IntVar()

r.title("itinker template by J.Hinebrook")


if(LOGO_ON == True):
    try:
        logo = PhotoImage(file="img/logo.png")
        logo = logo.zoom(ZoomAMT) 
        logo = logo.subsample(40)
        logoPNG = Label(root, image=logo).grid(row=1,sticky=N,pady=4,column=2)
    except:
        print(errCodes[2])

if(ICON_ON == True):
    try:
        r.iconbitmap(r'img/icon.ico')
    except:
        print(errCodes[3])

f = Frame(r)


Label(r,text="itinker_Template.py",fg = "black",font = "Times").grid(row=2,sticky=N,pady=4,column=2)

messagebox .showinfo("Header","body")


b = Button(r,text="Start")
b.bind("<Button-1>",buttion)
b.grid(row=5,sticky=N,pady=4,column=1)


m = Menu(r)
hm = Menu(m)
hm.add_command(label="Help Docs",command = help_HelpDocs)
m.add_cascade(label="Help",menu=hm)
r.config(menu=m)




r.mainloop()
