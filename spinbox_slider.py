from tkinter import *

def getvalue(event):
    lbl1.config(text=str(x.get()))

def getvalue1(event):
    lbl2.config(text=str(int(spb.get())+1))

obj=Tk()
obj.title("Slider and Spinbox Tutorial")
obj.geometry("350x300")
Label(obj,text="Slider").grid(row=0,column=0)
x=DoubleVar()
sld=Scale(obj,from_=0,to=100,resolution=0.5,variable=x,length=200,orient=HORIZONTAL)
sld.grid(row=0,column=1)
sld.bind("<ButtonRelease>",getvalue)
lbl1=Label(obj,text="NONE")
lbl1.grid(row=1,column=0)
Label(obj,text="Spinbox").grid(row=2,column=0)
spb=Spinbox(obj,from_=0,to=50)
spb.grid(row=2,column=1)
spb.bind("<ButtonRelease>",getvalue1)
lbl2=Label(obj,text="NONE")
lbl2.grid(row=3,column=0)
obj.mainloop()
