from tkinter import *


app=Tk()
app.geometry("600x600")
app.title("PWM using 555 timer")


def calculate():
    lbl4.config(text=(float(y.get())+float(x.get()))*0.69*float(z.get()))
    lbl5.config(text=float(z.get()+y.get())*0.69)

x=DoubleVar()
y=DoubleVar()
z=DoubleVar()
m = DoubleVar()
n = DoubleVar()


Label(app,text="Value of R1 (in Ω)").grid(row=0,column=0)
s1=Scale(app,from_=0,to=100,resolution=0.5,variable=x,length=200,orient=HORIZONTAL)
s1.grid(row=0,column=1)
s1.bind("<ButtonRelease>")



Label(app,text="Value of R2 (in Ω)").grid(row=1,column=0)
s2=Scale(app,from_=0,to=100,resolution=0.5,variable=y,length=200,orient=HORIZONTAL)
s2.grid(row=1,column=1)
s2.bind("<ButtonRelease>")



Label(app,text="Value of C (in F)").grid(row=2,column=0)
s3=Scale(app,from_=0,to=100,resolution=0.5,variable=z,length=200,orient=HORIZONTAL)
s3.grid(row=2,column=1)
s3.bind("<ButtonRelease>")


Button(app,text="Switch On",command=calculate).grid(row=10,column=0)
Label(app,text="On time:").grid(row=15,column=0)
lbl4=Label(app,text="")
lbl4.grid(row=15,column=1)
Label(app,text="Off time:").grid(row=17,column=0)
lbl5=Label(app,text="")
lbl5.grid(row=17,column=1)


app.mainloop()