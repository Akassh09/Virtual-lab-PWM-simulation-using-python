from tkinter import *
import serial
board=serial.Serial('COM7',9600)

def showinfo():
    board.write(txt.get().encode())


tk=Tk()
tk.title('Text Display App')
tk.geometry('300x300')
Label(tk,text="Enter Name").place(x=20,y=20)
txt=Entry(tk)
txt.place(x=100,y=20)
Button(tk,text="Submit",command=showinfo).place(x=80,y=80)
tk.mainloop()
