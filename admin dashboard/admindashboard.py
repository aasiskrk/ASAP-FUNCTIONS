from tkinter import colorchooser
from tkinter import *
from tkinter import messagebox
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pip import main
from pyparsing import White


#colourvar
maincolor='#DDC9FF'
    
root = Tk()

root.state('zoomed')
root.title('ASAP-LOGIN V-1.0.0'.center(220))
root.iconbitmap('Logo.ico')
root.configure(background=maincolor)

#row-config
root.columnconfigure(1,weight=1)
root.columnconfigure(0,weight=2)
root.rowconfigure(0,weight=1)
#image
dir1='F:/tkn\ASAP/admin dashboard/'
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


frame2_title=  Label(frame4, font='times 35', bg='blue')
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


show_frame(frame5,1)
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




#settings

def choose_color():
    maicolor = colorchooser.askcolor(title ="Choose color")
    root.configure(background=maicolor[1])
    btnframe.configure(background=maicolor[1])
    frame1.configure(background=maicolor[1])
    frame1_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame2_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame3_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame4_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    frame5_btn.configure(activebackground=maicolor[1],bg=maicolor[1])
    button_custom.configure(activebackground=maicolor[1],bg=maicolor[1],border=2)


def defined_color(color,btncode):
    root.configure(background=color)
    btnframe.configure(background=color)
    frame1.configure(background=color)
    frame1_btn.configure(activebackground=color,bg=color)
    frame2_btn.configure(activebackground=color,bg=color)
    frame3_btn.configure(activebackground=color,bg=color)
    frame4_btn.configure(activebackground=color,bg=color)
    frame5_btn.configure(activebackground=color,bg=color)
    
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
