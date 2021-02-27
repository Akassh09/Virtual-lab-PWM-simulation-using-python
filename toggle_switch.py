from tkinter import *
from tkinter import messagebox

def showinfo():
    a=btn.config("text")[4]
    if(a=="Switch on"):
        btn.config(text="Switch off")
        messagebox.showinfo(title="Message",message="I am switched on")
    elif(a=="Switch off"):
        btn.config(text="Switch on")
        messagebox.showinfo(title="Message",message="I am switched off")
    

app=Tk()
app.title("Simple Application")
app.geometry("300x300")
btn=Button(app,text="Switch on",command=showinfo)
btn.place(x=20,y=20)
app.mainloop()
