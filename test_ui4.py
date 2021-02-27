from tkinter import *
from tkinter import ttk

a=[]
def includeinfo():
    a.append(txt.get())
    cmb.config(values=a)

app=Tk()
app.geometry("300x300")
app.title("Simple App")
txt=Entry(app)
txt.place(x=0,y=0)
Button(app,text="Enter",command=includeinfo).place(x=0,y=40)
cmb=ttk.Combobox(app)
cmb.place(x=0,y=80)
app.mainloop()
