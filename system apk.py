import os
from tkinter import *

def rt():
    os.system("shutdown /r /t 1")

def rtm():
    os.system("shutdown /r /t 20")

def shut():
    os.system("shutdown -l")
    
def log():
    os.system("shutdown /s /t 1")    
w=Tk()
w.geometry("600x300")
w.config(bg="gray")
b1= Button(w, text="RESTART",relief=RAISED,cursor="plus",width=40,fg="green",bg="black",command=rt
).place(y=50,x=150)
b2= Button(w, text="RESTART time",relief=RAISED,cursor="plus",width=40,fg="green",bg="black",command=rtm
).place(y=100,x=150)
b3= Button(w, text="LOG OUT",relief=RAISED,cursor="plus",width=40,fg="green",bg="black",command=log
).place(y=150,x=150)
b4= Button(w, text="SHUT DOWN",relief=RAISED,cursor="plus",width=40,fg="green",bg="black",command=shut
).place(y=200,x=150)
w.mainloop()