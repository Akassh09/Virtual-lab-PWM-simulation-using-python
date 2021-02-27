from tkinter import *

def showinfo():
    if((v.get()=="arindam") and (v1.get()=="arinban")):
        print("Authenticated")
    else:
        print("Log in failure")

app=Tk()
app.geometry("300x300")
app.title("Simple App")
Label(app,text="User Name",bg="yellow",fg="blue").place(x=40,y=40)
v=StringVar()
txt1=Entry(app,textvariable=v).place(x=120,y=40)
Label(app,text="Password").place(x=40,y=80)
v1=StringVar()
txt2=Entry(app,show="*",textvariable=v1).place(x=120,y=80)
Button(app,text="Submit",command=showinfo).place(x=60,y=120)
app.mainloop()
