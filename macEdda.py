class Safna(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        #...
    
        #upphafsstilla breytur
        self.markmidsUpphaed = self.sparnadarUpphaed = self.hvernigGreidsla = 0
        self.vextirTimab = self.verdtrOverdtr = 0
        self.markmidsUpphaed2 = self.bundidTimabil = self.hvernigGreidsla2 = 0
        self.vextirUpph = 0
    
    #timabil
    def markmidsUpp(self, event):
    	self.markmidsUpphaed = int(event.GetString())
        
    #...
