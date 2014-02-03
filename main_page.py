import wx

class MainPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)


        # fyrirsögn
        self.fyrirsogn = wx.StaticText(self, label="Hvað skal gera við péningana?")
        self.fyrirsognFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.fyrirsogn.SetFont(self.fyrirsognFont)
        mainSizer.Add(self.fyrirsogn, flag=wx.ALL|wx.EXPAND, border=10)

        mainSizer.Add(grid, 0, wx.ALL, 5)

        # labels á lán
        self.stadaLana = wx.StaticText(self, label="Staða láns")    
        grid.Add(self.stadaLana, pos=(0,0))

        self.vextir = wx.StaticText(self, label="Vextir")
        grid.Add(self.vextir, pos=(0,2))

        self.greidslubyrgdi = wx.StaticText(self, label="Greiðslubyrgði")
        grid.Add(self.greidslubyrgdi, pos=(0,4))

        self.verdtryggtLan = wx.StaticText(self, label="Verðtryggt/óverðtryggt")
        grid.Add(self.verdtryggtLan, pos=(0,6))
        
        '''
        "HARÐKÓÐAÐ"
        # inputs og valmöguleikar fyrir lán
        self.lan1 = wx.TextCtrl(self, size = (80,20))
        grid.Add(self.lan1, pos=(1,0))
        self.kr11 = wx.StaticText(self, label="kr.")
        grid.Add(self.kr11, pos=(1,1))

        self.vextir1 = wx.TextCtrl(self, size = (50,20))
        grid.Add(self.vextir1, pos=(1,2))
        self.prosenta = wx.StaticText(self, label="%")
        grid.Add(self.prosenta, pos=(1,3))

        self.greidslubyrgdi1 = wx.TextCtrl(self, size = (80,20))
        grid.Add(self.greidslubyrgdi1, pos=(1,4))
        self.kr12 = wx.StaticText(self, label="kr.")
        grid.Add(self.kr12, pos=(1,5))
        
        radioList1 = ['Verðtryggt', 'Óverðtryggt']
        self.radios1 = wx.RadioBox(self, choices=radioList1)
        grid.Add(self.radios1, pos=(1,6))

        '''
        self.radioList = ['Verðtryggt', 'Óverðtryggt']
        
        for i in range(1, 4):
            # innsláttur fyrir lán - self.lani
            lan = 'lan' + str(i)
            setattr(self, lan, wx.TextCtrl(self, size = (80,20)))  
            grid.Add(object.__getattribute__(self, lan), pos=(i,0), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.lan_upph, object.__getattribute__(self, lan))
            
            # kr. merki fyrir lánsupphæð - self.kronai1
            krona1 = 'krona' + str(i) + '1'
            setattr(self, krona1, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona1), pos=(i,1), flag=wx.TOP, border=17)
            
            # innsláttur fyrir vexti - self.vextiri
            vextir = 'vextir' + str(i)
            setattr(self, vextir, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, vextir), pos=(i,2), flag=wx.TOP, border=17)

            # prósentumerki - self.prosentai
            prosenta = 'prosenta' + str(i)
            setattr(self, prosenta, wx.StaticText(self, label='%'))
            grid.Add(object.__getattribute__(self, prosenta), pos=(i,3), flag=wx.TOP, border=17)

            # greiðslubyrgði - self.greidslubyrgdii
            greidslubyrgdi = 'greidslubyrgdi' + str()
            setattr(self, greidslubyrgdi, wx.TextCtrl(self, size = (80,20)))
            grid.Add(object.__getattribute__(self, greidslubyrgdi), pos=(i,4), flag=wx.TOP, border=17)
            
            # kr. merki fyrir greiðslubyrgði - self.kronai2
            krona2 = 'krona' + str(i) + '2'
            setattr(self, krona2, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona2), pos=(i,5), flag=wx.TOP, border=17)

            # radio buttons fyrir verðtryggingu - self.verdtryggingi
            verdtrygging = 'verdtrygging' + str(i)
            setattr(self, verdtrygging, wx.RadioBox(self, choices=self.radioList))
            grid.Add(object.__getattribute__(self, verdtrygging), pos=(i,6), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            
        

        self.SetSizerAndFit(mainSizer)
        
    def lan_upph(self, event):
        widget = event.GetEventObject()
        if (widget == self.lan1):
            lan1_upph = event.GetString()
        if (widget == self.lan2):
            lan2_upph = event.GetString()
        if (widget == self.lan3):
            lan3_upph = event.GetString()
        

app = wx.App(False)
frame = wx.Frame(None, title="Fyrsta útgáfa")
frame.SetSize((600,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
