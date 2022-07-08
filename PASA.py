# import code
# from tkinter import *
# import sqlite3
# from tkinter import messagebox

# root = Tk()
# root.title("ASAP")

# root_label = Label(root,text="ASAP",font=('myFont',25),fg='blue',borderwidth=3) 

# root_label.grid(row=0,column=1,columnspan=3)
 

# conn = sqlite3.connect("PASA.db")

# c = conn.cursor() 

# # c.execute("""CREATE TABLE USER(
# #     User_code integer,
# #     First_Name text,
# #     Last_Name text,
# #     contact integer,  
# #     Add text,
# #     Role text
   


# # )""")


# delete_box = Entry(root,width=30)
# delete_box.grid(row=10,column=1,pady=5)

# delete_label= Label(root,text="Delete ID")
# delete_label.grid(row=10,column=0,pady=5)


# User_code= Entry(root, width=30)
# User_code.grid(row=1,column=1,padx=20)

# User_code_label= Label(root,text="User code")
# User_code_label.grid(row=1,column=0)

# First_Name =Entry(root,width=30)
# First_Name.grid(row=2,column=1)

# First_Name_label= Label(root,text="Name")
# First_Name_label.grid(row=2,column=0)

# Last_Name= Entry(root,width=30)
# Last_Name.grid(row=3,column=1)

# Last_Name_label=Label(root,text="Particulars")
# Last_Name_label.grid(row=3,column=0)

# Contact= Entry(root,width=30)
# Contact.grid(row=4,column=1)

# Contact_label=Label(root,text="Quantity")
# Contact_label.grid(row=4,column=0)

# Add = Entry(root,width=30)
# Add.grid(row=5,column=1)

# Add_label=Label(root,text="Rate")
# Add_label.grid(row=5,column=0)

# Role= Entry(root,width=30)
# Role.grid(row=6,column=1)

# Role_label=Label(root,text="Amount")
# Role_label.grid(row=6,column=0)


# def submit():
    
#     conn = sqlite3.connect("PASA.db")

 
#     c = conn.cursor() 

#     c.execute("INSERT INTO USER VALUES (:SN, :Name, :Particulars,:Quantity,:Rate,:Amount)",{
#         'User_code':User_code.get(),
#         'First_Name':First_Name.get(),
#         'Last_Name':Last_Name.get(),
#         'Contact':Contact.get(),
#         'Add':Add.get(),
#         'Role':Role.get()
#     })
#     messagebox.showinfo("USER", "insterted successfully")

#     User_code.delete(0,END)
#     First_Name.delete(0,END)
#     Last_Name.delete(0,END)
#     Contact.delete(0,END)
#     Add.delete(0,END)
#     Role.delete(0,END)

#     conn.commit()
#     conn.close()

# def query():
#     conn= sqlite3.connect("PASA.db")
#     c = conn.cursor()
#     c.execute("SELECT *,oid FROM USER")

#     records = c.fetchall()
#     print(records)

#     # print_records=""
#     # for record in records:
#     #     print_records+=str(record[0])+" "+str(record[1])
#     # print(print_records)
#     conn.commit()
#     conn.close()

# def delete():
#     conn= sqlite3.connect("PASA.db")
#     c = conn.cursor()
#     c.execute("DELETE from USER WHERE oid ="+ delete_box.get())
#     print("deleted successfully")
#     conn.commit()
#     conn.close()

# def update():
#     conn=sqlite3.connect("PASA.db")
#     c=conn.cursor()
#     record_id=delete_box.get()
        
#     c.execute("""UPDATE USER SET
#     User_code=:User_code,
#     First_Name=:First_Name,
#     Last_Name=:Last_Name,
#     Contact=:Contact,
#     Add=:Add,
#     Role=:Role
#     WHERE oid=:oid""",
#     {'User_code':User_code_editor.get(),
#      'First_Name':First_Name_editor.get(),
#      'Last_Name':Last_Name_editor.get(),
#      'Contact':Contact_editor.get(),
#      'Add':Add_editor.get(),
#      'Role':Role_editor.get(),

#      'oid':record_id
    
    
#     })
        
#     kkk=Toplevel()
#     kkk.title('Update')
#     kkk.geometry('200x100')
#     lbl=Label(kkk,text='Updateed!',font=10)
#     lbl.place(x=60,y=45)
#     btn=Button(kkk,text='OK',width=15,command=kkk.destroy)
#     btn.place(x=45,y=45)
    
#     delete_box.delete(0,END)
    
#     conn.commit()
#     conn.close()
#     editor.destroy()


# def edit():
#     global editor
#     editor=Toplevel()
#     editor.title("Update data")
#     editor.geometry("500x500")

#     conn=sqlite3.connect("PASA.db")
#     c= conn.cursor()
#     record_id=delete_box.get()
#     c.execute("SELECT * FROM USER WHERE oid="+record_id)
#     records=c.fetchall()


#     global SN_editor
#     global Name_editor
#     global Particulars_editor
#     global Quantity_editor
#     global Add_editor
#     global Role_editor



    

#     SN_editor= Entry(editor, width=30)
#     SN_editor.grid(row=0,column=1,padx=40)

#     SN_label= Label(editor,text="SN")
#     SN_label.grid(row=0,column=0)

#     Name_editor =Entry(editor,width=30)
#     Name_editor.grid(row=1,column=1)


#     Name_label= Label(editor,text="Name")
#     Name_label.grid(row=1,column=0)

#     Particulars_editor= Entry(editor,width=30)
#     Particulars_editor.grid(row=2,column=1)

#     Particulars_label=Label(editor,text="Particulars")
#     Particulars_label.grid(row=2,column=0)
    
#     Quantity_editor= Entry(editor,width=30)
#     Quantity_editor.grid(row=3,column=1)

#     Quantity_label=Label(editor,text="Quantity")
#     Quantity_label.grid(row=3,column=0)

#     Rate_editor = Entry(editor,width=30)
#     Rate_editor.grid(row=4,column=1)

#     Rate_label=Label(editor,text="Rate")
#     Rate_label.grid(row=4,column=0)

#     Amount_editor= Entry(editor,width=30)
#     Amount_editor.grid(row=5,column=1)

#     Amount_label=Label(editor,text="Amount")
#     Amount_label.grid(row=5,column=0)


   



    
#     for record in records:
#         SN_editor.insert(0,record[0])
#         Name_editor.insert(0,record[1])
#         Particulars_editor.insert(0,record[2])
#         Quantity_editor.insert(0,record[3])
#         Rate_editor.insert(0,record[4])
#         Amount_editor.insert(0,record[5])
        




#     edit_btn=Button(editor,text="Save",command=update)
#     edit_btn.grid(row=8 ,column=1)

#     conn.commit()
#     conn.close()



# del_btn= Button(root,text="Delete ID",command=delete)
# del_btn.grid(row=14,column=1)

# sub_btn= Button(root,text="Submit",command=submit)
# sub_btn.grid(row=11,column=1)

# query_btn=Button(root,text="Show records",command=query)
# query_btn.grid(row=12,column=1)

# edit_btn=Button(root,text="Update",command=edit)
# edit_btn.grid(row=  13,column=1)



# conn.commit()

# conn.close()



# root.mainloop()