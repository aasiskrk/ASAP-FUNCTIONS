from tkinter import *
from tkinter import ttk

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


# my_tree=ttk.Treeview(mainframe)
# my_tree['columns']=("S.N","Particulars","Quality","Rate","Amount")
# my_tree.column("#0",width=120,minwidth=90)
# my_tree.column("S.N",anchor=W,width=20)
# my_tree.column("Particulars",anchor=CENTER,width=80)
# my_tree.column("Quality",anchor=W,width=120)
# my_tree.column("Rate",anchor=W,width=50)
# my_tree.column("Amount",anchor=E,width=90)

# my_tree.heading("#0",text="Name",anchor=W)
# my_tree.heading("S.N",text="S.N",anchor=W)
# my_tree.heading("Particulars",text="Particulars",anchor=CENTER)
# my_tree.heading("Quality",text="Quality",anchor=W)
# my_tree.heading("Rate",text="Rate",anchor=W)
# my_tree.heading("Amount",text="Amount",anchor=E)

# my_tree.insert(parent='',index='end',iid=0,text="Abhilekh",values=(1,"Cupcake",2,40,80))
# my_tree.place(x=70,y=270)



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




root.mainloop()