class Safna(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        #...
        
        self.radio = ['Eingreidsla', 'Manadarlega']
        #nýtt:
        self.radio2 = ['Overdtryggdur', 'Verdtryggdur']
        
        #...
        
        self.pros = wx.StaticText(self, label="%")
        self.grid.Add(self.pros, pos=(1,5))
        
        self.verdtr = wx.StaticText(self, label="Reikningurinn er:")
        self.grid.Add(self.verdtr, pos=(2,0))
        
        self.verdtryggdur = wx.RadioBox(self, choices=self.radio2)
        self.grid.Add(self.verdtryggdur, pos=(2,1))
        self.Bind(wx.EVT_RADIOBOX, self.verdOverd, self.verdtryggdur)
    
    #timabil
    def markmidsUpp(self, event):
    	self.markmidsUpphaed = int(event.GetString())
        
    #...
    
    def verdOverd(self, event):
    	self.verdtrOverdtr = event.GetInt()
    	
    #...
    
    def reikna_timab(self, event):
    	#breytan bætist við aftast:
        self.timabil = sparitimi.timabil(self.sparnadarUpphaed, self.vextirTimab, self.markmidsUpphaed, self.hvernigGreidsla, self.verdtrOverdtr)
        self.syna_timabil_glugga()
