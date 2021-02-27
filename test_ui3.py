from tkinter import *
from tkinter import ttk

def showinfo(event):
    print(cmb.get())

app=Tk()
app.geometry("300x300")
app.title("Simple App")
cmb=ttk.Combobox(app,values=['India','Bangladesh','Srilanka','Pakistan'])
cmb.place(x=0,y=20)
cmb.bind("<<ComboboxSelected>>",showinfo)
app.mainloop()
