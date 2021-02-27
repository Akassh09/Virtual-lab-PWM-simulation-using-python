from tkinter import *

def showinfo(event):
    a=lbx.get(lbx.curselection()[0])
    if(a=="Other"):
        txt.config(state=NORMAL)
    else:
        txt.config(state=DISABLED)

app=Tk()
app.title("Simple App")
app.geometry("300x300")
lbx=Listbox(app,selectmode=SINGLE)
lbx.insert(0,"Bengali")
lbx.insert(1,"English")
lbx.insert(2,"Hindi")
lbx.insert(3,"Other")
lbx.place(x=10,y=10)
lbx.bind("<<ListboxSelect>>",showinfo)
txt=Entry(app,state=DISABLED)
txt.place(x=10,y=200)
app.mainloop()
