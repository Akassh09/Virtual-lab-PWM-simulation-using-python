import wx
a=open("data.txt","r")
data=a.read().splitlines()



app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
pnl=wx.Panel(frm)
cmb=wx.ComboBox(pnl,choices=data,pos=(5,10))
frm.Show()
app.MainLoop()
