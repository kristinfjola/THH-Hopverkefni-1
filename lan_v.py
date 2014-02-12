# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

def lan(H, v, gb, n, verdtrygging, jafnar, verdbolga, umfram, einman):
	if(verdbolga == 0): 		#verðbólga núna
		vb = 3.1
	elif(verdbolga == 5): 		#verðbólga 5 ár
		vb = 6.07868852459016
	elif(verdbolga == 10): 		#verðbólga 10 ár
		vb = 6.19421487603305
	elif(verdbolga == 15):		#verðbólga 15 ár
		vb = 5.60276243093922
	else:
		vb = 0.0
		
	# Óverðtryggt - breytist ekki með verðbólgu
	# Raunvextir = nafnvextir - verðbólga
	if verdtrygging == 0:
		# Ef vextir láns eru lægri en verðbólga mun verðbólgan éta vextina.
		# Þá vextir = verðbólga. Þannig eru 0 prósent vextir.
		if v<vb:
			v = vb
		else:
			v = v-vb
		print 'Raunvextir óverðtryggðs láns á tímabilinu eru ' + str(v)
	
	if(einman == 0):	#umframgreiðslan er eingreiðsla
		if(jafnar == 1):
			if(verdtrygging == 0):
				overdAfborganirEin(H, n, v, umfram)			#afborganir, óverðtryggt
			else:
				verdAfborganirEin(H, n, v, vb, umfram)		#afborganir, verðtryggt
		else:
			if(verdtrygging == 0):
				overdGreidslurEin(H, n, v, umfram)			#greiðslur, óverðtryggt
			else:
				verdGreidslurEin(H, n, v, vb, umfram)		#greiðslur, verðtryggt
	else:				#umframgreiðslan er mánaðarlega
		if(jafnar == 1):	#jafnar afborganir
			if(verdtrygging == 0):
				overdAfborganirMan(H, n, v, umfram)			#afborganir, óverðtryggt
			else:
				verdAfborganirMan(H, n, v, vb, umfram)		#afborganir, verðtryggt
		else:		#jafnar greiðslur
			if(verdtrygging == 0):
				overdGreidslurMan(H, n, v, umfram)			#greiðslur, óverðtryggt
			else:
				verdGreidslurMan(H, n, v, vb, umfram)		#greiðslur, verðtryggt
				
# Notkun: 	bestu_lanavextir():
# Fyrir: 	Notandi hefur slegið inn upplýsingar um lánin sín og þær 
# 		upplýsingar eru að finna í <fylki>
# Eftir:	bestu_lanavextir er hæstu vextir lńa sem notandi er með.
#def bestu_lanavextir():
"""	Hvar geymir Jóhanna töfraupplýsingar um lánin?? :D
	Væri gott að vera með svipað upplýsingaform og fyrir sparnaðinn... (gogn.py)
"""


# Óverðtryggt, jafnar afborganir, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), me� einni umframgrei�slu
# Notkun: overdAfborganirEin(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla)
def overdAfborganirEin(H, n, v, umfram):
	def TEMP(H, n, v, umfram):
		print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir og ' + str(umfram) + ' kr umframgreiðslu fyrsta mánuðinn'
		v = float(v)/100
		nt = n*12
		vt = float(v)/12
		if(nt == 0):
			afb = 0
		else:
			afb = float(H)/nt
		eftirs = H
		summa = 0
		stodur = [eftirs]
		#Fyrsti mánuðurinn:
		greidsla = afb + vt*eftirs + umfram
		eftirs = eftirs - afb - 0.99*umfram
		summa = summa + greidsla
		stodur.append(round(eftirs))
		while(round(eftirs) > afb):
			greidsla = afb + vt*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#Síðasti mánuðurinn:
		afb = eftirs
		greidsla = afb + vt*eftirs
		eftirs = eftirs - afb
		summa = summa + greidsla
		stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i])
		print '--------------'
		#return stodur
	if(n == 0):
		print 'Enginn tími' #return []
	else:
		if(H > 0.99*umfram+H/(n*12)):
			TEMP(H, n, v, umfram)
		else:
			TEMP(H, n, v, 0)

# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með einni umframgreiðslu
# Noktun: verdAfborganirEin(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umframgreiðsla)
def verdAfborganirEin(H, n, v, vb, umfram):
	def TEMP(H, n, v, vb, umfram):
		import math
		print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir, ' + str(math.ceil(vb*100)/100) + '% verðbólgu og '  + str(umfram) + ' kr umframgreiðslu fyrsta mánuðinn'
		v = float(v)/100
		vb = float(vb)/100
		nt = n*12
		vt = float(v)/12
		vbt = float(vb)/12
		if(n == 0):
			afb = 0
		else:
			afb = float(H)/nt
		eftirs = H
		summa = 0
		stodur = [eftirs]
		#Fyrsti mánuðurinn:
		greidsla = afb + (vt+vbt)*eftirs + umfram
		eftirs = eftirs - afb - 0.99*umfram
		summa = summa + greidsla
		stodur.append(round(eftirs))
		while(round(eftirs) > afb):
			greidsla = afb + (vt+vbt)*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#Síðasti mánuðurinn:
		afb = eftirs
		greidsla = afb + (vt+vbt)*eftirs
		eftirs = eftirs - afb
		summa = summa + greidsla
		stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i])
		print '--------------'
		#return stodur
	if(n == 0):
		print 'enginn tími'	#return []
	else:
		if(H > 0.99*umfram+H/(n*12)):
			TEMP(H, n, v, vb, umfram)
		else:
			TEMP(H, n, v, vb, 0)


# Óverðtryggt, jafnar greiðslur, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með einni umframgreiðslu
# Notkun: overdGreidslurEin(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla)
def overdGreidslurEin(H, n, v, umfram):
	v = float(v)/100
	nt = n*12
	vt = float(v)/12
	def temp(H, n, v, umfram):
		print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n/12) + ' ár með ' + str(v*12*100) + '% vextir og ' + str(umfram) + ' kr umframgreiðslu fyrsta mánuðinn'	
		greidsla = A
		eftirs = H
		summa = 0
		stodur = [eftirs]
		#Fyrsti mánuðurinn:
		vextir = v*eftirs
		afb = greidsla - vextir + 0.99*umfram
		eftirs = eftirs - afb
		summa = summa + greidsla + umfram
		stodur.append(round(eftirs))
		while(round(eftirs) > greidsla - vextir):
			vextir = v*eftirs
			afb = greidsla - vextir
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#Síðasti mánuðurinn:
		afb = eftirs
		greidsla = afb + v*eftirs
		eftirs = eftirs - afb
		summa = summa + greidsla
		stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i]) + ' kr'
		print '--------------'
		#return stodur
	if(n == 0):
		print 'enginn tími' #return []
	elif(vt == 0):
		overdAfborganirEin(H, nt, 0, umfram)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if(H > A-v*H+0.99*umfram):
			temp(H, nt, vt, umfram)
		else:
			temp(H, nt, vt, 0)


# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með einni umframgreiðslu
# Notkun: verdGreidslurEin(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umfram)	
def verdGreidslurEin(H, n, v, vb, umfram):
	import math
	v = float(v)/100
	vb = float(vb)/100
	nt = n*12
	vt = float(v)/12
	vbt = float(vb)/12
	def temp(H, n, v, vb, umfram):
		print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n/12) + ' ár með ' + str(v*100*12) + '% vextir, ' + str((math.ceil(vb*12*100*100)/100)) + '% verðbólgu og ' + str(umfram) + ' kr umframgreiðslu fyrsta mánuðinn'
		eftirs = H
		greidsla = A
		summa = 0
		stodur = [eftirs]
		#Fyrsti mánuðurinn:
		eftirs = eftirs + vb*eftirs
		greidsla = (1+vb)*greidsla
		afb = greidsla - v*eftirs + 0.99*umfram
		eftirs = eftirs - afb
		summa = summa + greidsla + umfram
		stodur.append(round(eftirs))
		while(round(eftirs) > greidsla - v*eftirs):
			eftirs = eftirs + vb*eftirs
			greidsla = (1+vb)*greidsla
			afb = greidsla - v*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#Síðasti mánuðurinn:
		afb = eftirs
		greidsla = afb + v*eftirs
		eftirs = eftirs - afb
		summa = summa + greidsla
		stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(round(stodur[i]))
		print '--------------'			
	if(n == 0):
		print 'enginn tími' #return []
	elif(vbt == 0):
		overdGreidslurEin(H, nt, vt, umfram)
	elif(v == 0):
		verdAfborganirEin(H, nt, 0, vbt, umfram)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if((1+vb)*H > (1+vb)*A-v*H+0.99*umfram):
			temp(H, nt, vt, vbt, umfram)
		else:
			temp(H, nt, vt, vbt, 0)


# Óverðtryggt, jafnar afborganir, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með mánaðarlegri umframgreiðslu
# Notkun: overdAfborganirMan(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla)
def overdAfborganirMan(H, n, v, umfram):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir og ' + str(umfram) + ' kr í umframgreiðslu mánaðarlega'
	v = float(v)/100
	nt = n*12
	vt = float(v)/12
	if(nt == 0):
		print 'enginn tími' #return []
	else:
		afb = float(H)/nt
		eftirs = H
		summa = 0
		stodur = [eftirs]
		#keyrum þetta á meðan summa afborgunar og umframgreiðslu er minni en eftirstaðan (svo eftirstaðan fer ekki í mínustölu)
		while(round(eftirs) > afb+0.99*umfram):
			greidsla = afb + vt*eftirs + umfram
			eftirs = eftirs - afb - 0.99*umfram		#0.99 útaf 1% fer í uppgreiðslukosntaður
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgnunin er meiri en eftirstaðan verður engin umframgreiðsla
		if(afb > eftirs):
			afb = eftirs
			greidsla = afb + vt*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgunin er minni, þá þurfum við fyrst að reikna hver umframgreiðslan þarf að vera
		else:
			umfram = (eftirs - afb)/0.99
			greidsla = afb + vt*eftirs + umfram
			eftirs = eftirs - afb - 0.99*umfram		# == eftirs - afb - (eftirs - afb) = 0
			summa = summa + greidsla
			stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i])
		print '--------------'
		#return stodur


# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með mánaðarlegri umframgreiðslu
# Noktun: verdAfborganirMan(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umframgreiðsla)
def verdAfborganirMan(H, n, v, vb, umfram):
	import math
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir, ' + str(math.ceil(vb*100)/100) + '% verðbólgu og '  + str(umfram) + ' kr í umframgreiðslu mánaðarlega'
	v = float(v)/100
	vb = float(vb)/100
	nt = n*12
	vt = float(v)/12
	vbt = float(vb)/12
	if(n == 0):
		print 'enginn tími' #return []
	else:
		afb = float(H)/nt
		eftirs = H
		summa = 0
		stodur = [eftirs]
		#keyrum þetta á meðan summa afborgunar og umframgreiðslu er minni en eftirstaðan (svo eftirstaðan fer ekki í mínustölu)
		while(round(eftirs) > afb+0.99*umfram):
			greidsla = afb + (vt+vbt)*eftirs + umfram
			eftirs = eftirs - afb - 0.99*umfram		#0.99 útaf 1% fer í uppgreiðslukosntaður
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgnunin er meiri en eftirstaðan verður engin umframgreiðsla
		if(afb > eftirs):
			afb = eftirs
			greidsla = afb + (vt+vbt)*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgunin er minni, þá þurfum við fyrst að reikna hver umframgreiðslan þarf að vera
		else:
			umfram = (eftirs - afb)/0.99
			greidsla = afb + (vt+vbt)*eftirs + umfram
			eftirs = eftirs - afb - 0.99*umfram
			summa = summa + greidsla
			stodur.append(round(eftirs))	
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i])
		print '--------------'
		#return stodur


# Óverðtryggt, jafnar greiðslur, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með mánaðarlegri umframgreiðslu
# Notkun: overdGreidslurMan(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla)
def overdGreidslurMan(H, n, v, umfram):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir og ' + str(umfram) + ' kr í umframgreiðslu mánaðarlega'
	v = float(v)/100
	nt = n*12
	vt = float(v)/12
	def temp(H, n, v, umfram):
		greidsla = A
		eftirs = H
		summa = 0
		stodur = [eftirs]
		#keyrum þetta á meðan afborgunin = greidsla-v*eftirs+0.99*umfram er minni en eftirstaðan
		while(round(eftirs) > greidsla-v*eftirs+0.99*umfram):
			afb = greidsla - v*eftirs + 0.99*umfram		#þar sem v*eftirs = vextir #0.99 útaf 1% fer í uppgreiðslukosntaður
			eftirs = eftirs - afb
			summa = summa + greidsla + umfram
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgnunin = greidsla-v*eftirs er meiri en eftirstaðan verður engin umframgreiðsla
		if(greidsla-v*eftirs > eftirs):
			afb = eftirs
			greidsla = afb + v*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgunin er minni, þá þurfum við fyrst að reikna hver umframgreiðslan þarf að vera
		else:
			umfram = (eftirs - (greidsla - v*eftirs))/0.99		#þar sem greidsla-v*eftirs er afborgunin (án umframgreiðslu)
			afb = greidsla - v*eftirs + 0.99*umfram
			eftirs = eftirs - afb
			summa = summa + greidsla + umfram
			stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i]) + ' kr'
		print '--------------'
		#return stodur
	#áður en við förum í temp þarf að ath hvort n=0 eða v=0 svo við séum ekki að deila með 0 og fá keyrsluvillu
	if(n == 0):
		print 'enginn tími' #return []
	elif(v == 0):
			overdAfborganirMan(H, n, 0, umfram)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if(H > A-v*H+0.99*umfram):
			temp(H, nt, vt, umfram)
		else:
			temp(H, nt, vt, 0)


# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%), með mánaðarlegri umframgreiðslu
# Notkun: verdGreidslurMan(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umfram)	
def verdGreidslurMan(H, n, v, vb, umfram):
	import math
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir, ' + str((math.ceil(vb*100)/100)) + '% verðbólgu og ' + str(umfram) + ' kr í umframgreiðslu mánaðarlega'
	v = float(v)/100
	vb = float(vb)/100
	nt = n*12
	vt = float(v)/12
	vbt = float(vb)/12
	def temp(H, n, v, vb, umfram):
		eftirs = H
		greidsla = A
		summa = 0
		stodur = [eftirs]
		#keyrum þetta á meðan afborgunin = greidsla-v*eftirs+0.99*umfram er minni en eftirstaðan(með viðbættri verðbólgu)
		while(round((1+vb)*eftirs) > (1+vb)*greidsla-v*eftirs+0.99*umfram): 	
			eftirs = (1+vb)*eftirs
			greidsla = (1+vb)*greidsla
			afb = greidsla - v*eftirs + 0.99*umfram		#þar sem v*eftirs = vextir #0.99 útaf 1% fer í uppgreiðslukosntaður
			eftirs = eftirs - afb
			summa = summa + greidsla + umfram
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgnunin = greidsla-v*eftirs er meiri en eftirstaðan (með verðbólgu) verður engin umframgreiðsla
		if(greidsla-v*eftirs > (1+vb)*eftirs):
			eftirs = (1+vb)*eftirs
			afb = eftirs
			greidsla = (1+vb)*(afb + v*eftirs)
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgunin er minni, þá þurfum við fyrst að reikna hver umframgreiðslan þarf að vera
		else:
			eftirs = (1+vb)*eftirs
			greidsla = (1+vb)*greidsla
			umfram = (eftirs - (greidsla - v*eftirs))/0.99		#þar sem greidsla-v*eftirs er afborgunin (án umframgreiðslu)
			afb = greidsla - v*eftirs + 0.99*umfram
			eftirs = eftirs - afb
			summa = summa + greidsla + umfram
			stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(stodur[i])
		print '--------------'
		#return stodur
	#áður en við förum í temp þarf að ath hvort n=0 eða v=0 svo við séum ekki að deila með 0 og fá keyrsluvillu
	if(n == 0):
		print 'enginn tími' #return []
	elif(vb == 0):
			overdGreidslurMan(H, n, v, umfram)
	elif(v == 0): 
		verdAfborganirMan(H, n, 0, vb, umfram)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if((1+vb)*H > (1+vb)*A-v*H+0.99*umfram):
			temp(H, nt, vt, vbt, umfram)
		else:
			temp(H, nt, vt, vbt, 0)
