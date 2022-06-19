import tkinter as tk


    
root = tk.Tk()
root.state('zoomed')

root.columnconfigure(1,weight=10)
root.rowconfigure(0,weight=1)


#tab-commands
def show_frame(frame): 
    frame.tkraise()


#frames
frame1 = tk.Frame(root,bg='red')
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame3.grid(row=0,column=0)

#frame placement
for frame in (frame1, frame2):
    frame.grid(row=0,column=1,sticky='nsew')
    
#dashboard-frames
frame1_title=  tk.Label(frame1, text='Page 1', font='times 35', bg='red')
frame1_title.pack(fill='both', expand=True)


frame2_title=  tk.Label(frame2, text='Page 2', font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)

show_frame(frame1)

#buttons
frame1_btn = tk.Button(frame3, text='Enter',command=lambda:show_frame(frame1))
frame1_btn.pack(fill='x', ipady=15)


frame2_btn = tk.Button(frame3, text='Enter',command=lambda:show_frame(frame2))
frame2_btn.pack(fill='x', ipady=15)


#plot


root.mainloop()