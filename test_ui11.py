from tkinter import *

def showinfo(event):
    lbl.config(text=str(sld.get()))

app=Tk()
app.title("Simple Application")
app.geometry("300x300")
sld=Scale(app,from_=0,to=100,orient=HORIZONTAL)
sld.place(x=10,y=10)
sld.bind("<ButtonRelease-1>",showinfo)
lbl=Label(app)
lbl.place(x=10,y=60)
app.mainloop()
