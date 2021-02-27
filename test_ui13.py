from tkinter import *

def showinfo():
    a=x.get()
    if(a==True):
        lbl.config(text="I am checked")
    else:
        lbl.config(text="I am unchecked")

app=Tk()
app.title("Simple App")
app.geometry("300x300")
x=BooleanVar()
chk=Checkbutton(app,text="Click me",variable=x,command=showinfo)
chk.place(x=10,y=20)
lbl=Label(app)
lbl.place(x=10,y=60)
app.mainloop()
