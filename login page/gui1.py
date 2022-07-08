from tkinter import *
from PIL import Image,ImageTk
import sqlite3 as sq


#initial setup
root=Tk()
root.title('ASAP-LOGIN V-1.0.0'.center(220))
root.iconbitmap('logo.ico')
root.configure(background='#DDC9FF')
root.maxsize(height=700,width=900)
root.minsize(height=700,width=900)
root.geometry('900x700')




#image
myimag=(Image.open('pooza.png'))
ok=myimag.resize((250,290))
conimg=ImageTk.PhotoImage(ok)
my_label=Label(root,image=conimg,bg='#DDC9FF')
my_label.place(x=100,y=295)
img1=PhotoImage(file='rec1.png')

#Entry
frame=LabelFrame(root,padx=25,pady=10,highlightbackground="black", highlightthickness=3,background='white',border=0)
frame.place(x=350,y=200)
signup=Label(frame, text='Cashier Login',bg='white',font='{Tw cen mt} 25 bold')#rockwell #Tw Cen MT #condensed #century gothic
signup.grid(row=0,column=0,sticky=W)
name=Label(frame,text="Username",bg='white',justify='right',font='{Tw cen mt} 15')
name.grid(row=1,column=0,sticky=W,pady=(5,0))

#img for entry
img=PhotoImage(file='rec.png') 
img_open=PhotoImage(file='open.png')
img_close=PhotoImage(file='close.png')
#entry1
fm=Frame(frame,border=0,relief='solid')
fm.grid(row=2,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e3=Entry(fm,border=0,width=22,relief="solid",font=50,background='white')
e3.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))




passWord=Label(frame,text="Password",bg='white',justify='right',font='{Tw cen mt} 15',anchor=W)
passWord.grid(row=3,column=0,sticky=W)



a=0
def showpass():
    global a
    a=a+1
    if a%2==0:
        e2.config(show='*')
        showPass.config(image=img_close)
    else:
        e2.config(show='')
        showPass.config(image=img_open)





fm=Frame(frame,border=0,relief='solid')
fm.grid(row=4,column=0)
lb=Label(fm,image=img,background='white',compound='center',justify=CENTER)
lb.grid(row=0,column=0,columnspan=2)
e2=Entry(fm,border=0,width=22,relief="solid",font=50,background='white',show='*')
e2.grid(row=0,column=0,ipady=10,sticky=NS,pady=(4,18),padx=(0,0))
showPass=Button(fm,image=img_close,bg='white',relief='solid',cursor='hand2',activebackground='white',border=0,command=showpass)
showPass.grid(row=0,column=1,sticky=W,pady=(0,17))


btn_frame=Frame(frame,width=241,height=50,background='#BFBFBF')
btn_frame.place(x=20,y=269)
btn=Button(frame,text='Sign In',relief="solid",bd=3,bg='#FF7676',font='{Tw cen mt} 13 bold ',width=26,height=2,activebackground='#FF7676',cursor='hand2')
btn.grid(row=5,column=0,pady=(15,12),padx=(1,5))
btn1=Button(frame,text='Create a new user',relief="flat",bg='white',font='{Tw cen mt} 11 underline',activebackground='white',bd=0,cursor='hand2')
btn1.grid(row=6,column=0,pady=(5,10))




#login verifacationdef login1():


def login1():
    cen=sq.connect('game.db')
    c=cen.cursor()
    c.execute('select *,oid from Usersd')
    record=c.fetchall()
    for i in range(len(record)):
        if record[i][0]==userData.get():
            if record[i][1]==passData.get():
                print('hello mister')
            else:
                print('wrong pass')
        else:
            print('dumdum')

    cen.commit()
    cen.close



root.mainloop()