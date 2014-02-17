class SvarGluggi(wx.Frame):

    def __init__(self,parent,id):
      	
      	# ...
      	
      	#nýtt:
        ax.set_ylim([nidurstodur[1][0]-(nidurstodur[1][0]*0.02), nidurstodur[1][12]])
        #...
        
        if(size(nidurstodur2) != 0):
        	#...
        	
        	data_x2 = nidurstodur2[0][0]
        	data_y2 = nidurstodur2[0][1]
        	#nýtt:
        	data_xobr = nidurstodur2[1][0]
        	data_yobr = nidurstodur2[1][1] 
        
        	ax2.plot(data_x2, data_y2, label="Lan ef borgad er inna thad")
        	ax2.plot(data_xobr, data_yobr, label="Obreytt lan")
        
       	 	

        #...
        
app = wx.App(False)
frame = wx.Frame(None, title="Onnur utgafa")
frame.SetSize((850,500))
panel = MainPage(frame)
frame.Show()
app.MainLoop()
