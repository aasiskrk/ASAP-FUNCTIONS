from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("DATA")

root_label = Label(root,text="ASAP",font=('myFont',25),fg='blue',borderwidth=3) 

root_label.grid(row=0,column=1,columnspan=3)
 

conn = sqlite3.connect("DATA.db")

c = conn.cursor() 

c.execute("""CREATE TABLE if not exixts INVOICE(
    Invoice_ID text,
    Customer_Name text,
    Date timestamp,
    Items text,  
    Total_Amount integer,
    Tender integer
   
)""")


delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1,pady=5)

delete_label= Label(root,text="Delete ID")
delete_label.grid(row=10,column=0,pady=5)


Invoice_ID= Entry(root, width=30)
Invoice_ID.grid(row=1,column=1,padx=20)

Invoice_ID_label= Label(root,text="Invoice ID")
Invoice_ID_label.grid(row=1,column=0)

Customer_Name =Entry(root,width=30)
Customer_Name.grid(row=2,column=1)

Customer_Name_label= Label(root,text="Customer Name")
Customer_Name_label.grid(row=2,column=0)

Date= Entry(root,width=30)
Date.grid(row=3,column=1)

Date_label=Label(root,text="Date")
Date_label.grid(row=3,column=0)

Items= Entry(root,width=30)
Items.grid(row=4,column=1)

Items_label=Label(root,text="Items")
Items_label.grid(row=4,column=0)

Total_Amount = Entry(root,width=30)
Total_Amount.grid(row=5,column=1)

Total_Amount_label=Label(root,text="Total Amount")
Total_Amount_label.grid(row=5,column=0)

Tender= Entry(root,width=30)
Tender.grid(row=6,column=1)

Tender_label=Label(root,text="Tender")
Tender_label.grid(row=6,column=0)


def submit():
    
    conn = sqlite3.connect("DATA.db")

 
    c = conn.cursor() 

    c.execute("INSERT INTO INVOICE VALUES (:Invoice_ID, :Customer_Name, :Date,:Items,:Total_Amount,:Tender)",{
        'Invoice_ID':Invoice_ID.get(),
        'Customer_Name':Customer_Name.get(),
        'Date':Date.get(),
        'Items':Items.get(),
        'Total_Amount':Total_Amount.get(),
        'Tender':Tender.get()
    })
    messagebox.showinfo("INVOICE", "insterted successfully")

    Invoice_ID.delete(0,END)
    Customer_Name.delete(0,END)
    Date.delete(0,END)
    Items.delete(0,END)
    Total_Amount.delete(0,END)
    Tender.delete(0,END)

    conn.commit()
    conn.close()

def query():
    conn= sqlite3.connect("DATA.db")
    c = conn.cursor()
    c.execute("SELECT *,oid FROM INVOICE")

    records = c.fetchall()
    print(records)

    # print_records=""
    # for record in records:
    # #     print_records+=str(record[0])+" "+str(record[1])
    # print(print_records)
    conn.commit()
    conn.close()

def delete():
    conn= sqlite3.connect("DATA.db")
    c = conn.cursor()
    c.execute("DELETE from INVOICE WHERE oid ="+ delete_box.get())
    print("deleted successfully")
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect("DATA.db")
    c=conn.cursor()
    record_id=delete_box.get()
        
    c.execute("""UPDATE INVOICE SET
    Invoice_ID=:Invoice_ID,
    Customer_Name=:Customer_Name,
    Date=:Date,
    Items=:Items,
    Total_Amount=:Total_Amount,
    Tender=:Tender
    WHERE oid=:oid""",
    {'Invoice_ID':Invoice_ID_editor.get(),
     'Customer_Name':Customer_Name_editor.get(),
     'Date':Date_editor.get(),
     'Items':Items_editor.get(),
     'Total_Amount':Total_Amount_editor.get(),
     'Tender':Tender_editor.get(),

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

    conn=sqlite3.connect("DATA.db")
    c= conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM INVOICE WHERE oid="+record_id)
    records=c.fetchall()


    global Invoice_ID_editor
    global Customer_Name_editor
    global Date_editor
    global Items_editor
    global Total_Amount_editor
    global Tender_editor



    

    Invoice_ID_editor= Entry(editor, width=30)
    Invoice_ID_editor.grid(row=0,column=1,padx=40)

    Invoice_ID_label= Label(editor,text="Invoice")
    Invoice_ID.grid(row=0,column=0)

    Customer_Name_editor =Entry(editor,width=30)
    Customer_Name_editor.grid(row=1,column=1)


    Customer_Name_label= Label(editor,text="Customer Name")
    Customer_Name_label.grid(row=1,column=0)

    Date_editor= Entry(editor,width=30)
    Date_editor.grid(row=2,column=1)

    Date_label=Label(editor,text="Date")
    Date_label.grid(row=2,column=0)
    
    Items_editor= Entry(editor,width=30)
    Items_editor.grid(row=3,column=1)

    Items_label=Label(editor,text="Items")
    Items_label.grid(row=3,column=0)

    Total_Amount_editor = Entry(editor,width=30)
    Total_Amount_editor.grid(row=4,column=1)

    Total_Amount_label=Label(editor,text="Total Amount")
    Total_Amount.grid(row=4,column=0)

    Tender_editor= Entry(editor,width=30)
    Tender_editor.grid(row=5,column=1)

    Tender_label=Label(editor,text="Tender")
    Tender_label.grid(row=5,column=0)


   



    
    for record in records:
        Invoice_ID_editor.insert(0,record[0])
        Customer_Name_editor.insert(0,record[1])
        Date_editor.insert(0,record[2])
        Items_editor.insert(0,record[3])
        Total_Amount_editor.insert(0,record[4])
        Tender_editor.insert(0,record[5])
        




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