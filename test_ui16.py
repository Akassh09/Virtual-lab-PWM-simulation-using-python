from tkinter import *
from tkinter import messagebox

def showmessage():
    lbl.config(text=spb.get())

app=Tk()
app.title("Simple App")
app.geometry("300x300")
spb=Spinbox(app,from_=0,to=50)
spb.place(x=10,y=20)
btn=Button(app,text="Show value",command=showmessage)
btn.place(x=10,y=50)
lbl=Label(app)
lbl.place(x=10,y=80)
app.mainloop()
