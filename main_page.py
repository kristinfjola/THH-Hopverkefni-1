# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
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

        self.timabilLana = wx.StaticText(self, label="Tímabil")
        grid.Add(self.timabilLana, pos=(0,6))

        self.verdtryggtLan = wx.StaticText(self, label="Verðtryggt/óverðtryggt")
        grid.Add(self.verdtryggtLan, pos=(0,8))

        self.greidslutypa = wx.StaticText(self, label="Jafnar greiðslur/jafnar afborganir")
        grid.Add(self.greidslutypa, pos=(0,9))
        
        self.umframgreidsla = wx.StaticText(self, label="Umframgreiðsla")
        grid.Add(self.umframgreidsla, pos=(4,6))
        
        self.timabil = wx.StaticText(self, label="Innistæða bundin í:")
        grid.Add(self.timabil, pos=(6,6))
        
        self.verdb = wx.StaticText(self, label="Tímabil verðbólgu:")
        grid.Add(self.verdb, pos=(8,6))
        
        self.verdtrSparn = wx.StaticText(self, label="Ég vil sparnaðinn:")
        grid.Add(self.verdtrSparn, pos=(10,6))
        
        
		
        self.radioListVerdtrygging = ['Verðtryggt', 'Óverðtryggt']
        self.radioListJafnar = ['Greiðslur', 'Afborganir']
        self.dropdown = ['ekki bundin', '3 mánuðir', '6 mánuðir', '9 mánuðir', '12 mánuðir']
        self.verdbolga = ['seinustu 15 ár', 'seinustu 10 ár', 'seinustu 5 ár', 'núna']
        self.radioList2 = ['Verðtryggðan', 'Óverðtryggðan']
        
        for i in range(1, 4):
            # innsláttur fyrir lán - self.lani
            lan = 'lan' + str(i)
            setattr(self, lan, wx.TextCtrl(self, size = (80,20)))  
            grid.Add(object.__getattribute__(self, lan), pos=(i,0), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.upphaed_lana, object.__getattribute__(self, lan))
            
            # kr. merki fyrir lánsupphæð - self.kronai1
            krona1 = 'krona' + str(i) + '1'
            setattr(self, krona1, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona1), pos=(i,1), flag=wx.TOP, border=17)
            
            # innsláttur fyrir vexti - self.vextiri
            vextir = 'vextir' + str(i)
            setattr(self, vextir, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, vextir), pos=(i,2), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.vextir_lana, object.__getattribute__(self, vextir))

            # prósentumerki - self.prosentai
            prosenta = 'prosenta' + str(i)
            setattr(self, prosenta, wx.StaticText(self, label='%'))
            grid.Add(object.__getattribute__(self, prosenta), pos=(i,3), flag=wx.TOP, border=17)

            # greiðslubyrgði - self.greidslubyrgdii
            greidslubyrgdi = 'greidslubyrgdi' + str(i)
            setattr(self, greidslubyrgdi, wx.TextCtrl(self, size = (80,20)))
            grid.Add(object.__getattribute__(self, greidslubyrgdi), pos=(i,4), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.greidslubyrgdi_lana, object.__getattribute__(self, greidslubyrgdi))
            
            # kr. merki fyrir greiðslubyrgði - self.kronai2
            krona2 = 'krona' + str(i) + '2'
            setattr(self, krona2, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona2), pos=(i,5), flag=wx.TOP, border=17)

            # tímabil láns - self.timabilLansi
            timabilLans = 'timabilLans' + str(i)
            setattr(self, timabilLans, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, timabilLans), pos=(i,6), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.timabil_lana, object.__getattribute__(self, timabilLans))

            # mánuðir - self.manudiri
            manudir = 'manudir' + str(i)
            setattr(self, manudir, wx.StaticText(self, label='mán.'))
            grid.Add(object.__getattribute__(self, manudir), pos=(i,7), flag=wx.TOP, border=17)

            # radio buttons fyrir verðtryggingu - self.verdtryggingi
            verdtrygging = 'verdtrygging' + str(i)
            setattr(self, verdtrygging, wx.RadioBox(self, choices=self.radioListVerdtrygging))
            grid.Add(object.__getattribute__(self, verdtrygging), pos=(i,8), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.verdtrygging_lana, object.__getattribute__(self, verdtrygging))

            # radio buttons fyrir jafnar greiðslur/jafnar afborganir
            jafnar = 'jafnar' + str(i)
            setattr(self, jafnar, wx.RadioBox(self, choices=self.radioListJafnar))
            grid.Add(object.__getattribute__(self, jafnar), pos=(i,9), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.jafnar_lana, object.__getattribute__(self, jafnar))

        self.umframgr = wx.TextCtrl(self, size = (120,20))
        grid.Add(self.umframgr, pos=(5,6))
        
        self.timab = wx.ComboBox(self, choices=self.dropdown, style=wx.CB_READONLY)
        grid.Add(self.timab, pos=(7,6))
        
        self.verdb = wx.ComboBox(self, choices=self.verdbolga, style=wx.CB_READONLY)
        grid.Add(self.verdb, pos=(9,6))
        
        self.verdSparn = wx.RadioBox(self, choices=self.radioList2)
        grid.Add(self.verdSparn, pos=(11,6))
        
        self.SetSizerAndFit(mainSizer)
        
    def upphaed_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.lan1):
            lan1_upph = event.GetString()
        if (widget == self.lan2):
            lan2_upph = event.GetString()
        if (widget == self.lan3):
            lan3_upph = event.GetString()

    def vextir_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.vextir1):
            lan1_vextir = event.GetString()
        if (widget == self.vextir2):
            lan2_vextir = event.GetString()
        if (widget == self.vextir3):
            lan3_vextir = event.GetString()

    def greidslubyrgdi_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.greidslubyrgdi1):
            lan1_greidslubyrgdi = event.GetString()
        if (widget == self.greidslubyrgdi2):
            lan2_greidslubyrgdi = event.GetString()
        if (widget == self.greidslubyrgdi3):
            lan3_greidslubyrgdi = event.GetString()

    def timabil_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.timabilLans1):
            lan1_timabil = event.GetString()
        if (widget == self.timabilLans2):
            lan2_timabil = event.GetString()
        if (widget == self.timabilLans3):
            lan3_timabil = event.GetString()

    def verdtrygging_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.verdtrygging1):
            lan1_verdtrygging = event.GetString()
        if (widget == self.verdtrygging2):
            lan2_verdtrygging = event.GetString()
        if (widget == self.verdtrygging3):
            lan3_verdtrygging = event.GetString()

    def timabil(self, event):
    	innist_bundin = event.GetValue()
    	
    
    def umframgreidsla(self, event):
    	umframgr = event.GetString()
    	
    def verdbolga(self, event):
    	verdb = event.GetValue()
    
    def verdtrSparn(self, event):
    	verdSparn = event.GetString()
    
    def jafnar_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.jafnar1):
            lan1_jafnar = event.GetInt()
        if (widget == self.jafnar2):
            lan2_jafnar = event.GetInt()
        if (widget == self.jafnar3):
            lan3_jafnar = event.GetInt()
            
        

app = wx.App(False)
frame = wx.Frame(None, title="Fyrsta útgáfa")
frame.SetSize((800,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
