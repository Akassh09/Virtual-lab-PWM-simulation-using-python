from tkinter import *
from tkinter import messagebox

def showinfo():
    a=x.get()
    if(a==True):
        btn.config(state=NORMAL)
    else:
        btn.config(state=DISABLED)

def display():
    messagebox.showinfo("Message","You clicked the button")

app=Tk()
app.title("Simple App")
app.geometry("300x300")
x=BooleanVar()
chk=Checkbutton(app,text="I agree with the terms and conditions",variable=x,command=showinfo)
chk.place(x=10,y=20)
btn=Button(app,text="Submit",command=display)
btn.place(x=10,y=60)
btn.config(state=DISABLED)
app.mainloop()
