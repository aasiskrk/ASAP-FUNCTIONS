from tkinter import*
import os
import tempfile
def print_area(txt):
    temp_file=tempfile.mktemp('.txt')
    open(temp_file,'w').write(txt)
    os.startfile(temp_file,'print')
root = Tk()
root.title("printing Demo")
root.geometry("900x600")

lbl_print = Label(root,text="printing Area:", fg="brown").place(x=100,y=20)
text_area = Text(root, bg="light yellow",font='{tw cen mt}')
text_area.place(x=100, y=100, width=400,height=300)
btn_print = Button(root, text ="print",bg="green",fg="brown", activebackground="yellow",command=lambda:print_area(text_area.get('1.0',END)))
btn_print.place(x=300, y= 400)

root.mainloop()