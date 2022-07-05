from tkinter import *
from tkinter import messagebox
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    
root = Tk()

root.state('zoomed')
root.title('ASAP-LOGIN V-1.0.0'.center(220))
root.iconbitmap('Logo.ico')
root.configure(background='#DDC9FF')
maincolor='#DDC9FF'

#row-config
root.columnconfigure(1,weight=1)
root.columnconfigure(0,weight=2)
root.rowconfigure(0,weight=1)

#image
img=PhotoImage(file='F:/tkn/ASAP/admin dashboard/bard.png')
dashImg=PhotoImage(file='home.png')
prodImg=PhotoImage(file='cart.png')
billImg=PhotoImage(file='bills.png')
profImg=PhotoImage(file='profile.png')
setImg=PhotoImage(file='settings.png')

#tab-commands
def show_frame(frame):
    frame.tkraise()
    


def signout():
    exitApp=messagebox.askquestion('signout','Do you reallllllly want to signout?',icon='warning',default='no')
    if exitApp=='yes':
        root.quit()


#frames
frame1 = Frame(root,bg=maincolor)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
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


frame2_title=  Label(frame4, font='times 35', bg='blue')
frame2_title.pack(fill='both', expand=True)


frame2_title=  Label(frame5, font='times 35', bg='pink')
frame2_title.pack(fill='both', expand=True)



show_frame(frame1)

#buttons
frame1_btn = Button(btnframe,activebackground=maincolor,width=30,border=0,bg=maincolor, text='  Dashboard',font='{tw cen mt}',compound=LEFT,image=dashImg,command=lambda:show_frame(frame1),cursor='hand2')
frame1_btn.pack(fill='x', ipady=15,ipadx=70,pady=(10,5))


frame2_btn = Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='  Products      ',font='{tw cen mt}',compound=LEFT,image=prodImg,command=lambda:show_frame(frame2),cursor='hand2')
frame2_btn.pack(fill='x', ipady=15,pady=5)

frame3_btn = Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='   Bills            ',font='{tw cen mt}',compound=LEFT,image=billImg,command=lambda:show_frame(frame3),cursor='hand2')
frame3_btn.pack(fill='x', ipady=15,pady=5)

frame4_btn = Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='   Users         ',font='{tw cen mt}',compound=LEFT,image=profImg,command=lambda:show_frame(frame4),cursor='hand2')
frame4_btn.pack(fill='x', ipady=15,pady=5)

frame5_btn = Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='  Settings      ',font='{tw cen mt}',compound=LEFT,image=setImg,command=lambda:show_frame(frame5),cursor='hand2')
frame5_btn.pack(fill='x', ipady=15,pady=5)

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


#plot
plt.style.use('seaborn-dark')
x=[2,3,5,6,7,8,5,4,7,9,5]
y=[3,5,7,8,3,6,7,8,3,5,6]
fig=plt.figure(figsize=(5,2.5))
fig.tight_layout()
ax1=fig.add_subplot(111)
ax1.plot(x,y)
canvas = FigureCanvasTkAgg(fig, master=fm3) 
canvas.get_tk_widget().pack(expand=True)
canvas.draw()








root.mainloop()
