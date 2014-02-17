    #nýtt í mainPage:
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
      	
      	ax.plot(data_x, data_y, label="Reikningur ef lagt er fyrir")
        
        ax.set_xlabel('Timi (manudir)')
        ax.set_ylabel('Upphaed')
        ax.set_title('Reyndu nu ad spara')
        ax.legend(loc=2); # upper left corner
        
        canvas.draw()
        
        #nýtt:
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
        
app = wx.App(False)
frame = wx.Frame(None, title="Onnur utgafa")
frame.SetSize((850,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
