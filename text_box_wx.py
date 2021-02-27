import wx
import serial
#board=serial.Serial('COM7',9600)

def showinfo(event):
    #board.write(txt.GetValue().encode())
    print('Hi')

app=wx.App()
frm=wx.Frame(None,title="Simple Text Display App",size=(300,300))
pnl=wx.Panel(frm)
lbl=wx.StaticText(pnl,label="Enter Name",pos=(5,10))
txt=wx.TextCtrl(pnl,pos=(100,10))
btn=wx.Button(pnl,label="Submit",pos=(50,50))
btn.Bind(wx.EVT_BUTTON,showinfo)
frm.Show()
app.MainLoop()

