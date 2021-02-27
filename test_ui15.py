from tkinter import *
from tkinter import messagebox

def showmessage(event):
    lbl.config(text=spb.get())

app=Tk()
app.title("Simple App")
app.geometry("300x300")
spb=Spinbox(app,from_=0,to=50)
spb.place(x=10,y=20)
spb.bind("<Button-1>",showmessage)
lbl=Label(app)
lbl.place(x=10,y=60)
app.mainloop()
