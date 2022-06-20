import tkinter as tk
from tkinter import CENTER, N, SOLID, PhotoImage, messagebox

    
root = tk.Tk()
root.state('zoomed')
root.title('ASAP-LOGIN V-1.0.0'.center(220))
root.iconbitmap('logo.ico')
root.configure(background='#DDC9FF')
maincolor='#DDC9FF'

#row-config
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)

#image
img=PhotoImage(file='F:/tkn/ASAP/admin dashboard/bard.png')

#tab-commands
def show_frame(frame): 
    frame.tkraise()

def signout():
    exitApp=messagebox.askquestion('signout','Do you reallllllly want to signout?',icon='warning',default='no')
    if exitApp=='yes':
        root.quit()


#frames
frame1 = tk.Frame(root,bg='red')
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
btnframe = tk.Frame(root)
btnframe.grid(row=0,column=0,sticky=N)

#frame placement
for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0,column=1,sticky='nsew')
    
#dashboard-frames
frame1_title=  tk.Label(frame1, text='Page 1', font='times 35', bg='red')
frame1_title.pack(expand=True)


frame2_title=  tk.Label(frame2, text='Page 2', font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)


frame2_title=  tk.Label(frame3, text='Page 3', font='times 35', bg='purple')
frame2_title.pack(fill='both', expand=True)


frame2_title=  tk.Label(frame4, text='Page 4', font='times 35', bg='blue')
frame2_title.pack(fill='both', expand=True)


frame2_title=  tk.Label(frame5, text='Page 5', font='times 35', bg='pink')
frame2_title.pack(fill='both', expand=True)



show_frame(frame1)

#buttons
frame1_btn = tk.Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='Dashboard',compound=CENTER,command=lambda:show_frame(frame1))
frame1_btn.pack(fill='x', ipady=15)


frame2_btn = tk.Button(btnframe,width=28,activebackground=maincolor,border=0,bg=maincolor, text='Products',command=lambda:show_frame(frame2))
frame2_btn.pack(fill='x', ipady=15)

frame3_btn = tk.Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='Bills',command=lambda:show_frame(frame3))
frame3_btn.pack(fill='x', ipady=15)

frame4_btn = tk.Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='Users',command=lambda:show_frame(frame4))
frame4_btn.pack(fill='x', ipady=15)

frame5_btn = tk.Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='Settings',command=lambda:show_frame(frame5))
frame5_btn.pack(fill='x', ipady=15)

frame6_btn = tk.Button(btnframe,activebackground=maincolor,border=0,bg=maincolor, text='Signout',command=signout)
frame6_btn.pack(fill='x', ipady=15)

#plot


root.mainloop()