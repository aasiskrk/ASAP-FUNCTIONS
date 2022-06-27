from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("ASAP")

# root.iconbitmap("facebook.ico")

root_label = Label(root,text="ASAP",font=('myFont',25),fg='blue',borderwidth=3) 

root_label.grid(row=0,column=1,columnspan=3)
 

conn = sqlite3.connect("ASAP.db")

c = conn.cursor() 

c.execute("""CREATE TABLE CHECKOUT(
    FirstName text,
    LastName text,
    Age text,
    Address text,
    City text,
    Zipcode text,
    Password text,
    Gender text



)""")
conn.commit()

#hello