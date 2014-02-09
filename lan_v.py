# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

def lan(H, v, gb, n, verdtrygging, jafnar, verdbolga):
	if(verdbolga == 0): 		#verðbólga núna
		vb = 3.1
	elif(verdbolga == 5): 		#verðbólga 5 ár
		vb = 6.07868852459016
	elif(verdbolga == 10): 		#verðbólga 10 ár
		vb = 6.19421487603305
	else:						#verðbólga 15 ár
		vb = 5.60276243093922
	
	umfram = 10000	#hef umframgreiðslu 10.000 kr þangað til búið er að bæta því við í fjarmal.py
	if(jafnar == 1):
		if(verdtrygging == 0):
			overdAfborganir(H, n, v, umfram)			#afborganir, óverðtryggt
		else:
			verdAfborganir(H, n, v, vb, umfram)			#afborganir, verðtryggt
	else:
		if(verdtrygging == 0):
			overdGreidslur(H, n, v, umfram)				#greiðslur, óverðtryggt
		else:
			verdGreidslur(H, n, v, vb, umfram)			#greiðslur, verðtryggt
	#v = float(v)/100
	#vb = float(vb)/100
	
	
#verdbolga = 0	gefur verðbólguna núna => 3.1%
#verdbolga = 5	gefur meðaltal síðustu 5 ár => 6.08%
#verdbolga = 10	gefur meðaltal síðustu 10 ár => 6.19%
#verdbolga = 15	gefur meðaltal síðustu 15 ár => 5.60%

#óverðtryggt gefur		verdtrygging = 0
#verðtryggt gefur 		verdtrygging = 1
#jafnar greiðslur gefa 	jafnar = 0
#jafnar afborganir gefa jafnar = 1


# Óverðtryggt, jafnar afborganir, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%)
# Notkun: overdAfborganir(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla)
def overdAfborganir(H, n, v, umfram):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir og ' + str(umfram) + ' kr í umframgreiðslu mánaðarlega'
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
	#keyrum þetta á meðan summa afborgunar og umframgreiðslu er minni en eftirstaðan (svo eftirstaðan fer ekki í mínustölu)
	while(round(eftirs) >= afb+0.99*umfram):
		greidsla = afb + vt*eftirs + umfram
		eftirs = eftirs - afb - 0.99*umfram		#0.99 útaf 1% fer í uppgreiðslukosntaður
		summa = summa + greidsla
		stodur.append(round(eftirs))
	#síðasti mánuðurinn: ef afborgnunin er meiri en eftirstaðan verður engin umframgreiðsla
	if(afb >= eftirs):
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


# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%)
# Noktun: verdAfborganir(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umframgreiðsla)
def verdAfborganir(H, n, v, vb, umfram):
	import math
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v) + '% vextir, ' + str(math.ceil(vb*100)/100) + '% verðbólgu og '  + str(umfram) + ' kr í umframgreiðslu mánaðarlega'
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
	#keyrum þetta á meðan summa afborgunar og umframgreiðslu er minni en eftirstaðan (svo eftirstaðan fer ekki í mínustölu)
	while(round(eftirs) >= afb+0.99*umfram):
		greidsla = afb + (vt+vbt)*eftirs + umfram
		eftirs = eftirs - afb - 0.99*umfram		#0.99 útaf 1% fer í uppgreiðslukosntaður
		summa = summa + greidsla
		stodur.append(round(eftirs))
	#síðasti mánuðurinn: ef afborgnunin er meiri en eftirstaðan verður engin umframgreiðsla
	if(afb >= eftirs):
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


# Óverðtryggt, jafnar greiðslur, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%)
# Notkun: overdGreidslur(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla)
def overdGreidslur(H, n, v, umfram):
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
		while(round(eftirs) >= greidsla-v*eftirs+0.99*umfram):
			afb = greidsla - v*eftirs + 0.99*umfram		#þar sem v*eftirs = vextir #0.99 útaf 1% fer í uppgreiðslukosntaður
			eftirs = eftirs - afb
			summa = summa + greidsla + umfram
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgnunin = greidsla-v*eftirs er meiri en eftirstaðan verður engin umframgreiðsla
		if(greidsla-v*eftirs >= eftirs):
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
	#áður en við förum í temp þarf að ath hvort n=0 eða v=0 svo við séum ekki að deila með 0 og fá keyrsluvillu
	if(nt <= 0):
		A = 0
		temp(H, nt, vt, umfram)
	else:
		if(vt <= 0):
			overdAfborganir(H, nt, 0, umfram)
		else:
			A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
			temp(H, nt, vt, umfram)


# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað mánaðarlega, með möguleika á umframgreiðslur (uppgreiðslugjald er 1%)
# Notkun: verdGreidslur(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umfram)	
def verdGreidslur(H, n, v, vb, umfram):
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
		while(round((1+vb)*eftirs) >= greidsla-v*eftirs+0.99*umfram): 	
			eftirs = (1+vb)*eftirs
			greidsla = (1+vb)*greidsla
			afb = greidsla - v*eftirs + 0.99*umfram		#þar sem v*eftirs = vextir #0.99 útaf 1% fer í uppgreiðslukosntaður
			eftirs = eftirs - afb
			summa = summa + greidsla + umfram
			stodur.append(round(eftirs))
		#síðasti mánuðurinn: ef afborgnunin = greidsla-v*eftirs er meiri en eftirstaðan (með verðbólgu) verður engin umframgreiðsla
		if(greidsla-v*eftirs >= (1+vb)*eftirs):
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
	#áður en við förum í temp þarf að ath hvort n=0 eða v=0 svo við séum ekki að deila með 0 og fá keyrsluvillu
	if(nt <= 0):
		A = 0
		temp(H, nt, vt, vbt, umfram)
	else:
		if(vbt <= 0):
			overdGreidslur(H, nt, vt, umfram)
		elif(v <= 0): 
			verdAfborganir(H, nt, 0, vbt, umfram)
		else:
			A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
			temp(H, nt, vt, vbt, umfram)