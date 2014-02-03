import wx

class MainPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)	#�nota�ur eins og er

        # fyrirs�gn
        self.fyrirsogn = wx.StaticText(self, label="Hva� skal gera vi� p�ningana?")
        self.fyrirsognFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.fyrirsogn.SetFont(self.fyrirsognFont)
        mainSizer.Add(self.fyrirsogn, flag=wx.ALL|wx.EXPAND, border=10)

        mainSizer.Add(grid, 0, wx.ALL, 5)

        # labels � l�n
        self.stadaLana = wx.StaticText(self, label="Sta�a l�ns")    
        grid.Add(self.stadaLana, pos=(0,0))

        self.vextir = wx.StaticText(self, label="Vextir")
        grid.Add(self.vextir, pos=(0,2))

        self.greidslubyrgdi = wx.StaticText(self, label="Grei�slubyrg�i")
        grid.Add(self.greidslubyrgdi, pos=(0,4))

        self.timabilLana = wx.StaticText(self, label="T�mabil")
        grid.Add(self.timabilLana, pos=(0,6))

        self.verdtryggtLan = wx.StaticText(self, label="Ver�tryggt/�ver�tryggt")
        grid.Add(self.verdtryggtLan, pos=(0,8))

        self.greidslutypa = wx.StaticText(self, label="Jafnar grei�slur/jafnar afborganir")
        grid.Add(self.greidslutypa, pos=(0,9))
        
        self.umframgreidsla = wx.StaticText(self, label="Umframgreiðsla")
        grid.Add(self.umframgreidsla, pos=(4,6))
        
        self.timabil = wx.StaticText(self, label="Innistæða bundin í:")
        grid.Add(self.timabil, pos=(6,6))
        
        self.verdb = wx.StaticText(self, label="Tímabil verðbólgu:")
        grid.Add(self.verdb, pos=(8,6))
        
        self.verdtrSparn = wx.StaticText(self, label="Ég vil sparnaðinn:")
        grid.Add(self.verdtrSparn, pos=(10,6))
		
        # listar fyrir radio buttons
        self.radioListVerdtrygging = ['Ver�tryggt', '�ver�tryggt']
        self.radioListJafnar = ['Grei�slur', 'Afborganir']
        self.dropdown = ['Ekki bundin', '3 mánuðir', '6 mánuðir', '9 mánuðir', '12 mánuðir']
        self.verdbolga = ['seinustu 15 ár', 'seinustu 10 ár', 'seinustu 5 ár', 'núna']
        self.radioList2 = ['Verðtryggðan', 'Óverðtryggðan']
        
        for i in range(1, 4):
            # innsl�ttur fyrir l�n - self.lani
            lan = 'lan' + str(i)
            setattr(self, lan, wx.TextCtrl(self, size = (80,20)))  
            grid.Add(object.__getattribute__(self, lan), pos=(i,0), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.lan_upph, object.__getattribute__(self, lan))
            
            # kr. merki fyrir l�nsupph�� - self.kronai1
            krona1 = 'krona' + str(i) + '1'
            setattr(self, krona1, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona1), pos=(i,1), flag=wx.TOP, border=17)
            
            # innsl�ttur fyrir vexti - self.vextiri
            vextir = 'vextir' + str(i)
            setattr(self, vextir, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, vextir), pos=(i,2), flag=wx.TOP, border=17)

            # pr�sentumerki - self.prosentai
            prosenta = 'prosenta' + str(i)
            setattr(self, prosenta, wx.StaticText(self, label='%'))
            grid.Add(object.__getattribute__(self, prosenta), pos=(i,3), flag=wx.TOP, border=17)

            # grei�slubyrg�i - self.greidslubyrgdii
            greidslubyrgdi = 'greidslubyrgdi' + str()
            setattr(self, greidslubyrgdi, wx.TextCtrl(self, size = (80,20)))
            grid.Add(object.__getattribute__(self, greidslubyrgdi), pos=(i,4), flag=wx.TOP, border=17)
            
            # kr. merki fyrir grei�slubyrg�i - self.kronai2
            krona2 = 'krona' + str(i) + '2'
            setattr(self, krona2, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona2), pos=(i,5), flag=wx.TOP, border=17)

            # t�mabil l�ns - self.timabilLansi
            timabilLans = 'timabilLans' + str(i)
            setattr(self, timabilLans, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, timabilLans), pos=(i,6), flag=wx.TOP, border=17)

            # m�nu�ir - self.manudiri
            manudir = 'manudir' + str(i)
            setattr(self, manudir, wx.StaticText(self, label='m�n.'))
            grid.Add(object.__getattribute__(self, manudir), pos=(i,7), flag=wx.TOP, border=17)

            # radio buttons fyrir ver�tryggingu - self.verdtryggingi
            verdtrygging = 'verdtrygging' + str(i)
            setattr(self, verdtrygging, wx.RadioBox(self, choices=self.radioListVerdtrygging))
            grid.Add(object.__getattribute__(self, verdtrygging), pos=(i,8), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)

            # radio buttons fyrir jafnar grei�slur/jafnar afborganir
            jafnar = 'jafnar' + str(i)
            setattr(self, jafnar, wx.RadioBox(self, choices=self.radioListJafnar))
            grid.Add(object.__getattribute__(self, jafnar), pos=(i,9), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            
        
	
	umframgreidsla = 'umframgreidsla'
        setattr(self, umframgreidsla, wx.TextCtrl(self, size = (120,20)))
        grid.Add(object.__getattribute__(self, umframgreidsla), pos=(5,6))
        
        timabil = 'timabil'
        setattr(self, timabil, wx.ComboBox(self, choices=self.dropdown, style=wx.CB_READONLY))
        grid.Add(object.__getattribute__(self, timabil), pos=(7,6))
        
        verdbolga = 'verdbolga'
        setattr(self, verdbolga, wx.ComboBox(self, choices=self.verdbolga, style=wx.CB_READONLY))
        grid.Add(object.__getattribute__(self, verdbolga), pos=(9,6))
        
        verdtrSparn = 'verdtrSparn'
        setattr(self, verdtrSparn, wx.RadioBox(self, choices=self.radioList2))
        grid.Add(object.__getattribute__(self, verdtrSparn), pos=(11,6)) 
		
        self.SetSizerAndFit(mainSizer)
        
	def lan_upph(self, event):
		widget = event.GetEventObject()
		if (widget == self.lan1):
			lan1_upph = event.GetString()
		if (widget == self.lan2):
			lan2_upph = event.GetString()
		if (widget == self.lan3):
			lan3_upph = event.GetString()
            

	def timabil(self, event):
    		innist_bundin = event.GetValue()
        
	def umframgreidsla(self, event):
    		umframgr = event.GetString()
        	
	def verdbolga(self, event):
    		verdb = event.GetValue()
        	
	def verdtrSparn(self, event):
    		verdSparn = event.GetString()
        

app = wx.App(False)
frame = wx.Frame(None, title="Fyrsta �tg�fa")
frame.SetSize((600,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
