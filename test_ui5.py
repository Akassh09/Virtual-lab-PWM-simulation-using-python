import wx

def showinfo(event):
    if((txt.GetValue()=="arindam") and (txt1.GetValue()=="arinban")):
        print("Authenticated")
    else:
        print("Log in failure")

app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
panel=wx.Panel(frm)
lbl=wx.StaticText(panel,label="User Name",pos=(5,10))
txt=wx.TextCtrl(panel,pos=(100,10))
lbl1=wx.StaticText(panel,label="Password",pos=(5,50))
txt1=wx.TextCtrl(panel,style=wx.TE_PASSWORD,pos=(100,50))
btn=wx.Button(panel,label="Submit",pos=(20,100))
btn.Bind(wx.EVT_BUTTON,showinfo)
frm.Show()
app.MainLoop()
