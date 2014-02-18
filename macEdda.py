class MainPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #...
        
        self.umframgreidsla = wx.StaticText(self, label="Umframgreidsla a manudi")
        self.grid2.Add(self.umframgreidsla, pos=(0,0))
        #nýtt:
        self.kronz = wx.StaticText(self, label="kr.")
        self.grid2.Add(self.kronz, pos=(0,2))
    
    def reikna(self, event):
    	self.nidurst = sparnadur1b.spar(self.umframgr, self.verdbolga, self.verdSparn, self.ein_man_greidsla, self.innist_bundin)
    	self.lanNidurst = lan_v.lan(self.lan1_upph, self.lan1_vextir, self.lan1_greidslubyrgdi, self.lan1_timabil, self.lan1_verdtrygging, self.lan1_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "lan1")
    	self.lanNidurst2 = lan_v.lan(self.lan2_upph, self.lan2_vextir, self.lan2_greidslubyrgdi, self.lan2_timabil, self.lan2_verdtrygging, self.lan2_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "lan2")
    	self.lanNidurst3 = lan_v.lan(self.lan3_upph, self.lan3_vextir, self.lan3_greidslubyrgdi, self.lan3_timabil, self.lan3_verdtrygging, self.lan3_jafnar, self.verdbolga, self.umframgr, self.ein_man_greidsla, "lan3")
    	self.syna_svar_glugga()
    	
    def fa_nidurstodur(self):
    	return self.nidurst
    
    def fa_nidurstodur_ur_lani(self):
    	return self.lanNidurst
    	
    def fa_nidurstodur_ur_lani2(self):
    	return self.lanNidurst2
    	
    def fa_nidurstodur_ur_lani3(self):
    	return self.lanNidurst3


class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
      	
      	# ...
      	
      	ax.set_ylim([nidurstodur[1][0]-(nidurstodur[1][0]*0.02), nidurstodur[1][12]])
        ax.set_xlim([0, 12])
        
        data_x = nidurstodur[0]
        data_y = nidurstodur[1]
      	
      	ax.plot(data_x, data_y, label="Reikningur ef lagt er fyrir")
        
        ax.set_xlabel('Timi (manudir)')
        ax.set_ylabel('Upphaed')
        ax.set_title('Reyndu nu ad spara')
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
        	
        
        nidurstodur2 = MainPage.fa_nidurstodur_ur_lani(panel)
        teiknaCanvas(2, nidurstodur2)
        
        nidurstodur3 = MainPage.fa_nidurstodur_ur_lani2(panel)
        teiknaCanvas(3, nidurstodur3)
        	
        nidurstodur4 = MainPage.fa_nidurstodur_ur_lani3(panel)
        teiknaCanvas(4, nidurstodur4)
        #...
        
        
        lanakostnadur = wx.StaticText(panel_svar, -1, "Auka kostnadur vid lan (vextir, uppgreidslugjald): " )#+ lana_kostnadur)
        sizer.Add(lanakostnadur, 0, wx.ALL, 10)
        
        sizer.Add(canvas, 0, wx.ALL, 10)
        #nýtt:
        if(size(nidurstodur2) != 0):
        	sizer.Add(self.canvas2, 0, wx.ALL, 10)
        if(size(nidurstodur3) != 0):
        	sizer.Add(self.canvas3, 0, wx.ALL, 10)
        if(size(nidurstodur4) != 0):
        	sizer.Add(self.canvas4, 0, wx.ALL, 10)
        	
        	
class Safna(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        #...
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.GridBagSizer(hgap=5, vgap=5)
        
        self.hversu_lengi = wx.StaticText(self, label="Hvad er eg lengi ad na thessum pening?") 
        self.sizer.Add(self.hversu_lengi, 0, wx.ALL, 10)
        
        self.sizer.Add(self.grid, 0, wx.ALL, 10)
        
        #timabil
        self.markmidsUpph = wx.StaticText(self, label="Markmidsupphaed")    
        self.grid.Add(self.markmidsUpph, pos=(0,0))
        
        self.markmUpph = wx.TextCtrl(self, size = (245,20))
        self.grid.Add(self.markmUpph, pos=(0,1))
        self.Bind(wx.EVT_TEXT, self.markmidsUpp, self.markmUpph)
        
        self.kronur = wx.StaticText(self, label="kr.")
        self.grid.Add(self.kronur, pos=(0,2))

        self.grUpph = wx.StaticText(self, label="Sparnadarupphaed")
        self.grid.Add(self.grUpph, pos=(0,3))
        
        self.spUpph = wx.TextCtrl(self, size = (150,20))
        self.grid.Add(self.spUpph, pos=(0,4))
        self.Bind(wx.EVT_TEXT, self.sparnUpph, self.spUpph)
        
        self.kronur2 = wx.StaticText(self, label="kr.")
        self.grid.Add(self.kronur2, pos=(0,5))
        
        self.hvernigGr = wx.StaticText(self, label="Eingreidsla/manadarleg")
        self.grid.Add(self.hvernigGr, pos=(1,0))
        
        self.radio = ['Eingreidsla', 'Manadarlega']
        
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
        
        self.reikna_timabil = wx.Button(self, label="Reikna timabil")
        self.Bind(wx.EVT_BUTTON, self.reikna_timab, self.reikna_timabil)
        self.sizer.Add(self.reikna_timabil, 0, wx.ALL, 10)

        self.hversu_mikid = wx.StaticText(self, label="Hvad tharf eg ad leggja mikid fyrir til ad fa thennan pening eftir thetta langan tima?") 
        self.sizer.Add(self.hversu_mikid, 0, wx.ALL, 10)
        
        self.grid2 = wx.GridBagSizer(hgap=5, vgap=5)
        self.sizer.Add(self.grid2, 0, wx.ALL, 10)
        
        #upphaed
        self.markmidsUpph2 = wx.StaticText(self, label="Markmidsupphaed")    
        self.grid2.Add(self.markmidsUpph2, pos=(0,0))
        
        self.markmUpph2 = wx.TextCtrl(self, size = (245,20))
        self.grid2.Add(self.markmUpph2, pos=(0,1))
        self.Bind(wx.EVT_TEXT, self.markmidsUpp2, self.markmUpph2)
        
        self.kronur3 = wx.StaticText(self, label="kr.")
        self.grid2.Add(self.kronur3, pos=(0,2))

        self.timabilLabel = wx.StaticText(self, label="Timabil")
        self.grid2.Add(self.timabilLabel, pos=(0,3))
        
        self.timab = wx.TextCtrl(self, size = (120,20))
        self.grid2.Add(self.timab, pos=(0,4))
        self.Bind(wx.EVT_TEXT, self.timabilBundid, self.timab)
        
        self.ar = wx.StaticText(self, label="ar")
        self.grid2.Add(self.ar, pos=(0,5))
        
        self.hvernigGr2 = wx.StaticText(self, label="Eingreidsla/manadarleg")
        self.grid2.Add(self.hvernigGr2, pos=(1,0))
        
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
		
        self.reikna_upphaed = wx.Button(self, label="Reikna upphaed")
        self.Bind(wx.EVT_BUTTON, self.reikna_upph, self.reikna_upphaed)
        self.sizer.Add(self.reikna_upphaed, 0, wx.ALL, 10)

        self.SetSizerAndFit(self.sizer)
    
    #timabil
    def markmidsUpp(self, event):
    	self.markmidsUpphaed = int(event.GetString())
        
    def sparnUpph(self, event):
    	self.sparnadarUpphaed = int(event.GetString())
    	
    def hvernig_greidsla(self, event):
    	self.hvernigGreidsla = event.GetInt()
    	
    def vextirT(self, event):
    	self.vextirTimab = int(event.GetString())
    	
    #upphaed
    def markmidsUpp2(self, event):
    	self.markmidsUpphaed2 = int(event.GetString())
        
    def timabilBundid(self, event):
    	self.bundidTimabil = int(event.GetString())
    	
    def hvernig_greidsla2(self, event):
    	self.hvernigGreidsla2 = event.GetInt()
    	
    def vextirU(self, event):
    	self.vextirUpph = int(event.GetString())
    
    #breyturnar koma svo hér inn...
    def reikna_timab(self, event):
        self.timabil = sparitimi.timabil(self.sparnadarUpphaed, self.vextirTimab, self.markmidsUpphaed, self.hvernigGreidsla)
        self.syna_timabil_glugga()

    def syna_timabil_glugga(self):
        self.timabil_gluggi = TimabilGluggi(parent=None, id=-1)
        self.timabil_gluggi.Show()

    def reikna_upph(self, event):
        self.upphaed = sparitimi.innlogn(self.markmidsUpphaed2, self.vextirUpph, self.bundidTimabil, self.hvernigGreidsla2)
        self.syna_upphaed_glugga()
