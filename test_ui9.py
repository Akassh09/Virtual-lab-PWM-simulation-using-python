import wx

def showinfo(event):
    a=lbx.GetStringSelection()
    if(a=="Other"):
        txt.Enable(True)
    else:
        txt.Enable(False)

app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
pnl=wx.Panel(frm)
lbx=wx.ListBox(pnl,choices=["Bengali","English","Hindi","Other"],pos=(10,20))
lbx.Bind(wx.EVT_LISTBOX,showinfo)
txt=wx.TextCtrl(pnl,pos=(10,100))
txt.Enable(False)
frm.Show()
app.MainLoop()
