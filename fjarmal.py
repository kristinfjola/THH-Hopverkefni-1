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


        # fyrirs�gn
        self.fyrirsogn = wx.StaticText(self, label="Hva� skal gera vi� peningana?")
        self.fyrirsognFont = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.fyrirsogn.SetFont(self.fyrirsognFont)
        self.mainSizer.Add(self.fyrirsogn, flag=wx.ALL|wx.EXPAND, border=10)

        self.mainSizer.Add(self.grid2, 0, wx.ALL, 5)
        self.mainSizer.Add(self.grid, 0, wx.ALL, 5)

        # labels � l�n
        self.stadaLana = wx.StaticText(self, label="Sta�a l�ns")    
        self.grid.Add(self.stadaLana, pos=(0,0))

        self.vextir = wx.StaticText(self, label="Vextir")
        self.grid.Add(self.vextir, pos=(0,2))

        self.timabilLana = wx.StaticText(self, label="T�mabil")
        self.grid.Add(self.timabilLana, pos=(0,4))

        self.verdtryggtLan = wx.StaticText(self, label="�ver�tryggt/Ver�tryggt")
        self.grid.Add(self.verdtryggtLan, pos=(0,6))
	
        self.greidslutypa = wx.StaticText(self, label="Jafnar grei�slur/jafnar afborganir")
        self.grid.Add(self.greidslutypa, pos=(0,7))

        # labels � sparna�
        self.umframgreidsla = wx.StaticText(self, label="Umframgrei�sla")
        self.grid2.Add(self.umframgreidsla, pos=(0,0))
		
        self.greidsla = wx.StaticText(self, label="Eingrei�sla/m�na�arlega")
        self.grid2.Add(self.greidsla, pos=(1,0), flag=wx.TOP, border=17)

        self.verdb = wx.StaticText(self, label="T�mabil ver�b�lgu:")
        self.grid2.Add(self.verdb, pos=(2,0), flag=wx.TOP, border=17)
        
        self.umframgreidsla = wx.StaticText(self, label="Hvernig sparna�arreikning?")
        self.grid2.Add(self.umframgreidsla, pos=(3,0), flag=wx.TOP, border=10)
        
        self.verdtrSparn = wx.StaticText(self, label="�g vil sparna�inn:")
        self.grid2.Add(self.verdtrSparn, pos=(4,0), flag=wx.TOP, border=17)

        self.timabil = wx.StaticText(self, label="Innist��a m� vera bundin �:")
        self.grid2.Add(self.timabil, pos=(4, 2), flag=wx.TOP, border=17)
	
        self.radioListVerdtrygging = ['�ver�tryggt', 'Ver�tryggt']
        self.radioListJafnar = ['Grei�slur', 'Afborganir']
        self.radioListGreidsla = ['Eingrei�sla', 'M�na�arlega']
        self.timabil_overd = ['ekki bundin', '12 m�nu�ir', '18 m�nu�ir', '24 m�nu�ir']
        self.timabil_verd = ['36 m�nu�ir', '48 m�nu�ir', '60 m�nu�ir']
        self.verdbolga_ = ['seinustu 15 �r', 'seinustu 10 �r', 'seinustu 5 �r', 'nuna']
        self.radioList2 = ['�ver�trygg�an', 'Ver�trygg�an']

        # upphafsstilla allar breytur sem 0
        self.lan1_upph = self.lan2_upph = self.lan3_upph = self.lan1_vextir = self.lan2_vextir = self.lan3_vextir = self.lan1_greidslubyrgdi = self.lan2_greidslubyrgdi = self.lan3_greidslubyrgdi = self.lan1_timabil = self.lan2_timabil = self.lan3_timabil =  self.lan1_verdtrygging =  self.lan2_verdtrygging =  self.lan3_verdtrygging = self.lan1_jafnar = self.lan2_jafnar = self.lan3_jafnar = self.umframgr = 0      
        self.verdbolga = 15
        self.verdSparn = self.ein_man_greidsla = self.innist_bundin = 0
        
        # l�na input
        for i in range(1, 4):
            # innsl�ttur fyrir l�n - self.lani
            lan = 'lan' + str(i)
            setattr(self, lan, wx.TextCtrl(self, size = (80,20)))  
            self.grid.Add(object.__getattribute__(self, lan), pos=(i,0), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.upphaed_lana, object.__getattribute__(self, lan))
            
            # kr. merki fyrir l�nsupph�� - self.kronai1
            krona1 = 'krona' + str(i) + '1'
            setattr(self, krona1, wx.StaticText(self, label='kr.'))
            self.grid.Add(object.__getattribute__(self, krona1), pos=(i,1), flag=wx.TOP, border=17)
            
            # innsl�ttur fyrir vexti - self.vextiri
            vextir = 'vextir' + str(i)
            setattr(self, vextir, wx.TextCtrl(self, size = (50,20)))
            self.grid.Add(object.__getattribute__(self, vextir), pos=(i,2), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.vextir_lana, object.__getattribute__(self, vextir))

            # pr�sentumerki - self.prosentai
            prosenta = 'prosenta' + str(i)
            setattr(self, prosenta, wx.StaticText(self, label='%'))
            self.grid.Add(object.__getattribute__(self, prosenta), pos=(i,3), flag=wx.TOP, border=17)

            # t�mabil l�ns - self.timabilLansi
            timabilLans = 'timabilLans' + str(i)
            setattr(self, timabilLans, wx.TextCtrl(self, size = (50,20)))
            self.grid.Add(object.__getattribute__(self, timabilLans), pos=(i,4), flag=wx.TOP, border=17)
            self.Bind(wx.EVT_TEXT, self.timabil_lana, object.__getattribute__(self, timabilLans))

           # ar - self.ari
            ar = 'ar' + str(i)
            setattr(self, ar, wx.StaticText(self, label='�r'))
            self.grid.Add(object.__getattribute__(self, ar), pos=(i,5), flag=wx.TOP, border=17)
			
            # radio buttons fyrir ver�tryggingu - self.verdtryggingi
            verdtrygging = 'verdtrygging' + str(i)
            setattr(self, verdtrygging, wx.RadioBox(self, choices=self.radioListVerdtrygging))
            self.grid.Add(object.__getattribute__(self, verdtrygging), pos=(i,6), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.verdtrygging_lana, object.__getattribute__(self, verdtrygging))

            # radio buttons fyrir jafnar grei�slur/jafnar afborganir
            jafnar = 'jafnar' + str(i)
            setattr(self, jafnar, wx.RadioBox(self, choices=self.radioListJafnar))
            self.grid.Add(object.__getattribute__(self, jafnar), pos=(i,7), flag=wx.FIXED_MINSIZE | wx.ALIGN_TOP)
            self.Bind(wx.EVT_RADIOBOX, self.jafnar_lana, object.__getattribute__(self, jafnar))

        # sparna�ar input
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

    	lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, 'lan2')
    	lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, 'lan3')
    	self.syna_svar_glugga()

    def syna_svar_glugga(self):
        self.svar_gluggi = SvarGluggi(parent=None, id=-1)
        self.svar_gluggi.Show()

    # get f�ll
    def fa_innist_bundin(self):
        return self.innist_bundin
    
    def fa_nidurstodur(self):
        return self.nidurstodur

    def fa_nidurstodur_ur_lani(self):
    	return self.lanNidurst

class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Sv�r', size=(800,650))
        wx.Frame.CenterOnScreen(self)

        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(1, 1, 800, 650)
        
        fig, ax = plt.subplots()

        panel_svar = wx.Panel(self.scroll)
        sizer = wx.BoxSizer(wx.VERTICAL)
        canvas = FigCanvas(panel_svar, -1, fig)

        innistaeda_bundin = MainPage.fa_innist_bundin(tabOne)
        
        besti_kostur = str(sparnadur1b.hvad_er_best_ad_gera(innistaeda_bundin))

        bestAdGera = wx.StaticText(panel_svar, -1, "�a� v�ri best fyrir �ig a� " + besti_kostur )
        bestAdGera_font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        bestAdGera.SetFont(bestAdGera_font)
        sizer.Add(bestAdGera, 0, wx.ALL, 10)

        
        ## --------------   gr�f byrja        ------------##

        nidurstodur = MainPage.fa_nidurstodur(tabOne)
    
        ax.set_ylim([nidurstodur[1][0]-(nidurstodur[1][0]*0.02), nidurstodur[1][12]])
        ax.set_xlim([0, 12])
        
        data_x = nidurstodur[0]
        data_y = nidurstodur[1]
        
        ax.plot(data_x, data_y, label="Reikningur ef lagt er fyrir")
        
        ax.set_xlabel(u'T�mi [m�nu�ir]')
        ax.set_ylabel(u'Upph�� [kr]')
        ax.set_title(u'Reyndu nu a� spara!')
        ax.legend(loc=2); # upper left corner
        
        canvas.draw()
        
        nidurstodur2 = MainPage.fa_nidurstodur_ur_lani(tabOne)

        if(size(nidurstodur2) != 0):
        	fig2, ax2 = plt.subplots()
        	canvas2 = FigCanvas(panel_svar, -1, fig2)
        	xmax = size(nidurstodur2[0][0])-1
        	ymin = size(nidurstodur2[0][1])-1
        	ax2.set_ylim([nidurstodur2[0][1][ymin], nidurstodur2[0][1][0]])
        	ax2.set_xlim([0, nidurstodur2[0][0][xmax]])
        
        	data_x2 = nidurstodur2[0][0]
        	data_y2 = nidurstodur2[0][1]
        	data_xobr = nidurstodur2[1][0]
        	data_yobr = nidurstodur2[1][1]
        
        	ax2.plot(data_x2, data_y2, label="Lan ef borgad er inna thad")
        	ax2.plot(data_xobr, data_yobr, label="Obreytt lan")

        	ax2.set_xlabel('Timi (manudir)')
        	ax2.set_ylabel('Upphaed')
        	ax2.set_title('Reyndu nu ad spara')
        	ax2.legend(loc=1); # upper right corner
        
        	canvas2.draw()

        ## ------------        gr�f b�in        ------------##
        

        besta_sparnadarleid = str(sparnadur1b.fa_bestu_sparnadarleid())

        uppl_um_sparnadarleid = str(sparnadur1b.fa_uppl_um_sparnadarleid())

        sparnadarleid = wx.StaticText(panel_svar, -1, "Besta sparna�arlei�in fyrir �ig er " + besta_sparnadarleid)
        sizer.Add(sparnadarleid, 0, wx.ALL, 10)

        sparnadar_box = wx.StaticBox(panel_svar, wx.ID_ANY, "Uppl�singar um sparna�arlei�")
        sparnadar_box_sizer = wx.StaticBoxSizer(sparnadar_box, wx.VERTICAL)
        sparnadar_box_sizer.SetMinSize((700, 50))
        sparnadar_uppl = wx.TextCtrl(panel_svar, value=uppl_um_sparnadarleid, size=(700,50), style=wx.TE_READONLY|wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.BORDER_NONE) 
        sparnadar_box_sizer.Add(sparnadar_uppl, 0, wx.EXPAND, 10)
        sizer.Add(sparnadar_box_sizer, 0, wx.ALL, 10)

        arsvextir = str(sparnadur1b.fa_arsvexti())

        ars_vextir = wx.StaticText(panel_svar, -1, "Vextir yfir 12 m�nu�i: " + arsvextir)
        sizer.Add(ars_vextir, 0, wx.ALL, 10)

        fjarmagnstekjuskattur = str(sparnadur1b.fa_fjarmagnstekjuskatt())

        ars_fjarmagnstekjuskattur = wx.StaticText(panel_svar, -1, "Fj�rmagnstekjuskattur yfir 12 m�nu�i: " + fjarmagnstekjuskattur)
        sizer.Add(ars_fjarmagnstekjuskattur, 0, wx.ALL, 10)

        lana_kostnadur = lan_v.fa_lanakostnad()
        lana_hagnadur = lan_v.fa_hagnad() 

        lanakostnadur = wx.StaticText(panel_svar, -1, "Auka kostna�ur vi� l�n (vextir, uppgrei�slugjald): ")
        sizer.Add(lanakostnadur, 0, wx.ALL, 10)
        lanakostnadur1 = wx.StaticText(panel_svar, -1, "L�n 1: " + str(lana_kostnadur[0]))
        sizer.Add(lanakostnadur1, 0, wx.ALL, 10)
        lanakostnadur2 = wx.StaticText(panel_svar, -1, "L�n 2: " + str(lana_kostnadur[1]))
        sizer.Add(lanakostnadur2, 0, wx.ALL, 10)
        lanakostnadur3 = wx.StaticText(panel_svar, -1, "L�n 3: " + str(lana_kostnadur[2]))
        sizer.Add(lanakostnadur3, 0, wx.ALL, 10)

        lanahagnadur = wx.StaticText(panel_svar, -1, "Hagna�ur vi� a� borga umframgrei�slu � l�n (mismunur � milli �ess a� nota umframgrei�slu � l�n e�a ekki): ")
        sizer.Add(lanahagnadur, 0, wx.ALL, 10)
        lanahagnadur1 = wx.StaticText(panel_svar, -1, "L�n 1: " + str(lana_hagnadur[0]))
        sizer.Add(lanahagnadur1, 0, wx.ALL, 10)
        lanahagnadur2 = wx.StaticText(panel_svar, -1, "L�n 2: " + str(lana_hagnadur[1]))
        sizer.Add(lanahagnadur2, 0, wx.ALL, 10)
        lanahagnadur3 = wx.StaticText(panel_svar, -1, "L�n 3: " + str(lana_hagnadur[2]))
        sizer.Add(lanahagnadur3, 0, wx.ALL, 10)

        
        # gr�f
        sizer.Add(canvas, 0, wx.ALL, 10)
        if(size(nidurstodur2) != 0):
        	sizer.Add(canvas2, 0, wx.ALL, 10)
        
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

        sizer = wx.BoxSizer(wx.VERTICAL)

        hallo = wx.StaticText(self, label="Hall� Kalli �g vil safna pening ") 
        sizer.Add(hallo, 0, wx.ALL, 10)
        

class Notebook(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        global tabOne
        tabOne = MainPage(self)
        self.AddPage(tabOne, "Hva� skal gera vi� peninginn?")

        tabTwo = Safna(self)
        self.AddPage(tabTwo, "Hvernig safna �g?")

        
class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "�ri�ja �tg�fa", size=(850,600))

        panel = wx.Panel(self)
        notebook = Notebook(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
        self.Show()

tabOne = 0
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow()
    app.MainLoop()
