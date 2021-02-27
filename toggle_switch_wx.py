import wx

def showinfo(event):
    a=event.GetEventObject().GetLabel()
    if(a=="Switch on"):
        btn.SetLabel("Switch off")
    elif(a=="Switch off"):
        btn.SetLabel("Switch on")

app=wx.App()
frm=wx.Frame(None,title="Simple Application",size=(300,300))
panel=wx.Panel(frm)
btn=wx.ToggleButton(panel,label="Switch on",pos=(10,10))
btn.Bind(wx.EVT_TOGGLEBUTTON,showinfo)
frm.Show()
app.MainLoop()
