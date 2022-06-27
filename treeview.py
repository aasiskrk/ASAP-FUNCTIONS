# from tkinter import *
# from tkinter import ttk
# import sqlite3


# root= Tk()
# root.title("ASAP")
# root.geometry("1080x1200")

# data=[
#     [1,"Abhilekh","wai",13,1,123]
#     # [2,"Yonjan","wa",12,2,"1223"],
#     # [3,"Abhi","noodles",10,3,"1323"],
#     # [4,"Yon","choco",1,4,"1423"],
#     # [5,"kh","late",2,5,"12563"],
#     # [6,"hello","candy",22,"61273"],
#     # [7,"world","dew",222,7,"1283"],
#     # [8,"ram","sam",124,8,"1293"]
# ]
# # datebase
# #create a database
# conn=sqlite3.connect('tree_ASAP.db')
# #create a cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE CHECKOUT(
#     SN integer,
#     Name text,
#     Particulars text,
#     Rate integer,
#     Amount integer
   


# )""")
# for record in data:
#     c.execute("INSERT INTO CHECKOUT VALUES(:SN,:Name,:Particulars,:Rate,:Amount)",
#             {
#            'SN':record[0],
#            'Name':record[1],
#            'Particulars':record[2],
#            'Rate':record[3],
#            'Amount':record[4]   
#             }
#             )

# conn.commit()

# conn.close()

# def query_database():
    
#     conn=sqlite3.connect('tree_ASAP.db')

#     c=conn.cursor()
#     c.execute("SELECT * FROM CHECKOUT")
#     records=c.fetchall()
#     # print(records)
    
#     global count
#     count=0
#     for record in records:
#         print(record)
        
#     for record in records:
#         if count%2==0:
#             my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],'evenrow',))
#         else:
#             my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],'oddrow',))
#         count+=1
    
    
#     conn.commit()

#     conn.close()

# #Add some style
# style=ttk.Style()
# style.theme_use("default")

# #configuer the treeview colors
# style.configure("Treeview",
#     background="gray",
#     foreground="black",
#     rowheight=25,
#     fieldbackground="gray")
# #change select color
# style.map("Treeview",
#     background=[('selected',"dark blue")])
# #create a treeview frame
# tree_frame=Frame(root)
# tree_frame.pack(pady=10)
# #create a Treeview scrollbar
# tree_scroll=Scrollbar(tree_frame)
# tree_scroll.pack(side=RIGHT,fill=Y)
# #create the treeview
# my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
# my_tree.pack()
# tree_scroll.config(command=my_tree.yview)
# #define our columns
# my_tree['columns']=("SN","Name","Particulars","Quantity","Rate","Amount")
# #format
# my_tree.column("#0",width=0,stretch=NO)
# my_tree.column("SN",anchor=W,width=20)
# my_tree.column("Name",anchor=W,width=100)
# my_tree.column("Particulars",anchor=CENTER,width=80)
# my_tree.column("Quantity",anchor=W,width=120)
# my_tree.column("Rate",anchor=W,width=50)
# my_tree.column("Amount",anchor=E,width=90)

# my_tree.heading("#0",text="",anchor=W)
# my_tree.heading("SN",text="SN",anchor=W)
# my_tree.heading("Name",text="Name",anchor=W)
# my_tree.heading("Particulars",text="Particulars",anchor=CENTER)
# my_tree.heading("Quantity",text="Quantity",anchor=W)
# my_tree.heading("Rate",text="Rate",anchor=W)
# my_tree.heading("Amount",text="Amount",anchor=E)
# #fake database

# #create striped row tags
# my_tree.tag_configure('oddrow',background="white")
# my_tree.tag_configure('evenrow',background="lightblue")

# # Add data
# # data=[
# #     [1,"Abhilekh","wai",13,1,123],
#     # [1,'Abhiyan',"Noodles",12,2,1235]
    
# # ]
# # global count
# # count=0
# # for record in data:
# #     if count%2==0:
# #         my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],'evenrow',))
# #     else:
# #         my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],'oddrow',))
# #         count+=1
# #add Record entry boxes
# data_frame=LabelFrame(root,text="Record")
# data_frame.pack(fill='x',expand='yes',padx=20)

# SN_label=Label(data_frame,text='SN')
# SN_label.grid(row=0,column=0,padx=10,pady=10)
# SN_entry=Entry(data_frame)
# SN_entry.grid(row=0,column=1,padx=10,pady=10)

# Name_label=Label(data_frame,text='Name')
# Name_label.grid(row=0,column=2,padx=10,pady=10)
# Name_entry=Entry(data_frame)
# Name_entry.grid(row=0,column=3,padx=10,pady=10)

# Particulars_label=Label(data_frame,text='Items')
# Particulars_label.grid(row=1,column=0,padx=10,pady=10)
# Particulars_entry=Entry(data_frame)
# Particulars_entry.grid(row=1,column=1,padx=10,pady=10)

# Quantity_label=Label(data_frame,text='Qty')
# Quantity_label.grid(row=1,column=2,padx=10,pady=10)
# Quantity_entry=Entry(data_frame)
# Quantity_entry.grid(row=1,column=3,padx=10,pady=10)

# Rate_label=Label(data_frame,text='Rate')
# Rate_label.grid(row=2,column=0,padx=10,pady=10)
# Rate_entry=Entry(data_frame)
# Rate_entry.grid(row=2,column=1,padx=10,pady=10)

# Amount_label=Label(data_frame,text='Amount')
# Amount_label.grid(row=2,column=2,padx=20,pady=20)
# Amount_entry=Entry(data_frame)
# Amount_entry.grid(row=2,column=3,padx=20,pady=20)

# #move row up
# def up():
#     rows=my_tree.selection()
#     for row in rows:
#         my_tree.move(row,my_tree.parent(row),my_tree.index(row)-1)

# #def down
# def down():
#     rows=my_tree.selection()
#     for row in reversed(row):
#         my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)

# def remove_one():
#     x=my_tree.selection()[0]
#     my_tree.delete(x)
    

# #clear entries:
# def clear_entries():
#     SN_entry.delete(0,END)
#     Name_entry.delete(0,END)
#     Particulars_entry.delete(0,END)
#     Quantity_entry.delete(0,END)
#     Rate_entry.delete(0,END)
#     Amount_entry.delete(0,END)
# #select records
# def select_record(e):
#     SN_entry.delete(0,END)
#     Name_entry.delete(0,END)
#     Particulars_entry.delete(0,END)
#     Quantity_entry.delete(0,END)
#     Rate_entry.delete(0,END)
#     Amount_entry.delete(0,END)
#     #grab records
#     selected=my_tree.focus()
    
#     values=my_tree.item(selected,'values')
    
#     #output to enty boxes
#     SN_entry.insert(0,values[0])
#     Name_entry.insert(0,values[1])
#     Particulars_entry.insert(0,values[2])
#     Quantity_entry.insert(0,values[3])
#     Rate_entry.insert(0,values[4])
#     Amount_entry.insert(0,values[5])
    
# def update_record():
#     selected=my_tree.focus()
#     my_tree.item(selected,text="",values=( SN_entry.get(),Name_entry.get(),Particulars_entry.get(),Rate_entry.get(),Amount_entry.get(),))       

#     SN_entry.delete(0,END)
#     Name_entry.delete(0,END)
#     Particulars_entry.delete(0,END)
#     Quantity_entry.delete(0,END)
#     Rate_entry.delete(0,END)
#     Amount_entry.delete(0,END)
    
# #buttons
# button_frame=LabelFrame(root,text="Commands")
# button_frame.pack(fill="x",expand="yes",padx=20)

# Update_button=Button(button_frame,text="Update",command=update_record)
# Update_button.grid(row=0,column=0,padx=10,pady=10)

# add_button=Button(button_frame,text="ADD")
# add_button.grid(row=0,column=1,padx=10,pady=10)

# move_up_button=Button(button_frame,text="Move up",command=up)
# move_up_button.grid(row=0,column=3,padx=10,pady=10)

# move_down_button=Button(button_frame,text="Move Down",command=down)
# move_down_button.grid(row=0,column=4,padx=10,pady=10)

# remove_button=Button(button_frame,text="Remove",command=remove_one)
# remove_button.grid(row=0,column=2,padx=10,pady=10)

# select_record_button=Button(button_frame,text="Clear",command=clear_entries)
# select_record_button.grid(row=3,column=0,padx=10,pady=10)
# my_tree.bind("<ButtonRelease-1>",select_record)

# #run to pull data from database on start
# query_database()

# root.mainloop()


