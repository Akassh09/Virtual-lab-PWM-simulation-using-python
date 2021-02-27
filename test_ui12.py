from tkinter import *

def showinfo():
    a=x.get()
    if(a==1):
        lbl.config(text=str(rdb1['text']))
    elif(a==2):
        lbl.config(text=str(rdb2['text']))
    elif(a==3):
        lbl.config(text=str(rdb3['text']))

app=Tk()
app.title("Simple Application")
app.geometry("300x300")
x=IntVar()
rdb1=Radiobutton(app,text="SC",value=1,variable=x,command=showinfo)
rdb2=Radiobutton(app,text="ST",value=2,variable=x,command=showinfo)
rdb3=Radiobutton(app,text="OBC",value=3,variable=x,command=showinfo)
rdb1.place(x=10,y=10)
rdb2.place(x=50,y=10)
rdb3.place(x=90,y=10)
lbl=Label(app)
lbl.place(x=10,y=60)
app.mainloop()
