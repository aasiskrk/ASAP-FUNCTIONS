from itertools import count
from tkinter import *
from tkinter import ttk
import sqlite3




#basic tkinter modification
root = Tk()
root.title("ASAP")
root.state('zoomed')
# root.iconbitmap("logo.ico")
root.geometry("1920x1080")

root.minsize(width=500,height=500)
root.maxsize(width=1920,height=1080)

#tabs part

#Main tab elements
tabs= ttk.Notebook(root)
tabs.pack()

mainframe= Frame(tabs,width=1920,height=1080,bg="#D9D9D9")
records_frame= Frame(tabs,width=1920,height=1080,bg="#D9D9D9")


# bg=PhotoImage(file="background_ASAP.png")
# Background=Label(mainframe,image=bg)
# Background.place(x=0,y=0,relwidth=1,relheight=1)

mainframe.pack(fill=BOTH,expand=1)
records_frame.pack(fill=BOTH,expand=1)

tabs.add(mainframe,text="Main")
tabs.add(records_frame,text="Records")

#Elements inside tab
customer_detail_frame= Frame(mainframe,borderwidth=2,relief=SOLID,width=950,height=210,bg="#DDC9FF").place(x=60,y=30)
customer_label= Label(mainframe,text="CUSTOMER DETAILS",font=20,border=1,fg="black",bg="#DDC9FF").place(x=64,y=33)

bill_no_label=Label(mainframe,text="Bill no.",font=7,bg="#DDC9FF").place(x=105,y=80)
bill_no_entry=Entry(mainframe,width=20,relief=RAISED).place(x=280,y=85,width=150,height=23)

date_label=Label(mainframe,text="Transaction Date",font=7,bg="#DDC9FF").place(x=105,y=110)
date_entry=Entry(mainframe,width=20,relief=RAISED).place(x=280,y=115,width=150,height=23)

bill_to_label=Label(mainframe,text="Bill To",font=7,bg="#DDC9FF").place(x=105,y=140)
bill_to_entry=Entry(mainframe,width=20,relief=RAISED).place(x=280,y=145,width=150,height=23)

address_label=Label(mainframe,text="Address",font=7,bg="#DDC9FF").place(x=105,y=170)
address_entry=Entry(mainframe,width=20,relief=RAISED).place(x=280,y=175,width=150,height=23)



# qrcode_frame= Frame(mainframe,borderwidth=2,relief=SOLID,width=420,height=210,bg="#857A8E").place(x=1050,y=30)
qr_buttonl= Button(mainframe,text="QR CODE MODULE",borderwidth=2,relief=SOLID,fg="black",bg="#857A8E",width=59,height=13).place(x=1050,y=30)

item_details_frame= Frame(mainframe,borderwidth=2,relief=SOLID,width=950,height=490,bg="#DDC9FF").place(x=60,y=260)
item_label= Label(mainframe,text="ITEM DETAILS",font=20,border=1,fg="black",bg="#DDC9FF").place(x=64,y=263)


gross_label=Label(mainframe,text="Gross Amount",font=12,fg="black",bg="#DDC9FF").place(x=64,y=603)
gross_entrybox=Entry(mainframe,width=20,relief=RAISED).place(x=200,y=609)

discount_label_2=Label(mainframe,text="Discount",font=12,fg="black",bg="#DDC9FF").place(x=64,y=635)
dicount_entry_2=Entry(mainframe,width=20,relief=RAISED).place(x=200,y=641)

netamount_label=Label(mainframe,text="Net Amount",font=12,fg="black",bg="#DDC9FF").place(x=64,y=658)
netamount_entry=Entry(mainframe,width=20,relief=RAISED).place(x=200,y=664)

given_amount_label=Label(mainframe,text="Given Amount",font=12,fg="black",bg="#DDC9FF").place(x=64,y=689)
given_amount_entry=Entry(mainframe,width=20,relief=RAISED).place(x=200,y=695)

change_label=Label(mainframe,text="Change",font=12,fg="black",bg="#DDC9FF").place(x=64,y=711)
change_entry=Entry(mainframe,width=20,relief=RAISED).place(x=200,y=718)

#database

conn = sqlite3.connect("ASAP.db")

c = conn.cursor() 

#Sir taught to comment but we can use if not exists
c.execute("""CREATE TABLE if not exists ITEM_DETAILS(  
    SN integer,
    Item_Name text,
    Quantity integer,  
    Rate integer,
    Discount integer,
    Amount integer,
    Tender integer,
    Payment_mode text,
    Bill_no integer
   


)""")

c.execute("""CREATE TABLE if not exists PAST_INVOICE(  
    Customer_Name text,
    Transaction_date text,
    Payment_mode text,  
    Address text,
    Bill_no integer
   


)""")

c.execute("""CREATE TABLE if not exists ITEMS_IN_STORE(  
    Item_Name text,
    Rate integer
   


)""")







# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=28,fieldbackground="#D3D3D3",font=4)
style.configure('Treeview.Heading',font=8)
# Change Selected Color
style.map('Treeview',background=[('selected', "#857A8E")])

# Create a Treeview Frame
tree_frame = Frame(mainframe,width=1000,height=500,background="black")
tree_frame.place(x=62,y=290)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

my_tree['columns']=("S.N","Particulars","Quantity","Rate","Amount")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("S.N",anchor=CENTER,width=90)
my_tree.column("Particulars",anchor=W,width=295)
my_tree.column("Quantity",anchor=W,width=180)
my_tree.column("Rate",anchor=W,width=180)
my_tree.column("Amount",anchor=CENTER,width=181)


my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count= 0

for record in ITEM_DETAILS:
    if count % 2 == 0:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
    else:
        my_tree.insert(parent='',index='end',iid=count,text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
        
    count+=1

#select a record
def select_rec(e):
    item_name_entry.delete(0,END)
    quantity_entry.delete(0,END)
    rate_entry.delete(0,END)
    discount_entry.delete(0,END)
    
    
    
    selected = my_tree.focus()
    values=my_tree.items(selected,'values')
    
    item_name_entry.insert(0,values[1])
    quantity_entry.insert(0,values[2])
    rate_entry.insert(0,values[3])
    discount_entry.insert(0,values[4])
    
my_tree.bind("<ButtonRelease-1",select_rec)

insert_item_frame= Frame(mainframe,borderwidth=2,relief=SOLID,width=420,height=270,bg="#DDC9FF").place(x=1050,y=260)
insert_item_label= Label(mainframe,text="INSERT ITEM DETAILS",font=20,border=1,fg="black",bg="#DDC9FF").place(x=1053,y=263)

item_name_label=Label(mainframe,text="Item Name",font=7,bg="#DDC9FF").place(x=1100,y=300)
item_name_entry=Entry(mainframe,width=30,relief=RAISED).place(x=1250,y=305,width=150,height=23)

quantity_label=Label(mainframe,text="Quantity",font=7,bg="#DDC9FF").place(x=1100,y=330)
quantity_entry=Entry(mainframe,width=30,relief=RAISED).place(x=1250,y=335,width=150,height=23)

rate_label=Label(mainframe,text="Rate",font=7,bg="#DDC9FF").place(x=1100,y=360)
rate_entry=Entry(mainframe,width=30,relief=RAISED).place(x=1250,y=365,width=150,height=23)

discount_label=Label(mainframe,text="Discount",font=7,bg="#DDC9FF").place(x=1100,y=390)
discount_entry=Entry(mainframe,width=30,relief=RAISED).place(x=1250,y=395,width=150,height=23)

add_item_btn= Button(mainframe,text="Add Item",font=5).place(x=1300,y=440)
edit_item_btn= Button(mainframe,text="Edit Item",font=5).place(x=1300,y=480)


print_frame=Frame(mainframe,borderwidth=2,relief=SOLID,width=420,height=210,bg="#DDC9FF").place(x=1050,y=540)
tender_label=Label(mainframe,text="Tender",font=7,bg="#DDC9FF").place(x=1100,y=560)
tender_entry=Entry(mainframe,width=30,relief=RAISED).place(x=1250,y=565,width=150,height=23)

payment_options=["Cash","Card"]
payment_option_label= Label(mainframe,text="Payment Option",font=7,bg="#DDC9FF").place(x=1100,y=605 )
payment_combo= ttk.Combobox(mainframe,value=payment_options,width=27)
payment_combo.current(0)
payment_combo.place(x=1250,y=610,width=150,height=23)

store_invoice_button = Button(mainframe,text="STORE INVOICE",font= 15).place(x=1090,y=680)

print_invoice_button = Button(mainframe,text="PRINT INVOICE",font= 15).place(x=1270,y=680)

# payment_combo.bind("<<>>")

#record tab elements

past_inovice_label= Label(records_frame,text="Past Invoice History",font=20,border=1,relief=RAISED,fg="black",bg='#DDC9FF').place(x=680,y=0)

crud_frame=Frame(records_frame,borderwidth=2,relief=SOLID,width=300,height=320,bg='#DDC9FF').place(x=1232,y=140)

access_invoice_button=Button(records_frame,text="Access Inovice",font=15).place(x=1320,y=200)
delete_invoice_button=Button(records_frame,text="Delete Invoice",font=15).place(x=1322,y=250)
print_invoice_button=Button(records_frame,text="Print Invoice",font=15).place(x=1330,y=300)

#functions for treeview


    
    
    
    
    


conn.commit()

conn.close()

root.mainloop()