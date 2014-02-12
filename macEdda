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
    	
    	#!!!!!!
    	#ekki copy-a eftirfarandi 4 línur :)
    	lan_v.lan(self.lan1_upph, self.lan1_vextir, self.lan1_greidslubyrgdi, self.lan1_timabil, self.lan1_verdtrygging, self.lan1_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla)
    	lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla)
    	lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla)
    	self.syna_svar_glugga()

   #...
   
    def fa_nidurstodur(self):
    	return self.nidurst

class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Svor', size=(800,650))
        wx.Frame.CenterOnScreen(self)
        
        fig, ax = plt.subplots()

        panel_svar = wx.Panel(self)
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
        sizer.Add(canvas, 1, wx.GROW)

        #...

        
        panel_svar.SetSizerAndFit(sizer)
        panel_svar.Layout()
        
app = wx.App(False)
frame = wx.Frame(None, title="Onnur utgafa")
frame.SetSize((850,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
