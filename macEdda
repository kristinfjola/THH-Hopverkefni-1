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

       #...alls konar kóði

    def reikna(self, event):
      #bara þessi lína breyttist:
    	self.nidurst = sparnadur1b.spar(self.umframgr, self.verdbolga, self.verdSparn, self.ein_man_greidsla, self.innist_bundin)
    	self.lanNidurst = lan_v.lan(self.lan1_upph, self.lan1_vextir, self.lan1_greidslubyrgdi, self.lan1_timabil, self.lan1_verdtrygging, self.lan1_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "Lan 1")
    	
    	#!!!!!!
    	#ekki copy-a eftirfarandi 3 línur :)
    	lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla)
    	lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla)
    	self.syna_svar_glugga()

   #...
   
    def fa_nidurstodur(self):
    	return self.nidurst
    
    def fa_nidurstodur_ur_lani(self):
    	return self.lanNidurst

class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Svor', size=(800,650))
        wx.Frame.CenterOnScreen(self)
        
        self.scroll = wx.ScrolledWindow(self, -1) #NÝTT
        self.scroll.SetScrollbars(1, 1, 800, 650) #NÝTT
        
        fig, ax = plt.subplots()
        
        panel_svar = wx.Panel(self.scroll) #NÝTT
        sizer = wx.BoxSizer(wx.VERTICAL)
        canvas = FigCanvas(panel_svar, -1, fig)
        
        #...
        
        nidurstodur = MainPage.fa_nidurstodur(panel)
        
        ax.set_ylim([nidurstodur[1][0], nidurstodur[1][12]])
        ax.set_xlim([0, 12])
        
        data_x = nidurstodur[0]
        data_y = nidurstodur[1]
        
        ax.plot(data_x, data_y, label="Reikningur ef lagt er fyrir")
        
        ax.set_xlabel('Timi (manudir)')
        ax.set_ylabel('Upphaed')
        ax.set_title('Reyndu nu ad spara')
        ax.legend(loc=2); # upper left corner
        
        canvas.draw()
        
        nidurstodur2 = MainPage.fa_nidurstodur_ur_lani(panel)
        
        if(size(nidurstodur2) != 0):
        	fig2, ax2 = plt.subplots()
        	canvas2 = FigCanvas(panel_svar, -1, fig2)
        	xmax = size(nidurstodur2[0])-1
        	ymin = size(nidurstodur2[1])-1
        	ax2.set_ylim([nidurstodur2[1][ymin], nidurstodur2[1][0]])
        	ax2.set_xlim([0, nidurstodur2[0][xmax]])
        
        	data_x2 = nidurstodur2[0]
        	data_y2 = nidurstodur2[1]
        
        	ax2.plot(data_x2, data_y2, label="Lan ef borgad er inna thad")
        
       	 	ax2.set_xlabel('Timi (manudir)')
        	ax2.set_ylabel('Upphaed')
        	ax2.set_title('Reyndu nu ad spara')
        	ax2.legend(loc=1); # upper right corner
        
        	canvas2.draw()

        #...
        
        lanakostnadur = wx.StaticText(panel_svar, -1, "Auka kostnadur vid lan (vextir, uppgreidslugjald): " )#+ lana_kostnadur)
        sizer.Add(lanakostnadur, 0, wx.ALL, 10)
        
        sizer.Add(canvas, 0, wx.ALL, 10) #NÝTT -> nýr staður
        if(size(nidurstodur2) != 0):
        	sizer.Add(canvas2, 0, wx.ALL, 10)
        
        # !! NÝTT !!! (út þetta fall)
        
        panel_svar.SetSizer(sizer)
        panel_svar.SetAutoLayout(True)
        panel_svar.Layout()
        panel_svar.Fit()
        
        self.Center()
        self.MakeModal( True )
        
        self.frmPanelWid, self.frmPanelHgt = panel_svar.GetSize()
        self.unit = 1
        self.scroll.SetScrollbars( self.unit, self.unit, self.frmPanelWid/self.unit, self.frmPanelHgt/self.unit )
        
app = wx.App(False)
frame = wx.Frame(None, title="Onnur utgafa")
frame.SetSize((850,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
