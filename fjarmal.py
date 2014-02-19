# -*- coding: cp1252 -*-
import wx
import sparnadur1b
import lan_v
import sparitimi
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

        self.kronz = wx.StaticText(self, label="kr.")
        self.grid2.Add(self.kronz, pos=(0,2))
		
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
    	self.lanNidurst = lan_v.lan(self.lan1_upph, self.lan1_vextir, self.lan1_greidslubyrgdi, self.lan1_timabil, self.lan1_verdtrygging, self.lan1_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "lan1")
    	self.lanNidurst2 = lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "lan2")
    	self.lanNidurst3 = lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "lan3")
    	self.syna_svar_glugga()

    def syna_svar_glugga(self):
        self.svar_gluggi = SvarGluggi(parent=None, id=-1)
        self.svar_gluggi.Show()

    # get föll
    def fa_innist_bundin(self):
        return self.innist_bundin
    
    def fa_nidurstodur(self):
        return self.nidurstodur

    def fa_nidurstodur_ur_lani(self):
    	return self.lanNidurst
    
    def fa_nidurstodur_ur_lani2(self):
    	return self.lanNidurst2
    	
    def fa_nidurstodur_ur_lani3(self):
    	return self.lanNidurst3

class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Svör', size=(800,650))
        wx.Frame.CenterOnScreen(self)

        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(1, 1, 800, 650)
        
        fig, ax = plt.subplots()

        panel_svar = wx.Panel(self.scroll)
        sizer = wx.BoxSizer(wx.VERTICAL)
        canvas = FigCanvas(panel_svar, -1, fig)

        innistaeda_bundin = MainPage.fa_innist_bundin(tabOne)
        
        besti_kostur = str(sparnadur1b.hvad_er_best_ad_gera(innistaeda_bundin))

        bestAdGera = wx.StaticText(panel_svar, -1, "Það væri best fyrir þig að " + besti_kostur )
        bestAdGera_font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        bestAdGera.SetFont(bestAdGera_font)
        sizer.Add(bestAdGera, 0, wx.ALL, 10)

        
        ## --------------   gröf byrja        ------------##

        nidurstodur = MainPage.fa_nidurstodur(tabOne)
    
        ax.set_ylim([nidurstodur[1][0]-(nidurstodur[1][0]*0.02), nidurstodur[1][12]])
        ax.set_xlim([0, 12])
        
        data_x = nidurstodur[0]
        data_y = nidurstodur[1]
        
        ax.plot(data_x, data_y, label="Reikningur ef lagt er fyrir")
        
        ax.set_xlabel(u'Tími [mánuðir]')
        ax.set_ylabel(u'Upphæð [kr]')
        ax.set_title(u'Reyndu nú að spara!')
        ax.legend(loc=2); # upper left corner
        
        canvas.draw()
        
        def teiknaCanvas(nr, nidurst):
        	if(size(nidurst) != 0):
        		fig, ax = plt.subplots()
        		if(nr == 2):
        			self.canvas2 = FigCanvas(panel_svar, -1, fig)
        		if(nr == 3):
        			self.canvas3 = FigCanvas(panel_svar,1 -1, fig)
        		if(nr == 4):
        			self.canvas4 = FigCanvas(panel_svar,1 -1, fig)
        		xmax = size(nidurst[0][0])-1
        		ymin = size(nidurst[0][1])-1
        		ax.set_ylim([nidurst[0][1][ymin], nidurst[0][1][0]])
        		ax.set_xlim([0, nidurst[0][0][xmax]])
        		
        		data_x2 = nidurst[0][0]
        		data_y2 = nidurst[0][1]
        		data_xobr = nidurst[1][0]
        		data_yobr = nidurst[1][1]
        		
        		ax.plot(data_x2, data_y2, label="Lan ef borgad er inna thad")
        		ax.plot(data_xobr, data_yobr, label="Obreytt lan")
        		ax.set_xlabel('Timi (manudir)')
        		ax.set_ylabel('Upphaed')
        		if(nr == 2):
        			ax.set_title('Lan 1')
        		if(nr == 3):
        			ax.set_title('Lan 2')
        		if(nr == 4):
        			ax.set_title('Lan 3')
        		ax.legend(loc=1); # upper right corner
        
        		if(nr == 2):
        			self.canvas2.draw()
        		if(nr == 3):
        			self.canvas3.draw()
        		if(nr == 4):
        			self.canvas4.draw()
        	
        
        nidurstodur2 = MainPage.fa_nidurstodur_ur_lani(tabOne)
        teiknaCanvas(2, nidurstodur2)
        
        nidurstodur3 = MainPage.fa_nidurstodur_ur_lani2(tabOne)
        teiknaCanvas(3, nidurstodur3)
        	
        nidurstodur4 = MainPage.fa_nidurstodur_ur_lani3(tabOne)
        teiknaCanvas(4, nidurstodur4)

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

        lana_kostnadur = lan_v.fa_lanakostnad()
        lana_hagnadur = lan_v.fa_hagnad() 

        lanakostnadur = wx.StaticText(panel_svar, -1, "Auka kostnaður við lán (vextir, uppgreiðslugjald): ")
        sizer.Add(lanakostnadur, 0, wx.ALL, 10)
        lanakostnadur1 = wx.StaticText(panel_svar, -1, "Lán 1: " + str(lana_kostnadur[0]))
        sizer.Add(lanakostnadur1, 0, wx.ALL, 10)
        lanakostnadur2 = wx.StaticText(panel_svar, -1, "Lán 2: " + str(lana_kostnadur[1]))
        sizer.Add(lanakostnadur2, 0, wx.ALL, 10)
        lanakostnadur3 = wx.StaticText(panel_svar, -1, "Lán 3: " + str(lana_kostnadur[2]))
        sizer.Add(lanakostnadur3, 0, wx.ALL, 10)

        lanahagnadur = wx.StaticText(panel_svar, -1, "Hagnaður við að borga umframgreiðslu á lán (mismunur á milli þess að nota umframgreiðslu í lán eða ekki): ")
        sizer.Add(lanahagnadur, 0, wx.ALL, 10)
        lanahagnadur1 = wx.StaticText(panel_svar, -1, "Lán 1: " + str(lana_hagnadur[0]))
        sizer.Add(lanahagnadur1, 0, wx.ALL, 10)
        lanahagnadur2 = wx.StaticText(panel_svar, -1, "Lán 2: " + str(lana_hagnadur[1]))
        sizer.Add(lanahagnadur2, 0, wx.ALL, 10)
        lanahagnadur3 = wx.StaticText(panel_svar, -1, "Lán 3: " + str(lana_hagnadur[2]))
        sizer.Add(lanahagnadur3, 0, wx.ALL, 10)

        
        # gröf
        sizer.Add(canvas, 0, wx.ALL, 10)
        if(size(nidurstodur2) != 0):
        	sizer.Add(self.canvas2, 0, wx.ALL, 10)
        if(size(nidurstodur3) != 0):
        	sizer.Add(self.canvas3, 0, wx.ALL, 10)
        if(size(nidurstodur4) != 0):
        	sizer.Add(self.canvas4, 0, wx.ALL, 10)
        
        panel_svar.SetSizer(sizer)
        panel_svar.SetAutoLayout(True)
        panel_svar.Layout()
        panel_svar.Fit()
        
        self.Center()
        self.MakeModal( True )
        
        self.frmPanelWid, self.frmPanelHgt = panel_svar.GetSize()
        self.unit = 1
        self.scroll.SetScrollbars( self.unit, self.unit, self.frmPanelWid/self.unit, self.frmPanelHgt/self.unit )


class Safna(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.GridBagSizer(hgap=5, vgap=5)
        
        self.hversu_lengi = wx.StaticText(self, label="Hvað er ég lengi að safna þessari upphæð?") 
        self.hversu_lengi_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.hversu_lengi.SetFont(self.hversu_lengi_font)
        self.sizer.Add(self.hversu_lengi, 0, wx.ALL, 10)
        
        self.sizer.Add(self.grid, 0, wx.ALL, 10)
        
        #timabil
        self.markmidsUpph = wx.StaticText(self, label="Markmiðsupphæð")    
        self.grid.Add(self.markmidsUpph, pos=(0,0))
        
        self.markmUpph = wx.TextCtrl(self, size = (245,20))
        self.grid.Add(self.markmUpph, pos=(0,1))
        self.Bind(wx.EVT_TEXT, self.markmidsUpp, self.markmUpph)
        
        self.kronur = wx.StaticText(self, label="kr.")
        self.grid.Add(self.kronur, pos=(0,2))

        self.grUpph = wx.StaticText(self, label="Umframgreiðsla")
        self.grid.Add(self.grUpph, pos=(0,3))
        
        self.spUpph = wx.TextCtrl(self, size = (150,20))
        self.grid.Add(self.spUpph, pos=(0,4))
        self.Bind(wx.EVT_TEXT, self.sparnUpph, self.spUpph)
        
        self.kronur2 = wx.StaticText(self, label="kr.")
        self.grid.Add(self.kronur2, pos=(0,5))
        
        self.hvernigGr = wx.StaticText(self, label="Eingreiðsla/mánaðarleg")
        self.grid.Add(self.hvernigGr, pos=(1,0), flag=wx.TOP, border=17)
        
        self.radio = ['Eingreiðsla', 'Mánaðarlega']
        self.radio2 = ['Óverðtryggður', 'Verðtryggður']
        
        self.greidsla = wx.RadioBox(self, choices=self.radio)
        self.grid.Add(self.greidsla, pos=(1,1))
        self.Bind(wx.EVT_RADIOBOX, self.hvernig_greidsla, self.greidsla)

        self.spVextir = wx.StaticText(self, label="Vextir")
        self.grid.Add(self.spVextir, pos=(1,3))
        
        self.vextirTimabil = wx.TextCtrl(self, size = (150,20))
        self.grid.Add(self.vextirTimabil, pos=(1,4))
        self.Bind(wx.EVT_TEXT, self.vextirT, self.vextirTimabil)
        
        self.pros = wx.StaticText(self, label="%")
        self.grid.Add(self.pros, pos=(1,5))

        self.verdtr = wx.StaticText(self, label="Reikningurinn er:")
        self.grid.Add(self.verdtr, pos=(2,0), flag=wx.TOP, border=17)
        
        self.verdtryggdur = wx.RadioBox(self, choices=self.radio2)
        self.grid.Add(self.verdtryggdur, pos=(2,1))
        self.Bind(wx.EVT_RADIOBOX, self.verdOverd, self.verdtryggdur)        
        
        self.reikna_timabil = wx.Button(self, label="Reikna tímabil")
        self.Bind(wx.EVT_BUTTON, self.reikna_timab, self.reikna_timabil)
        self.sizer.Add(self.reikna_timabil, 0, wx.ALL, 10)

        #upphaed
        self.hversu_mikid = wx.StaticText(self, label="Hvað þarf ég að leggja mikið fyrir til að ná þessari upphæð eftir þetta langan tíma?") 
        self.hversu_mikid_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.hversu_mikid.SetFont(self.hversu_mikid_font)
        self.sizer.Add(self.hversu_mikid, 0, wx.ALL, 10)
        
        self.grid2 = wx.GridBagSizer(hgap=5, vgap=5)
        self.sizer.Add(self.grid2, 0, wx.ALL, 10)
        
        self.markmidsUpph2 = wx.StaticText(self, label="Markmiðsupphæð")    
        self.grid2.Add(self.markmidsUpph2, pos=(0,0))
        
        self.markmUpph2 = wx.TextCtrl(self, size = (245,20))
        self.grid2.Add(self.markmUpph2, pos=(0,1))
        self.Bind(wx.EVT_TEXT, self.markmidsUpp2, self.markmUpph2)
        
        self.kronur3 = wx.StaticText(self, label="kr.")
        self.grid2.Add(self.kronur3, pos=(0,2))

        self.timabilLabel = wx.StaticText(self, label="Tímabil")
        self.grid2.Add(self.timabilLabel, pos=(0,3))
        
        self.timab = wx.TextCtrl(self, size = (120,20))
        self.grid2.Add(self.timab, pos=(0,4))
        self.Bind(wx.EVT_TEXT, self.timabilBundid, self.timab)
        
        self.ar = wx.StaticText(self, label="ár")
        self.grid2.Add(self.ar, pos=(0,5))
        
        self.hvernigGr2 = wx.StaticText(self, label="Eingreiðsla/mánaðarleg")
        self.grid2.Add(self.hvernigGr2, pos=(1,0), flag=wx.TOP, border=17)
        
        self.greidsla2 = wx.RadioBox(self, choices=self.radio)
        self.grid2.Add(self.greidsla2, pos=(1,1))
        self.Bind(wx.EVT_RADIOBOX, self.hvernig_greidsla2, self.greidsla2)

        self.spVextir2 = wx.StaticText(self, label="Vextir")
        self.grid2.Add(self.spVextir2, pos=(1,3))
        
        self.vextir = wx.TextCtrl(self, size = (120,20))
        self.grid2.Add(self.vextir, pos=(1,4))
        self.Bind(wx.EVT_TEXT, self.vextirU, self.vextir)
        
        self.pros2 = wx.StaticText(self, label="%")
        self.grid2.Add(self.pros2, pos=(1,5))
		
        self.reikna_upphaed = wx.Button(self, label="Reikna upphæð")
        self.Bind(wx.EVT_BUTTON, self.reikna_upph, self.reikna_upphaed)
        self.sizer.Add(self.reikna_upphaed, 0, wx.ALL, 10)

        image = 'piggy-bank.jpg'
        jpg1 = wx.Image(image, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, jpg1, (10 + jpg1.GetWidth()*1.1, 340), (jpg1.GetWidth()*0.8, jpg1.GetHeight()*0.7))

        self.SetSizerAndFit(self.sizer)

        #upphafsstilla breytur
        self.markmidsUpphaed = self.sparnadarUpphaed = self.hvernigGreidsla = 0
        self.vextirTimab = self.verdtrOverdtr = 0
        self.markmidsUpphaed2 = self.bundidTimabil = self.hvernigGreidsla2 = 0
        self.vextirUpph = 0
    
    #timabil
    def markmidsUpp(self, event):
    	self.markmidsUpphaed = int(event.GetString())
        
    def sparnUpph(self, event):
    	self.sparnadarUpphaed = int(event.GetString())
    	
    def hvernig_greidsla(self, event):
    	self.hvernigGreidsla = event.GetInt()
    	
    def vextirT(self, event):
    	self.vextirTimab = int(event.GetString())

    def verdOverd(self, event):
    	self.verdtrOverdtr = event.GetInt()
    	
    #upphaed
    def markmidsUpp2(self, event):
    	self.markmidsUpphaed2 = int(event.GetString())
        
    def timabilBundid(self, event):
    	self.bundidTimabil = int(event.GetString())
    	
    def hvernig_greidsla2(self, event):
    	self.hvernigGreidsla2 = event.GetInt()
    	
    def vextirU(self, event):
    	self.vextirUpph = int(event.GetString())
    
    def reikna_timab(self, event):
        self.timabil = sparitimi.timabil(self.sparnadarUpphaed, self.vextirTimab, self.markmidsUpphaed, self.hvernigGreidsla, self.verdtrOverdtr)
        self.syna_timabil_glugga()

    def syna_timabil_glugga(self):
        self.timabil_gluggi = TimabilGluggi(parent=None, id=-1)
        self.timabil_gluggi.Show()

    def reikna_upph(self, event):
        self.upphaed = sparitimi.innlogn(self.markmidsUpphaed2, self.vextirUpph, self.bundidTimabil, self.hvernigGreidsla2)
        self.syna_upphaed_glugga()

    def syna_upphaed_glugga(self):
        self.upphaed_gluggi = UpphaedGluggi(parent=None, id=-1)
        self.upphaed_gluggi.Show()

    # get föll
    def fa_timabil(self):
        return self.timabil

    def fa_upphaed(self):
        return self.upphaed

class TimabilGluggi(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Svör', size=(400,200))
        wx.Frame.CenterOnScreen(self)

        self.SetBackgroundColour('#c297b8')

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.timabil = Safna.fa_timabil(tabTwo)

        self.hvada_timabil = wx.StaticText(self, label=self.timabil) 
        self.sizer.Add(self.hvada_timabil, 0, wx.ALL, 10)

class UpphaedGluggi(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Svör', size=(400,200))
        wx.Frame.CenterOnScreen(self)
        
        self.SetBackgroundColour('#93b3c2')

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.upphaed = Safna.fa_upphaed(tabTwo)

        self.hvada_upphaed = wx.StaticText(self, label=self.upphaed) 
        self.sizer.Add(self.hvada_upphaed, 0, wx.ALL, 10)
        
class Notebook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        global tabOne
        tabOne = MainPage(self)
        self.AddPage(tabOne, "Hvað skal gera við peninginn?")

        global tabTwo
        tabTwo = Safna(self)
        self.AddPage(tabTwo, "Hvernig safna ég?")

        
class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Reiknivél", size=(850,600))
        wx.Frame.CenterOnScreen(self)

        panel = wx.Panel(self)
        notebook = Notebook(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
        self.Show()

# set global variables
tabOne = tabTwo = 0

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow()
    app.MainLoop()
