from tkinter import *
import serial
board=serial.Serial('COM7',9600)

def showinfo(event):
    board.write(txt.get().encode())
    lbl.config(text=txt.get())

tk=Tk()
tk.title('Simple App')
tk.geometry('300x300')
txt=Entry(tk)
txt.place(x=20,y=20)
lbl=Label(tk)
lbl.place(x=20,y=60)
txt.bind("<Key>",showinfo)
tk.mainloop()

