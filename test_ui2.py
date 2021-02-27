from tkinter import *

def showinfo(event):
    lbl1.config(text=txt1.get())

app=Tk()
app.geometry("300x300")
app.title("Simple App")
txt1=Entry(app)
txt1.place(x=40,y=40)
txt1.bind("<Key>",showinfo)
lbl1=Label(app)
lbl1.place(x=40,y=100)
app.mainloop()
