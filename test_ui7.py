import wx

def showinfo(event):
    wx.MessageBox(cmb.GetStringSelection(),caption="Message")

app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
panel=wx.Panel(frm)
cmb=wx.ComboBox(panel,choices=["India","Srilanka","Nepal","Bhutan","China"],pos=(5,10))
cmb.Bind(wx.EVT_COMBOBOX,showinfo)
frm.Show()
app.MainLoop()
