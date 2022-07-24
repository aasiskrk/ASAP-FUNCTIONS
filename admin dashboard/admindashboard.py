from tkinter import colorchooser
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import sqlite3


#colourvar
maincolor='#DDC9FF'
    
root = Tk()

root.state('zoomed')
root.title('ASAP-LOGIN V-1.0.0'.center(220))
dir1='F:/tkn\ASAP/admin dashboard/'
root.iconbitmap(dir1+'Logo.ico')
root.configure(background=maincolor)

#row-config
root.columnconfigure(1,weight=1)
root.columnconfigure(0,weight=2)
root.rowconfigure(0,weight=1)
#image
img=PhotoImage(file='F:/tkn/ASAP/admin dashboard/bard.png')
dashImg=PhotoImage(file=dir1+'home.png')
prodImg=PhotoImage(file=dir1+'cart.png')
billImg=PhotoImage(file=dir1+'bills.png')
profImg=PhotoImage(file=dir1+'profile.png')
setImg=PhotoImage(file=dir1+'settings.png')
pickerImg=PhotoImage(file=dir1+'picker.png')


#tab-commands
def show_frame(frame,btn):
    frame.tkraise()
    if btn==1:
        frame1_btn.configure(border=1)
        frame2_btn.configure(border=0)
        frame3_btn.configure(border=0)
        frame4_btn.configure(border=0)
        frame5_btn.configure(border=0)
    elif btn==2:
        frame1_btn.configure(border=0)
        frame2_btn.configure(border=1)
        frame3_btn.configure(border=0)
        frame4_btn.configure(border=0)
        frame5_btn.configure(border=0)
    elif btn==3:
        frame1_btn.configure(border=0)
        frame2_btn.configure(border=0)
        frame3_btn.configure(border=1)
        frame4_btn.configure(border=0)
        frame5_btn.configure(border=0)
    elif btn==4:
        frame1_btn.configure(border=0)
        frame2_btn.configure(border=0)
        frame3_btn.configure(border=0)
        frame4_btn.configure(border=1)
        frame5_btn.configure(border=0)
    elif btn==5:
        frame1_btn.configure(border=0)
        frame2_btn.configure(border=0)
        frame3_btn.configure(border=0)
        frame4_btn.configure(border=0)
        frame5_btn.configure(border=1)



def signout():
    exitApp=messagebox.askquestion('signout','Do you reallllllly want to signout?',icon='warning',default='no')
    if exitApp=='yes':
        root.quit()


#frames
frame1 = Frame(root,bg=maincolor)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root,background='white')
btnframe = Frame(root,background=maincolor)
btnframe.grid(row=0,column=0,sticky=N)

#frame placement
for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0,column=1,sticky='nsew',pady=10,padx=10)
    

# #dashboard-frames
# frame1_title=  Label(frame1, font='times 35', bg='red')
# frame1_title.pack(expand=True)


frame2_title=  Label(frame2, font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)


frame2_title=  Label(frame3, font='times 35', bg='purple')
frame2_title.pack(fill='both', expand=True)






#buttons
frame1_btn = Button(btnframe,relief='solid',activebackground=maincolor,width=30,border=0,bg=maincolor, text='  Dashboard',font='{tw cen mt}',compound=LEFT,image=dashImg,command=lambda:show_frame(frame1,1),cursor='hand2')
frame1_btn.pack(fill='x', ipady=15,ipadx=70,pady=(10,6))


frame2_btn = Button(btnframe,relief='solid',activebackground=maincolor,border=0,bg=maincolor, text='  Products      ',font='{tw cen mt}',compound=LEFT,image=prodImg,command=lambda:show_frame(frame2,2),cursor='hand2')
frame2_btn.pack(fill='x', ipady=15,pady=6)

frame3_btn = Button(btnframe,relief='solid',activebackground=maincolor,border=0,bg=maincolor, text='   Bills            ',font='{tw cen mt}',compound=LEFT,image=billImg,command=lambda:show_frame(frame3,3),cursor='hand2')
frame3_btn.pack(fill='x', ipady=15,pady=6)

frame4_btn = Button(btnframe,relief='solid',activebackground=maincolor,border=0,bg=maincolor, text='   Users         ',font='{tw cen mt}',compound=LEFT,image=profImg,command=lambda:show_frame(frame4,4),cursor='hand2')
frame4_btn.pack(fill='x', ipady=15,pady=6)

frame5_btn = Button(btnframe,relief='solid',activebackground=maincolor,border=0,bg=maincolor, text='  Settings      ',font='{tw cen mt}',compound=LEFT,image=setImg,command=lambda:show_frame(frame5,5),cursor='hand2')
frame5_btn.pack(fill='x', ipady=15,pady=6)


show_frame(frame1,1)
#frame1
fm1=Frame(frame1,width=800,height=200)
fm1.grid(row=0,column=0)

fm2=Frame(frame1,width=350,height=200)
fm2.grid(row=0,column=1,padx=(10,0))

fm3=Frame(frame1,width=1159,height=260,background='white',highlightbackground='red')
fm3.grid(row=1,column=0,columnspan=2,pady=10)

fm4=Frame(frame1,width=800,height=200,background='white')
fm4.grid(row=2,column=0)

fm5=Frame(frame1,width=350,height=200)
fm5.grid(row=2,column=1,padx=(10,0))


#plot-label
ply_label=Label(fm3,text='Insights',font='{tw cen mt} 20',width=50,bg='white')
ply_label.pack(anchor='nw')

#plot
plt.style.use('seaborn-dark')
x=[2,3,5,6,7,8,5,4,7,9,5]
y=[3,5,7,8,3,6,7,8,3,5,6]
fig=plt.figure(figsize=(5,2.5))
fig.tight_layout()
ax1=fig.add_subplot(111)
ax1.plot(x,y)
canvas = FigureCanvasTkAgg(fig, master=fm3) 
canvas.get_tk_widget().pack(anchor=W)
canvas.draw()

#users
conn = sqlite3.connect('asapDatabase.db')

# Create a cursor instance
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE if not exists userd(
	first_name text,
	last_name text,
	username text,
    address text,
	password text)
	""")
# Add dummy data to table

# for record in data:
# 	c.execute("INSERT INTO userd VALUES (:first_name, :last_name, :username, :address,:password)", 
# 		{
# 		'first_name': record[0],
# 		'last_name': record[1],
# 		'username': record[2],
# 		'address': record[3],
#         'password': record[4]
# 		}
# 		)



# Commit changes
conn.commit()

# Close our connection
conn.close()

def query_database():
	# Create a database or connect to one that exists
	conn = sqlite3.connect('F:/tkn/ASAP/admin dashboard/asapDatabase.db')

	# Create a cursor instance
	c = conn.cursor()

	c.execute("SELECT *,oid FROM userd")
	records = c.fetchall()
	#print(records)
	# Add our data to the screen
	global count
	count = 0

	for record in records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4],record[5]), tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4],record[5]), tags=('oddrow',))
		# increment counter
		count += 1


	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()



# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=50,
	fieldbackground="#D3D3D3",
    font='{tw cen mt}')


style.configure("Treeview.Heading", font=('{tw cen mt} 15'),
    background='white',
    border=2
)
# Change Selected Color
style.map('Treeview',
	background=[('selected', "#FF8080")])

#frame for tt


# Create a Treeview Frame
tree_frame = Frame(frame4)
tree_frame.grid(row=0,column=0,pady=(100,0),padx=(50,10))

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("First Name", "Last Name", "Username", "Address")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=250)
my_tree.column("Last Name", anchor=W, width=250)
my_tree.column("Username", anchor=CENTER, width=180)
my_tree.column("Address", anchor=CENTER, width=180)



# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Username", text="Username", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)



# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background=maincolor)


# Remove all records
def update_table():
    for record in my_tree.get_children():
        my_tree.delete(record)
    query_database()



# Update record
def delete_record():
    msg=messagebox.askquestion("Warning!!", "Are you sure you want to delete following user?",icon = 'warning')
    print(msg)
    if msg=='yes':
	# Grab the record number
        selected = my_tree.focus()
        dosi = my_tree.item(selected,'values')
        # ok=int(selected)+1
        # print(dosi[5])
        conn= sqlite3.connect('F:/tkn/ASAP/admin dashboard/asapDatabase.db')
        c=conn.cursor()
        c.execute('delete from userd where oid ='+dosi[5])
        print('success','deleted')
        conn.commit()
        conn.close()
        update_table()

def update_users():
    conn = sqlite3.connect('F:/tkn/ASAP/admin dashboard/asapDatabase.db')
    selected = my_tree.focus()
    dosi = my_tree.item(selected,'values')
    c = conn.cursor()
    c.execute('''UPDATE userd SET
            first_name=:first_name,
            last_name=:last_name,
            username=:username,
            address=:address,
            password=:password
            where oid=:oid''',
            {'first_name':firstname_edit.get(),
            'last_name':lastname_edit.get(),
            'username':Username_edit.get(),
            'address':address_edit.get(),
            'password':password_edit.get(),
            'oid':dosi[5]
            }
        )
    conn.commit()
    conn.close()
    editor.destroy();update_table()


def edit_user():
    global editor
    editor=Toplevel()
    editor.title('Update data')
    editor.geometry('300x400')

    conn=sqlite3.connect('F:/tkn/ASAP/admin dashboard/asapDatabase.db')
    c=conn.cursor()
    selected = my_tree.focus()
    dosi = my_tree.item(selected,'values')
    c.execute("select * from userd where oid="+dosi[5])
    records=c.fetchall()

    global firstname_edit
    global lastname_edit
    global Username_edit
    global address_edit
    global password_edit


    firstname_edit= Entry(editor, width=30)
    firstname_edit.grid(row=1,column=1,padx=20,pady=5)

    lastname_edit=Entry(editor,width=30)
    lastname_edit.grid(row=2,column=1,pady=5)

    Username_edit=Entry(editor,width=30)
    Username_edit.grid(row=3,column=1,pady=5)

    address_edit=Entry(editor,width=30)
    address_edit.grid(row=4,column=1,pady=5)

    password_edit=Entry(editor,width=30)
    password_edit.grid(row=5,column=1,pady=5)

    fnamelabel= Label(editor,text="firstname")
    fnamelabel.grid(row=1,column=0)

    lastnamelabel= Label(editor,text="lastname")
    lastnamelabel.grid(row=2,column=0)

    agelabel= Label(editor,text="Username")
    agelabel.grid(row=3,column=0)

    addresslabel= Label(editor,text="address")
    addresslabel.grid(row=4,column=0)

    passwordlabel= Label(editor,text="password")
    passwordlabel.grid(row=5,column=0)


    sub_btn=Button(editor,text='Submit',command=update_users)
    sub_btn.grid(row=9,column=0,columnspan=2)
    for record in records:
        firstname_edit.insert(0,record[0])
        lastname_edit.insert(0,record[1])
        Username_edit.insert(0,record[2])
        address_edit.insert(0,record[3])
        password_edit.insert(0,record[4])


    conn.commit()
    conn.close()

def add_user():
    global editor
    editor=Toplevel()
    editor.title('add User')
    editor.geometry('300x400')

    global firstname_add
    global lastname_add
    global Username_add
    global address_add
    global password_add
    firstname_add= Entry(editor, width=30)
    firstname_add.grid(row=1,column=1,padx=20,pady=5)

    lastname_add=Entry(editor,width=30)
    lastname_add.grid(row=2,column=1,pady=5)

    Username_add=Entry(editor,width=30)
    Username_add.grid(row=3,column=1,pady=5)

    address_add=Entry(editor,width=30)
    address_add.grid(row=4,column=1,pady=5)

    password_add=Entry(editor,width=30)
    password_add.grid(row=5,column=1,pady=5)

    fnamelabel= Label(editor,text="firstname")
    fnamelabel.grid(row=1,column=0)

    lastnamelabel= Label(editor,text="lastname")
    lastnamelabel.grid(row=2,column=0)

    agelabel= Label(editor,text="Username")
    agelabel.grid(row=3,column=0)

    addresslabel= Label(editor,text="address")
    addresslabel.grid(row=4,column=0)

    passwordlabel= Label(editor,text="password")
    passwordlabel.grid(row=5,column=0);
    
    btn=Button(editor,text='add user',command=submit)
    btn.grid(row=6,column=1)

def submit():
    conn= sqlite3.connect('F:/tkn/ASAP/admin dashboard/asapDatabase.db')
    c=conn.cursor()
    c.execute('''insert into userd values(:first_name,:last_name,:username,:address,:password)''',{'first_name':firstname_add.get(),'last_name':lastname_add.get(),'username':Username_add.get(),'address':address_add.get(),'password':password_add.get()}
    )
    messagebox.showinfo('success','Inserted sucessfully')
            
    conn.commit()
    conn.close()
    update_table()

# Add Buttons
button_frame = Frame(frame4)
button_frame.grid(row=0,column=1)

delete_user = Button(button_frame, text="Delete user", command=delete_record,relief="solid",bd=2,bg='#FF7676',font='{Tw cen mt} 13 ',width=19,height=2,activebackground='#FF7676',cursor='hand2')
delete_user.grid(row=0, column=0, padx=10, pady=10)

update_user = Button(button_frame, text="Update",command=edit_user,relief="solid",bd=2,bg='#FF7676',font='{Tw cen mt} 13 ',width=19,height=2,activebackground='#FF7676',cursor='hand2')
update_user.grid(row=1, column=0, padx=10, pady=10)

add_user = Button(button_frame, text="Add user",command=add_user,relief="solid",bd=2,bg='#FF7676',font='{Tw cen mt} 13 ',width=19,height=2,activebackground='#FF7676',cursor='hand2')
add_user.grid(row=2, column=0, padx=10, pady=10)


# Run to pull data from database on start
query_database()




#settings

def choose_color():
    maicolor = colorchooser.askcolor(title ="Choose color")
    root.configure(background=maicolor[1])
    btnframe.configure(background=maicolor[1])
    frame1.configure(background=maicolor[1])
    my_tree.tag_configure('evenrow', background=maincolor[1])
    frame1_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame2_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame3_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame4_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame5_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    button_custom.configure(activebackground=maicolor[1],bg=maicolor[1],border=2)
    lavender_btn.configure(border=0)
    peach_btn.configure(border=0)
    fiery_btn.configure(border=0)
    azure_btn.configure(border=0)
    mint_btn.configure(border=0)        
    gray_btn.configure(border=0)
    shadow_btn.configure(border=0)


def defined_color(color,btncode):
    root.configure(background=color)
    btnframe.configure(background=color)
    frame1.configure(background=color)
    frame1_btn.configure(activebackground=color,bg=color)
    frame2_btn.configure(activebackground=color,bg=color)
    frame3_btn.configure(activebackground=color,bg=color)
    frame4_btn.configure(activebackground=color,bg=color)
    frame5_btn.configure(activebackground=color,bg=color)
    my_tree.tag_configure('evenrow', background=color)
    
    #border-color
    if btncode==1:
        lavender_btn.configure(border=2)
        peach_btn.configure(border=0)
        fiery_btn.configure(border=0)
        azure_btn.configure(border=0)
        mint_btn.configure(border=0)        
        gray_btn.configure(border=0)
        shadow_btn.configure(border=0)
        button_custom.configure(border=0)
    elif btncode==2:
        lavender_btn.configure(border=0)
        peach_btn.configure(border=2)
        fiery_btn.configure(border=0)
        azure_btn.configure(border=0)
        mint_btn.configure(border=0)        
        gray_btn.configure(border=0)
        shadow_btn.configure(border=0)
        button_custom.configure(border=0)
    elif btncode==3:
        lavender_btn.configure(border=0)
        peach_btn.configure(border=0)
        fiery_btn.configure(border=2)
        azure_btn.configure(border=0)
        mint_btn.configure(border=0)        
        gray_btn.configure(border=0)
        shadow_btn.configure(border=0)
        button_custom.configure(border=0)
    elif btncode==4:
        lavender_btn.configure(border=0)
        peach_btn.configure(border=0)
        fiery_btn.configure(border=0)
        azure_btn.configure(border=2)
        mint_btn.configure(border=0)        
        gray_btn.configure(border=0)
        shadow_btn.configure(border=0)
        button_custom.configure(border=0)
    elif btncode==5:
        lavender_btn.configure(border=0)
        peach_btn.configure(border=0)
        fiery_btn.configure(border=0)
        azure_btn.configure(border=0)
        mint_btn.configure(border=2)        
        gray_btn.configure(border=0)
        shadow_btn.configure(border=0)
        button_custom.configure(border=0)
    elif btncode==6:
        lavender_btn.configure(border=0)
        peach_btn.configure(border=0)
        fiery_btn.configure(border=0)
        azure_btn.configure(border=0)
        mint_btn.configure(border=0)        
        gray_btn.configure(border=2)
        shadow_btn.configure(border=0)
        button_custom.configure(border=0)
    elif btncode==7:
        lavender_btn.configure(border=0)
        peach_btn.configure(border=0)
        fiery_btn.configure(border=0)
        azure_btn.configure(border=0)
        mint_btn.configure(border=0)        
        gray_btn.configure(border=0)
        shadow_btn.configure(border=2)
        button_custom.configure(border=0)
#label
color_label=Label(frame5,text='Colors',font='{te cen mt} 20 bold',bg='white')
color_label.grid(row=0,column=0,pady=(10,5))

#btns
lavender_btn=Button(frame5,text='Lavender',bg='#DDC9FF',fg='white',activebackground='#DDC9FF',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=2,relief='solid',command= lambda:defined_color('#DDC6FF',1))
lavender_btn.grid(row=1,column=0,padx=(40,10))

peach_btn=Button(frame5,text='peach',bg='#FFAFAF',fg='white',activebackground='#FFAFAF',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command= lambda:defined_color('#FFAFAF',2) )
peach_btn.grid(row=1,column=1,padx=10)

fiery_btn=Button(frame5,text='fiery',bg='#ECA234',fg='white',activebackground='#ECA234',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command= lambda:defined_color('#ECA234',3) )
fiery_btn.grid(row=1,column=2,padx=10)

azure_btn=Button(frame5,text='Azure',bg='#6CB6FF',fg='white',activebackground='#6CB6FF',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command= lambda:defined_color('#6CB6FF',4) )
azure_btn.grid(row=1,column=3,padx=10)

mint_btn=Button(frame5,text='mint',bg='#76B660',fg='white',activebackground='#76B660',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command= lambda:defined_color('#76B660',5) )
mint_btn.grid(row=1,column=4,padx=10)

gray_btn=Button(frame5,text='gray',bg='#D9D9D9',fg='white',activebackground='#D9D9D9',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command= lambda:defined_color('#D9D9D9',6) )
gray_btn.grid(row=1,column=5,padx=10)

shadow_btn=Button(frame5,text='shadow',bg='#5D5074',fg='white',activebackground='#5D5074',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command= lambda:defined_color('#5D5074',7) )
shadow_btn.grid(row=1,column=6,padx=10)



button_custom = Button(frame5, text = "Custom",bg='red',fg='white',activebackground='red',font='{tw cen mt} 16',height=4,width=10,anchor='se',border=0,relief='solid',command = choose_color)
button_custom.grid(row=1,column=7)



root.mainloop()
