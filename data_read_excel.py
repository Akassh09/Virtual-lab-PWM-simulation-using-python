import wx
import xlrd
wb=xlrd.open_workbook("name.xlsx")
ws=wb.sheet_by_index(0)
m=ws.nrows
n=ws.ncols
data=[]
for i in range(1,m):
    data.append(ws.cell_value(i,0))


def showinfo(event):
    a=cmb.GetSelection()
    b=ws.cell_value(a+1,1)
    lbl.SetLabel(str(int(b)))

app=wx.App()
frm=wx.Frame(None,title="Simple App",size=(300,300))
pnl=wx.Panel(frm)
cmb=wx.ComboBox(pnl,choices=data,pos=(5,10))
cmb.Bind(wx.EVT_COMBOBOX,showinfo)
lbl=wx.StaticText(pnl,pos=(5,50))
frm.Show()
app.MainLoop()
