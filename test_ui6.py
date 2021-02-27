import wx

def showinfo(event):
    lbl.SetLabel(txt.GetValue())

app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
panel=wx.Panel(frm)
txt=wx.TextCtrl(panel,pos=(5,10))
txt.Bind(wx.EVT_TEXT,showinfo)
lbl=wx.StaticText(panel,pos=(5,50))
lbl.SetBackgroundColour("red")
lbl.SetForegroundColour("green")
frm.Show()
app.MainLoop()
