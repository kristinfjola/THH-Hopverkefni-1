# -*- coding: cp1252 -*-
import wx
import sparnadur1b
import lan_v
from pylab import *
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
	FigureCanvasWxAgg as FigCanvas, \
	NavigationToolbar2WxAgg as NavigationToolbar

class MainPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # sizers
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.GridBagSizer(hgap=5, vgap=5)
        self.grid2 = wx.GridBagSizer(hgap=5, vgap=5)
        self.hSizer = wx.BoxSizer(wx.HORIZONTAL)


        # fyrirsögn
        self.fyrirsogn = wx.StaticText(self, label="Hvað skal gera við peningana?")
        self.fyrirsognFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.fyrirsogn.SetFont(self.fyrirsognFont)
        self.mainSizer.Add(self.fyrirsogn, flag=wx.ALL|wx.EXPAND, border=10)

        self.mainSizer.Add(self.grid2, 0, wx.ALL, 5)
        self.mainSizer.Add(self.grid, 0, wx.ALL, 5)

        # labels á lán
        self.stadaLana = wx.StaticText(self, label="Staða láns")    
        self.grid.Add(self.stadaLana, pos=(0,0))

        self.vextir = wx.StaticText(self, label="Vextir")
        self.grid.Add(self.vextir, pos=(0,2))

        self.timabilLana = wx.StaticText(self, label="Tímabil")
        self.grid.Add(self.timabilLana, pos=(0,4))

        self.verdtryggtLan = wx.StaticText(self, label="Óverðtryggt/Verðtryggt")
        self.grid.Add(self.verdtryggtLan, pos=(0,6))
	
        self.greidslutypa = wx.StaticText(self, label="Jafnar greiðslur/jafnar afborganir")
        self.grid.Add(self.greidslutypa, pos=(0,7))

        # labels á sparnað
        self.umframgreidsla = wx.StaticText(self, label="Umframgreiðsla")
        self.grid2.Add(self.umframgreidsla, pos=(0,0))
		
        self.greidsla = wx.StaticText(self, label="Eingreiðsla/mánaðarlega")
        self.grid2.Add(self.greidsla, pos=(1,0), flag=wx.TOP, border=17)

        self.verdb = wx.StaticText(self, label="Tímabil verðbólgu:")
        self.grid2.Add(self.verdb, pos=(2,0), flag=wx.TOP, border=17)
        
        self.umframgreidsla = wx.StaticText(self, label="Hvernig sparnaðarreikning?")
        self.grid2.Add(self.umframgreidsla, pos=(3,0), flag=wx.TOP, border=10)
        
        self.verdtrSparn = wx.StaticText(self, label="Ég vil sparnaðinn:")
        self.grid2.Add(self.verdtrSparn, pos=(4,0), flag=wx.TOP, border=17)

        self.timabil = wx.StaticText(self, label="Innistæða má vera bundin í:")
        self.grid2.Add(self.timabil, pos=(4, 2), flag=wx.TOP, border=17)
	
        self.radioListVerdtrygging = ['Óverðtryggt', 'Verðtryggt']
        self.radioListJafnar = ['Greiðslur', 'Afborganir']
        self.radioListGreidsla = ['Eingreiðsla', 'Mánaðarlega']
        self.timabil_overd = ['ekki bundin', '12 mánuðir', '18 mánuðir', '24 mánuðir']
        self.timabil_verd = ['36 mánuðir', '48 mánuðir', '60 mánuðir']
        self.verdbolga_ = ['seinustu 15 ár', 'seinustu 10 ár', 'seinustu 5 ár', 'nuna']
        self.radioList2 = ['Óverðtryggðan', 'Verðtryggðan']

        # upphafsstilla allar breytur sem 0
        self.lan1_upph = self.lan2_upph = self.lan3_upph = self.lan1_vextir = self.lan2_vextir = self.lan3_vextir = self.lan1_greidslubyrgdi = self.lan2_greidslubyrgdi = self.lan3_greidslubyrgdi = self.lan1_timabil = self.lan2_timabil = self.lan3_timabil =  self.lan1_verdtrygging =  self.lan2_verdtrygging =  self.lan3_verdtrygging = self.lan1_jafnar = self.lan2_jafnar = self.lan3_jafnar = self.umframgr = 0      
        self.verdbolga = 15
        self.verdSparn = self.ein_man_greidsla = self.innist_bundin = 0
        
        # lána input
        for i in range(1, 4):
            # innsláttur fyrir lán - self.lani
            lan = 'lan' + str(i)
            setattr(self, lan, wx.TextCtrl(self, size = (80,20)))  
            self.grid.Add(object.__getattribute__(self, lan), pos=(i,0), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.upphaed_lana, object.__getattribute__(self, lan))
            
            # kr. merki fyrir lánsupphæð - self.kronai1
            krona1 = 'krona' + str(i) + '1'
            setattr(self, krona1, wx.StaticText(self, label='kr.'))
            self.grid.Add(object.__getattribute__(self, krona1), pos=(i,1), flag=wx.TOP, border=17)
            
            # innsláttur fyrir vexti - self.vextiri
            vextir = 'vextir' + str(i)
            setattr(self, vextir, wx.TextCtrl(self, size = (50,20)))
            self.grid.Add(object.__getattribute__(self, vextir), pos=(i,2), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.vextir_lana, object.__getattribute__(self, vextir))

            # prósentumerki - self.prosentai
            prosenta = 'prosenta' + str(i)
            setattr(self, prosenta, wx.StaticText(self, label='%'))
            self.grid.Add(object.__getattribute__(self, prosenta), pos=(i,3), flag=wx.TOP, border=17)

            # tímabil láns - self.timabilLansi
            timabilLans = 'timabilLans' + str(i)
            setattr(self, timabilLans, wx.TextCtrl(self, size = (50,20)))
            self.grid.Add(object.__getattribute__(self, timabilLans), pos=(i,4), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.timabil_lana, object.__getattribute__(self, timabilLans))

           # ar - self.ari
            ar = 'ar' + str(i)
            setattr(self, ar, wx.StaticText(self, label='ár'))
            self.grid.Add(object.__getattribute__(self, ar), pos=(i,5), flag=wx.TOP, border=17)
			
            # radio buttons fyrir verðtryggingu - self.verdtryggingi
            verdtrygging = 'verdtrygging' + str(i)
            setattr(self, verdtrygging, wx.RadioBox(self, choices=self.radioListVerdtrygging))
            self.grid.Add(object.__getattribute__(self, verdtrygging), pos=(i,6), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.verdtrygging_lana, object.__getattribute__(self, verdtrygging))

            # radio buttons fyrir jafnar greiðslur/jafnar afborganir
            jafnar = 'jafnar' + str(i)
            setattr(self, jafnar, wx.RadioBox(self, choices=self.radioListJafnar))
            self.grid.Add(object.__getattribute__(self, jafnar), pos=(i,7), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.jafnar_lana, object.__getattribute__(self, jafnar))

        # sparnaðar input
        self.umframgr_ = wx.TextCtrl(self, size = (270,20))
        self.grid2.Add(self.umframgr_, pos=(0,1))
        self.Bind(wx.EVT_TEXT, self._umframgreidsla, self.umframgr_)

        self.einradgreidsla = wx.RadioBox(self, choices=self.radioListGreidsla)
        self.grid2.Add(self.einradgreidsla, pos=(1,1))
        self.Bind(wx.EVT_RADIOBOX, self.hvernig_greidsla, self.einradgreidsla)

        self.verdb = wx.ComboBox(self, value=self.verdbolga_[0], choices=self.verdbolga_, style=wx.CB_READONLY)
        self.grid2.Add(self.verdb, pos=(2,1), flag=wx.TOP, border=17)
        self.Bind(wx.EVT_COMBOBOX, self._verdbolga, self.verdb)

        self.verdSparn_ = wx.RadioBox(self, choices=self.radioList2)
        self.grid2.Add(self.verdSparn_, pos=(4,1))
        self.Bind(wx.EVT_RADIOBOX, self._verdtrSparn, self.verdSparn_)
                
        self.timab = wx.ComboBox(self, value=self.timabil_overd[0], choices=self.timabil_overd, style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self._timabil, self.timab)      
        self.timab_sizer = wx.BoxSizer(wx.VERTICAL)
        self.grid2.Add(self.timab_sizer, pos=(4, 3), flag=wx.TOP, border=10)
        self.timab_sizer.Add(self.timab, 0, wx.ALL, 5)
        
        # reikna allt
        self.reikna_allt = wx.Button(self, label="Reikna")
        self.Bind(wx.EVT_BUTTON, self.reikna, self.reikna_allt)
        self.mainSizer.Add(self.reikna_allt, 0, wx.ALL, 5)
        
        
        self.SetSizerAndFit(self.mainSizer)
        
    
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
        self.innist_bundin = event.GetString()[:2]
        if(self.innist_bundin == "1"):
        	self.innist_bundin = "12"
        if(self.innist_bundin == "ek"):
        	self.innist_bundin = 0
        self.innist_bundin = int(self.innist_bundin)
        
    def _umframgreidsla(self, event):
        self.umframgr = int(event.GetString())
        	
    def _verdbolga(self, event):
        self.verdbolga = event.GetString()
        if(self.verdbolga == "nuna"):
        	self.verdbolga = 0
        else:
        	self.verdbolga = int(self.verdbolga[9:-2])
        
    def _verdtrSparn(self, event):
        self.verdSparn = event.GetInt()
        self.breyta_timabil()

    def breyta_timabil(self):
        if (self.verdSparn == 0):
            self.timab2 = wx.ComboBox(self, value=self.timabil_overd[0], choices=self.timabil_overd, style=wx.CB_READONLY)
            self.Bind(wx.EVT_COMBOBOX, self._timabil, self.timab2)
            self.innist_bundin = 0
        else:
            self.timab2 = wx.ComboBox(self, value=self.timabil_verd[0], choices=self.timabil_verd, style=wx.CB_READONLY)
            self.Bind(wx.EVT_COMBOBOX, self._timabil, self.timab2)
            self.innist_bundin = 36

        self.timab_sizer.Replace(self.timab, self.timab2, False)
        self.timab.Destroy()
        self.timab_sizer.Layout()
        self.timab = self.timab2
        
        
    def hvernig_greidsla(self, event):
        self.ein_man_greidsla = event.GetInt()

    def reikna(self, event):
    	self.nidurstodur = sparnadur1b.spar(self.umframgr, self.verdbolga, self.verdSparn, self.ein_man_greidsla, self.innist_bundin)
    	lan_v.lan(self.lan1_upph, self.lan1_vextir, self.lan1_greidslubyrgdi, self.lan1_timabil, self.lan1_verdtrygging, self.lan1_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, 'lan1')
    	lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, 'lan2')
    	lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, 'lan3')
    	self.syna_svar_glugga()

    def syna_svar_glugga(self):
        self.svar_gluggi = SvarGluggi(parent=None, id=-1)
        self.svar_gluggi.Show()

    # get föll
    def fa_innist_bundin(self):
        return self.innist_bundin
    
    def fa_nidurstodur(self):
        return self.nidurstodur

class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Svör', size=(800,650))
        wx.Frame.CenterOnScreen(self)

        fig, ax = plt.subplots()

        panel_svar = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        canvas = FigCanvas(panel_svar, -1, fig)

        innistaeda_bundin = MainPage.fa_innist_bundin(panel)
        
        besti_kostur = str(sparnadur1b.hvad_er_best_ad_gera(innistaeda_bundin))

        bestAdGera = wx.StaticText(panel_svar, -1, "Það væri best fyrir þig að " + besti_kostur )
        bestAdGera_font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        bestAdGera.SetFont(bestAdGera_font)
        sizer.Add(bestAdGera, 0, wx.ALL, 10)


        ## --------------   gröf byrja        ------------##

        nidurstodur = MainPage.fa_nidurstodur(panel)
    
        ax.set_ylim([nidurstodur[1][0], nidurstodur[1][12]])
        ax.set_xlim([0, 12])
        
        data_x = nidurstodur[0]
        data_y = nidurstodur[1]
        
        ax.plot(data_x, data_y, label="Reikningur ef lagt er fyrir")
        
        ax.set_xlabel(u'Tími [mánuðir]')
        ax.set_ylabel(u'Upphæð [kr]')
        ax.set_title(u'Reyndu nu að spara!')
        ax.legend(loc=2); # upper left corner
        
        canvas.draw()
        sizer.Add(canvas, 1, wx.GROW)

        ## ------------        gröf búin        ------------##
        

        besta_sparnadarleid = str(sparnadur1b.fa_bestu_sparnadarleid())

        uppl_um_sparnadarleid = str(sparnadur1b.fa_uppl_um_sparnadarleid())

        sparnadarleid = wx.StaticText(panel_svar, -1, "Besta sparnaðarleiðin fyrir þig er " + besta_sparnadarleid)
        sizer.Add(sparnadarleid, 0, wx.ALL, 10)

        sparnadar_box = wx.StaticBox(panel_svar, wx.ID_ANY, "Upplýsingar um sparnaðarleið")
        sparnadar_box_sizer = wx.StaticBoxSizer(sparnadar_box, wx.VERTICAL)
        sparnadar_box_sizer.SetMinSize((700, 50))
        sparnadar_uppl = wx.TextCtrl(panel_svar, value=uppl_um_sparnadarleid, size=(700,50), style=wx.TE_READONLY|wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.BORDER_NONE) 
        sparnadar_box_sizer.Add(sparnadar_uppl, 0, wx.EXPAND, 10)
        sizer.Add(sparnadar_box_sizer, 0, wx.ALL, 10)

        arsvextir = str(sparnadur1b.fa_arsvexti())

        ars_vextir = wx.StaticText(panel_svar, -1, "Vextir yfir 12 mánuði: " + arsvextir)
        sizer.Add(ars_vextir, 0, wx.ALL, 10)

        fjarmagnstekjuskattur = str(sparnadur1b.fa_fjarmagnstekjuskatt())

        ars_fjarmagnstekjuskattur = wx.StaticText(panel_svar, -1, "Fjármagnstekjuskattur yfir 12 mánuði: " + fjarmagnstekjuskattur)
        sizer.Add(ars_fjarmagnstekjuskattur, 0, wx.ALL, 10)

        lana_kostnadur = str(lan_v.fa_lanakostnad())

        lanakostnadur = wx.StaticText(panel_svar, -1, "Auka kostnaður við lán (vextir, uppgreiðslugjald): " + lana_kostnadur)
        sizer.Add(lanakostnadur, 0, wx.ALL, 10)
        
        panel_svar.SetSizerAndFit(sizer)
        panel_svar.Layout()


        
app = wx.App(False)
frame = wx.Frame(None, title="Önnur útgáfa")
frame.SetSize((850,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
