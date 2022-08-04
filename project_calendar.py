from calendar import month
import calendar
from tkinter import*
import tkinter as tk
from tkcalendar import*
import datetime 


root=Tk()
root.title("C A L A N D E R")
root.geometry("249x200")

def show_calendar():
    a=int(spin1.get())
    b=int(spin2.get())
    cal=calendar.month(b,a)
    txt.delete(0.0,END)
    txt.insert(INSERT,cal)

label_1=Label(root,text="Month",font=("Verdana",9,"bold")).place(x=15,y=0)
label_2=Label(root,text="Year",font=("Verdana",9,"bold")).place(x=115,y=0)



spin1=Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,12),width=4)
spin1.place(x=60,y=0)


spin2=Spinbox(root,from_= 2000,to_= 2100,width=4)
spin2.place(x=150,y=0)

btn1=Button(root,text="Show",font=("airial",10,"bold"),command=show_calendar).place(x=100,y=30)

txt=Text(root,width=24,height=8)
txt.place(x=20,y=57)

root.mainloop()