import wx

def showinfo(event):
    lbl.SetLabel(str(sld.GetValue()))

app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
pnl=wx.Panel(frm)
sld=wx.Slider(pnl,minValue=0,maxValue=100,pos=(10,10))
sld.Bind(wx.EVT_SLIDER,showinfo)
lbl=wx.StaticText(pnl,pos=(10,100))
frm.Show()
app.MainLoop()
