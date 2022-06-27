from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("ASAP")

root_label = Label(root,text="ASAP",font=('myFont',25),fg='blue',borderwidth=3) 

root_label.grid(row=0,column=1,columnspan=3)
 

conn = sqlite3.connect("ASAP.db")

c = conn.cursor() 

# c.execute("""CREATE TABLE CHECKOUT(
#     SN integer,
#     Name text,
#     Particulars text,
#     Quantity integer,  
#     Rate integer,
#     Amount integer
   


# # )""")


delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1,pady=5)

delete_label= Label(root,text="Delete ID")
delete_label.grid(row=10,column=0,pady=5)


SN= Entry(root, width=30)
SN.grid(row=1,column=1,padx=20)

SN_label= Label(root,text="SN")
SN_label.grid(row=1,column=0)

Name =Entry(root,width=30)
Name.grid(row=2,column=1)

Name_label= Label(root,text="Name")
Name_label.grid(row=2,column=0)

Particulars= Entry(root,width=30)
Particulars.grid(row=3,column=1)

Particulars_label=Label(root,text="Particulars")
Particulars_label.grid(row=3,column=0)

Quantity= Entry(root,width=30)
Quantity.grid(row=4,column=1)

Quantity_label=Label(root,text="Quantity")
Quantity_label.grid(row=4,column=0)

Rate = Entry(root,width=30)
Rate.grid(row=5,column=1)

Rate_label=Label(root,text="Rate")
Rate_label.grid(row=5,column=0)

Amount= Entry(root,width=30)
Amount.grid(row=6,column=1)

Amount_label=Label(root,text="Amount")
Amount_label.grid(row=6,column=0)


def submit():
    
    conn = sqlite3.connect("ASAP.db")

 
    c = conn.cursor() 

    c.execute("INSERT INTO Checkout VALUES (:SN, :Name, :Particulars,:Rate,:Amount)",{
        'SN':SN.get(),
        'Name':Name.get(),
        'Particulars':Particulars.get(),
        'Quantity':Quantity.get(),
        'Rate':Rate.get(),
        'Amount':Amount.get()
    })
    messagebox.showinfo("Checkout", "insterted successfully")

    SN.delete(0,END)
    Name.delete(0,END)
    Particulars.delete(0,END)
    Quantity.delete(0,END)
    Rate.delete(0,END)
    Amount.delete(0,END)

    conn.commit()
    conn.close()

def query():
    conn= sqlite3.connect("ASAP.db")
    c = conn.cursor()
    c.execute("SELECT *,oid FROM Checkout")

    records = c.fetchall()
    print(records)

    # print_records=""
    # for record in records:
    #     print_records+=str(record[0])+" "+str(record[1])
    # print(print_records)
    conn.commit()
    conn.close()

def delete():
    conn= sqlite3.connect("ASAP.db")
    c = conn.cursor()
    c.execute("DELETE from Checkout WHERE oid ="+ delete_box.get())
    print("deleted successfully")
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect("ASAP.db")
    c=conn.cursor()
    record_id=delete_box.get()
        
    c.execute("""UPDATE Checkout SET
    SN=:SN,
    Name=:Name,
    Particulars=:Particulars,
    Quantity=:Quantity,
    Rate=:Rate,
    Amount=:Amount
    WHERE oid=:oid""",
    {'SN':SN_editor.get(),
     'Name':Name_editor.get(),
     'Particulars':Particulars_editor.get(),
     'Quantity':Quantity_editor.get(),
     'Rate':Rate_editor.get(),
     'Amount':Amount_editor.get(),

     'oid':record_id
    
    
    })
        
    kkk=Toplevel()
    kkk.title('Update')
    kkk.geometry('200x100')
    lbl=Label(kkk,text='Updateed!',font=10)
    lbl.place(x=60,y=45)
    btn=Button(kkk,text='OK',width=15,command=kkk.destroy)
    btn.place(x=45,y=45)
    
    delete_box.delete(0,END)
    
    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor=Toplevel()
    editor.title("Update data")
    editor.geometry("500x500")

    conn=sqlite3.connect("ASAP.db")
    c= conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM Checkout WHERE oid="+record_id)
    records=c.fetchall()


    global SN_editor
    global Name_editor
    global Particulars_editor
    global Quantity_editor
    global Rate_editor
    global Amount_editor



    

    SN_editor= Entry(editor, width=30)
    SN_editor.grid(row=0,column=1,padx=40)

    SN_label= Label(editor,text="SN")
    SN_label.grid(row=0,column=0)

    Name_editor =Entry(editor,width=30)
    Name_editor.grid(row=1,column=1)


    Name_label= Label(editor,text="Name")
    Name_label.grid(row=1,column=0)

    Particulars_editor= Entry(editor,width=30)
    Particulars_editor.grid(row=2,column=1)

    Particulars_label=Label(editor,text="Particulars")
    Particulars_label.grid(row=2,column=0)
    
    Quantity_editor= Entry(editor,width=30)
    Quantity_editor.grid(row=3,column=1)

    Quantity_label=Label(editor,text="Quantity")
    Quantity_label.grid(row=3,column=0)

    Rate_editor = Entry(editor,width=30)
    Rate_editor.grid(row=4,column=1)

    Rate_label=Label(editor,text="Rate")
    Rate_label.grid(row=4,column=0)

    Amount_editor= Entry(editor,width=30)
    Amount_editor.grid(row=5,column=1)

    Amount_label=Label(editor,text="Amount")
    Amount_label.grid(row=5,column=0)


   



    
    for record in records:
        SN_editor.insert(0,record[0])
        Name_editor.insert(0,record[1])
        Particulars_editor.insert(0,record[2])
        Quantity_editor.insert(0,record[3])
        Rate_editor.insert(0,record[4])
        Amount_editor.insert(0,record[5])
        




    edit_btn=Button(editor,text="Save",command=update)
    edit_btn.grid(row=8 ,column=1)

    conn.commit()
    conn.close()



del_btn= Button(root,text="Delete ID",command=delete)
del_btn.grid(row=14,column=1)

sub_btn= Button(root,text="Submit",command=submit)
sub_btn.grid(row=11,column=1)

query_btn=Button(root,text="Show records",command=query)
query_btn.grid(row=12,column=1)

edit_btn=Button(root,text="Update",command=edit)
edit_btn.grid(row=  13,column=1)



conn.commit()

conn.close()



root.mainloop()