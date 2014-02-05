# -*- coding: cp1252 -*-
import wx
import sparnadur1b
import lan_v

class MainPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        grid2 = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)


        # fyrirs�gn
        self.fyrirsogn = wx.StaticText(self, label="Hva� skal gera vi� peningana?")
        self.fyrirsognFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.fyrirsogn.SetFont(self.fyrirsognFont)
        mainSizer.Add(self.fyrirsogn, flag=wx.ALL|wx.EXPAND, border=10)

        # reikna sparnap
        self.reiknaSparnad = wx.Button(self, label="Reikna sparna�")
        self.Bind(wx.EVT_BUTTON, self.reikna_sparnad, self.reiknaSparnad)

        mainSizer.Add(grid2, 0, wx.ALL, 5)
        mainSizer.Add(self.reiknaSparnad, 0, wx.ALL, 5)
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

        self.verdtryggtLan = wx.StaticText(self, label="�ver�tryggt/Ver�tryggt")
        grid.Add(self.verdtryggtLan, pos=(0,8))
	
        self.greidslutypa = wx.StaticText(self, label="Jafnar grei�slur/jafnar afborganir")
        grid.Add(self.greidslutypa, pos=(0,9))

        # labels � sparna�
        self.umframgreidsla = wx.StaticText(self, label="Umframgrei�sla � m�nu�i")
        grid2.Add(self.umframgreidsla, pos=(0,0))

        self.umframgreidsla = wx.StaticText(self, label="Hvernig sparna�arreikning?")
        grid2.Add(self.umframgreidsla, pos=(1,0), flag=wx.TOP, border=10)
        
        self.timabil = wx.StaticText(self, label="Innist��a m� vera bundin �:")
        grid2.Add(self.timabil, pos=(2,4), flag=wx.TOP, border=17)
        
        self.verdb = wx.StaticText(self, label="T�mabil ver�b�lgu:")
        grid2.Add(self.verdb, pos=(2,2), flag=wx.TOP, border=17)
        
        self.verdtrSparn = wx.StaticText(self, label="�g vil sparna�inn:")
        grid2.Add(self.verdtrSparn, pos=(2,0), flag=wx.TOP, border=17)
        
        
		
        self.radioListVerdtrygging = ['�ver�tryggt', 'Ver�tryggt']
        self.radioListJafnar = ['Grei�slur', 'Afborganir']
        self.dropdown = ['ekki bundin', '3 m�nu�ir', '6 m�nu�ir', '9 m�nu�ir', '12 m�nu�ir']
        self.verdbolga_ = ['seinustu 15 �r', 'seinustu 10 �r', 'seinustu 5 �r', 'n�na']
        self.radioList2 = ['�ver�trygg�an', 'Ver�trygg�an']
        
        for i in range(1, 4):
            # innsl�ttur fyrir l�n - self.lani
            lan = 'lan' + str(i)
            setattr(self, lan, wx.TextCtrl(self, size = (80,20)))  
            grid.Add(object.__getattribute__(self, lan), pos=(i,0), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.upphaed_lana, object.__getattribute__(self, lan))
            
            # kr. merki fyrir l�nsupph�� - self.kronai1
            krona1 = 'krona' + str(i) + '1'
            setattr(self, krona1, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona1), pos=(i,1), flag=wx.TOP, border=17)
            
            # innsl�ttur fyrir vexti - self.vextiri
            vextir = 'vextir' + str(i)
            setattr(self, vextir, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, vextir), pos=(i,2), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.vextir_lana, object.__getattribute__(self, vextir))

            # pr�sentumerki - self.prosentai
            prosenta = 'prosenta' + str(i)
            setattr(self, prosenta, wx.StaticText(self, label='%'))
            grid.Add(object.__getattribute__(self, prosenta), pos=(i,3), flag=wx.TOP, border=17)

            # grei�slubyrg�i - self.greidslubyrgdii
            greidslubyrgdi = 'greidslubyrgdi' + str(i)
            setattr(self, greidslubyrgdi, wx.TextCtrl(self, size = (80,20)))
            grid.Add(object.__getattribute__(self, greidslubyrgdi), pos=(i,4), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.greidslubyrgdi_lana, object.__getattribute__(self, greidslubyrgdi))
            
            # kr. merki fyrir grei�slubyrg�i - self.kronai2
            krona2 = 'krona' + str(i) + '2'
            setattr(self, krona2, wx.StaticText(self, label='kr.'))
            grid.Add(object.__getattribute__(self, krona2), pos=(i,5), flag=wx.TOP, border=17)

            # t�mabil l�ns - self.timabilLansi
            timabilLans = 'timabilLans' + str(i)
            setattr(self, timabilLans, wx.TextCtrl(self, size = (50,20)))
            grid.Add(object.__getattribute__(self, timabilLans), pos=(i,6), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.timabil_lana, object.__getattribute__(self, timabilLans))

           # ar - self.ari
            ar = 'ar' + str(i)
            setattr(self, ar, wx.StaticText(self, label='�r'))
            grid.Add(object.__getattribute__(self, ar), pos=(i,7), flag=wx.TOP, border=17)
			
            # radio buttons fyrir ver�tryggingu - self.verdtryggingi
            verdtrygging = 'verdtrygging' + str(i)
            setattr(self, verdtrygging, wx.RadioBox(self, choices=self.radioListVerdtrygging))
            grid.Add(object.__getattribute__(self, verdtrygging), pos=(i,8), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.verdtrygging_lana, object.__getattribute__(self, verdtrygging))

            # radio buttons fyrir jafnar grei�slur/jafnar afborganir
            jafnar = 'jafnar' + str(i)
            setattr(self, jafnar, wx.RadioBox(self, choices=self.radioListJafnar))
            grid.Add(object.__getattribute__(self, jafnar), pos=(i,9), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.jafnar_lana, object.__getattribute__(self, jafnar))

        # sparna�ar input
        self.umframgr_ = wx.TextCtrl(self, size = (270,20))
        grid2.Add(self.umframgr_, pos=(0,1))
        self.Bind(wx.EVT_TEXT, self._umframgreidsla, self.umframgr_)
        
        self.timab = wx.ComboBox(self, choices=self.dropdown, style=wx.CB_READONLY)
        grid2.Add(self.timab, pos=(2,5), flag=wx.TOP, border=17)
        self.Bind(wx.EVT_COMBOBOX, self._timabil, self.timab)
        
        self.verdb = wx.ComboBox(self, choices=self.verdbolga_, style=wx.CB_READONLY)
        grid2.Add(self.verdb, pos=(2,3), flag=wx.TOP, border=17)
        self.Bind(wx.EVT_COMBOBOX, self._verdbolga, self.verdb)
        
        self.verdSparn_ = wx.RadioBox(self, choices=self.radioList2)
        grid2.Add(self.verdSparn_, pos=(2,1))
        self.Bind(wx.EVT_RADIOBOX, self._verdtrSparn, self.verdSparn_)
        
        # reikna l�n
        self.reiknaLan = wx.Button(self, label="Reikna l�n")
        self.Bind(wx.EVT_BUTTON, self.reikna_lan, self.reiknaLan)
        mainSizer.Add(self.reiknaLan, 0, wx.ALL, 5)

        # upphafsstilla allar breytur sem 0
        self.lan1_upph = self.lan2_upph = self.lan3_upph = self.lan1_vextir = self.lan2_vextir = self.lan3_vextir = self.lan1_greidslubyrgdi = self.lan2_greidslubyrgdi = self.lan3_greidslubyrgdi = self.lan1_timabil = self.lan2_timabil = self.lan3_timabil =  self.lan1_verdtrygging =  self.lan2_verdtrygging =  self.lan3_verdtrygging = self.lan1_jafnar = self.lan2_jafnar = self.lan3_jafnar = self.umframgr = 0
        
        self.verdbolga = 15
        self.verdSparn = 0
        
        
        self.SetSizerAndFit(mainSizer)
        
    def upphaed_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.lan1):
            self.lan1_upph = int(event.GetString())
        if (widget == self.lan2):
            self.lan2_upph = int(event.GetString())
        if (widget == self.lan3):
            self.lan3_upph = int(event.GetString())

    def vextir_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.vextir1):
            self.lan1_vextir = float(event.GetString())
        if (widget == self.vextir2):
            self.lan2_vextir = float(event.GetString())
        if (widget == self.vextir3):
            self.lan3_vextir = float(event.GetString())

    def greidslubyrgdi_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.greidslubyrgdi1):
            self.lan1_greidslubyrgdi = int(event.GetString())
        if (widget == self.greidslubyrgdi2):
            self.lan2_greidslubyrgdi = int(event.GetString())
        if (widget == self.greidslubyrgdi3):
            self.lan3_greidslubyrgdi = int(event.GetString())

    def timabil_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.timabilLans1):
            self.lan1_timabil = int(event.GetString())
        if (widget == self.timabilLans2):
            self.lan2_timabil = int(event.GetString())
        if (widget == self.timabilLans3):
            self.lan3_timabil = int(event.GetString())

    def verdtrygging_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.verdtrygging1):
            self.lan1_verdtrygging = event.GetInt()
        if (widget == self.verdtrygging2):
            self.lan2_verdtrygging = event.GetInt()
        if (widget == self.verdtrygging3):
            self.lan3_verdtrygging = event.GetInt()

    def jafnar_lana(self, event):
        widget = event.GetEventObject()
        if (widget == self.jafnar1):
            self.lan1_jafnar = event.GetInt()
        if (widget == self.jafnar2):
            self.lan2_jafnar = event.GetInt()
        if (widget == self.jafnar3):
            self.lan3_jafnar = event.GetInt()

    def _timabil(self, event):
        self.innist_bundin = event.GetString()[:1]
        if(self.innist_bundin == "1"):
        	self.innist_bundin = "12"
        if(self.innist_bundin == "e"):
        	self.innist_bundin = 0
        self.innist_bundin = int(self.innist_bundin)
        
    def _umframgreidsla(self, event):
        self.umframgr = int(event.GetString())
        	
    def _verdbolga(self, event):
        self.verdbolga = event.GetString()
        if(self.verdbolga == "nuna"):
        	self.verdbolga = 0
        else:
        	self.verdbolga = int(self.verdbolga[9:-4])
        
    def _verdtrSparn(self, event):
        self.verdSparn = event.GetInt()

    def reikna_lan(self, event):
        lan_v.lan(self.lan1_upph, self.lan1_vextir, self.lan1_greidslubyrgdi, self.lan1_timabil, self.lan1_verdtrygging, self.lan1_jafnar, self.verdbolga) 
        lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga) 
        lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga) 

    def reikna_sparnad(self, event):
    	sparnadur1b.spar(self.umframgr, 12, self.verdbolga, self.verdSparn, 1)
        

app = wx.App(False)
frame = wx.Frame(None, title="Fyrsta �tg�fa")
frame.SetSize((950,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
