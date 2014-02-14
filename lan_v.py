# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

# TODO (auka):
## hafa n*12 og v/12 í lan
## hafa if n==0 or H==0 í lan
## bæta við append ef h=0, n=0

# # Gildi: fylki með 6 stökum þar sem fyrsta stakið er kostnaður við lán1 með umfram, stak tvö er kostnaður við lán1 án umfram, osfrv..
tempfylki = [0, 0, 0, 0, 0, 0]
# Gildi: fylki sem heldur utan um nöfn lánanna 3 og raunvexti þeirra
lan_uppl = []

# Gildi: fylki með 3 stökum þar sem fyrsta stakið er kostnaðurinn fyrir lán 1, annað stakið fyrir lán 2 osfrv.
def fa_lanakostnad():
	global tempfylki
	return [tempfylki[0], tempfylki[2], tempfylki[4]]

# Gildi: fylki með 3 stökum þar sem fyrsta stakið er hagnaður við að borga umfram í lán1, osfrv
def fa_hagnad():
	global tempfylki
	return [tempfylki[1]-tempfylki[0], tempfylki[3]-tempfylki[2], tempfylki[5]-tempfylki[4]]
	
	
#Gildi: fylki með tveimur stökum, nafn lánsins með hæstu raunvexti og raunvexturinn sjálfur
def raunvLan():
	global lan_uppl
	max = ['', 0]
	for i in range(0, len(lan_uppl)):
		if(lan_uppl[i][1] > max[1]):
			max[0] = lan_uppl[i][0]
			max[1] = lan_uppl[i][1]
	return max

# Notkun: lan(höfuðstóll, vextir(%), greiðslubyrgði(óþarfi), lengd láns(ár), ó/verðtryggt, jafnar afborganir/greiðslur, verðbólga(0,5,10,15), umframgreiðsla, umfram borguð 1x/mánaðarlega, nafn lánsins)
# Gildi: FYLKI sem skilar tveimur Fylkjum, fyrra Fylkið er ef þú borgar umframgreiðslu og seinna er fyrir umfram=0, í hverju Fylki eru tvö önnur fylki, fyrra fylkið hefur númer mánaðar (0 - n*12) og það seinna hefur stöðu lánsins á þeim tíma
# dæmi: [ [[0,1,2,3],[1000, 600, 200, 0]] , [0,1,2,3,4,5],[1000, 800, 600, 400, 200, 0] ]
def lan(H, v, gb, n, verdtrygging, jafnar, verdbolga, umfram, einman, nafnLan):
	global lan_uppl
	
	#setja inn rétta verðbólgu
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
	
	#setja inn nafn lána og raunvexti
	if(verdtrygging == 0):
		lan_uppl.append([nafnLan, v/100.0])
	else:
		lan_uppl.append([nafnLan, (v+vb)/100.0])
	
	#athuga hvaða fall á að kalla á
	if(einman == 0): #umframgreiðslan er eingreiðsla
		if(jafnar == 1): #jafnar afborganir
			if(verdtrygging == 0): #óverðtryggt
				return [overdAfborganirEin(H, n, v, umfram, nafnLan, 0), overdAfborganirEin(H, n, v, 0, nafnLan, 1)]
			else: #verðtryggt
				return [verdAfborganirEin(H, n, v, vb, umfram, nafnLan, 0), verdAfborganirEin(H, n, v, vb, 0, nafnLan, 1)]
		else: #jafnar greiðslur
			if(verdtrygging == 0): #óverðtryggt
				return [overdGreidslurEin(H, n, v, umfram, nafnLan, 0), overdGreidslurEin(H, n, v, 0, nafnLan, 1)]
			else: #verðtryggt
				return [verdGreidslurEin(H, n, v, vb, umfram, nafnLan, 0), verdGreidslurEin(H, n, v, vb, 0, nafnLan, 1)]
	else: #umframgreiðslan er mánaðarlega
		if(jafnar == 1): #jafnar afborganir
			if(verdtrygging == 0): #óverðtryggt
				return [overdAfborganirMan(H, n, v, umfram, nafnLan, 0), overdAfborganirMan(H, n, v, 0, nafnLan, 1)]
			else: #verðtryggt
				return [verdAfborganirMan(H, n, v, vb, umfram, nafnLan, 0), verdAfborganirMan(H, n, v, vb, 0, nafnLan, 1)]
		else: #jafnar greiðslur
			if(verdtrygging == 0): #óverðtryggt
				return [overdGreidslurMan(H, n, v, umfram, nafnLan, 0), overdGreidslurMan(H, n, v, 0, nafnLan, 1)]
			else: #verðtryggt
				return [verdGreidslurMan(H, n, v, vb, umfram, nafnLan, 0), verdGreidslurMan(H, n, v, vb, 0, nafnLan, 1)]

# Óverðtryggt, jafnar afborganir, umframgreiðsla borguð 1x
# Notkun: overdAfborganirEin(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla, auka (0 er með umfram og 1 er óbreytt lán))
def overdAfborganirEin(H, n, v, umfram, nafn, auka):
	global tempfylki
	def temp(H, n, v, umfram):
		v = float(v)/100
		nt = n*12
		vt = float(v)/12
		afb = float(H)/nt
		eftirs = H
		summa = 0
		stodur = [eftirs]
		
		#Fyrsti mánuðurinn:
		greidsla = afb + vt*eftirs + umfram
		eftirs = eftirs - afb - 0.99*umfram
		summa = summa + greidsla
		stodur.append(round(eftirs))
		
		while(round(eftirs) >= afb):
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil
		
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]

	else:
		if(H > 0.99*umfram+H/(n*12)):
			return temp(H, n, v, umfram)
		else:
			return temp(H, n, v, 0)

# Verðtryggt, jafnar afborganir, umframgreiðsla borguð 1x
# Noktun: verdAfborganirEin(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umframgreiðsla, auka (0 er með umfram og 1 er óbreytt lán))
def verdAfborganirEin(H, n, v, vb, umfram, nafn, auka):
	global tempfylki
	def temp(H, n, v, vb, umfram):
		import math
		v = float(v)/100
		vb = float(vb)/100
		nt = n*12
		vt = float(v)/12
		vbt = float(vb)/12
		afb = float(H)/nt
		eftirs = H
		summa = 0
		stodur = [eftirs]
		
		#Fyrsti mánuðurinn:
		greidsla = afb + (vt+vbt)*eftirs + umfram
		eftirs = eftirs - afb - 0.99*umfram
		summa = summa + greidsla
		stodur.append(round(eftirs))
		
		while(round(eftirs) >= afb):
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil
		
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]

	else:
		if(H > 0.99*umfram+H/(n*12)):
			return temp(H, n, v, vb, umfram)
		else:
			return temp(H, n, v, vb, 0)


# Óverðtryggt, jafnar greiðslur, umframgreiðsla borguð 1x
# Notkun: overdGreidslurEin(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla, auka (0 er með umfram og 1 er óbreytt lán))
def overdGreidslurEin(H, n, v, umfram, nafn, auka):
	global tempfylki
	v = float(v)/100
	nt = n*12
	vt = float(v)/12
	
	def temp(H, n, v, umfram):
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
		
		while(round(eftirs) >= greidsla - vextir):
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil
		
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]

	elif(vt == 0):
		return overdAfborganirEin(H, nt, 0, umfram, nafn, auka)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if(H > A-v*H+0.99*umfram):
			return temp(H, nt, vt, umfram)
		else:
			return temp(H, nt, vt, 0)


# Verðtryggt, jafnar greiðslur, umframgreiðsla borguð 1x
# Notkun: verdGreidslurEin(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umfram, auka (0 er með umfram og 1 er óbreytt lán))	
def verdGreidslurEin(H, n, v, vb, umfram, nafn, auka):
	global tempfylki
	import math
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
	
		#Fyrsti mánuðurinn:
		eftirs = eftirs + vb*eftirs
		greidsla = (1+vb)*greidsla
		afb = greidsla - v*eftirs + 0.99*umfram
		eftirs = eftirs - afb
		summa = summa + greidsla + umfram
		stodur.append(round(eftirs))
		
		while(round(eftirs) >= greidsla - v*eftirs):
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil
		
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]
	
	elif(vbt == 0):
		return overdGreidslurEin(H, nt, vt, umfram, nafn, auka)
	elif(v == 0):
		return verdAfborganirEin(H, nt, 0, vbt, umfram, nafn, auka)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if((1+vb)*H > (1+vb)*A-v*H+0.99*umfram):
			return temp(H, nt, vt, vbt, umfram)
		else:
			return temp(H, nt, vt, vbt, 0)


# Óverðtryggt, jafnar afborganir, umframgreiðsla borguð mánaðarlega
# Notkun: overdAfborganirMan(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla, auka (0 er með umfram og 1 er óbreytt lán))
def overdAfborganirMan(H, n, v, umfram, nafn, auka):
	global tempfylki
	v = float(v)/100
	nt = n*12
	vt = float(v)/12
	
	if(nt == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]

	
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil


# Verðtryggt, jafnar afborganir, umframgreiðsla borguð mánaðarlega
# Noktun: verdAfborganirMan(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umframgreiðsla, auka (0 er með umfram og 1 er óbreytt lán))
def verdAfborganirMan(H, n, v, vb, umfram, nafn, auka):
	global tempfylki
	import math
	v = float(v)/100
	vb = float(vb)/100
	nt = n*12
	vt = float(v)/12
	vbt = float(vb)/12
	
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]

	
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil


# Óverðtryggt, jafnar greiðslur, umframgreiðsla borguð mánaðarlega
# Notkun: overdGreidslurMan(höfuðstóll, fjöldi ára, vextir(%), umframgreiðsla, auka (0 er með umfram og 1 er óbreytt lán))
def overdGreidslurMan(H, n, v, umfram, nafn, auka):
	global tempfylki
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil
		
	#áður en við förum í temp þarf að ath hvort n=0 eða v=0 svo við séum ekki að deila með 0 og fá keyrsluvillu
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]
	
	elif(v == 0):
			return overdAfborganirMan(H, n, 0, umfram, nafn, auka)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if(H > A-v*H+0.99*umfram):
			return temp(H, nt, vt, umfram)
		else:
			return temp(H, nt, vt, 0)


# Verðtryggt, jafnar greiðslur, umframgreiðsla borguð mánaðarlega
# Notkun: verdGreidslurMan(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%), umfram, auka (0 er með umfram og 1 er óbreytt lán))	
def verdGreidslurMan(H, n, v, vb, umfram, nafn, auka):
	global tempfylki
	import math
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
		while(round((1+vb)*eftirs) >= (1+vb)*greidsla-v*eftirs+0.99*umfram): 	
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
		
		if(nafn == 'lan1'):
			if(auka == 0):
				tempfylki[0] = round(summa - H)
			else:
				tempfylki[1] = round(summa - H)
		elif(nafn == 'lan2'):
			if(auka == 0):
				tempfylki[2] = round(summa - H)
			else:
				tempfylki[3] = round(summa - H)
		elif(nafn == 'lan3'):
			if(auka == 0):
				tempfylki[4] = round(summa - H)
			else:
				tempfylki[5] = round(summa - H)
		
		x = []
		skil = []
		for i in range(0, len(stodur)):
			x.append(i)
		skil.append(x)
		skil.append(stodur)
		return skil
		
	#áður en við förum í temp þarf að ath hvort n=0 eða v=0 svo við séum ekki að deila með 0 og fá keyrsluvillu
	if(n == 0) or (H == 0):
		if(nafn == 'lan1'):
			tempfylki[0] = 0.0
			tempfylki[1] = 0.0
		elif(nafn == 'lan2'):
			tempfylki[2] = 0.0
			tempfylki[3] = 0.0
		elif(nafn == 'lan3'):
			tempfylki[4] = 0.0
			tempfylki[5] = 0.0
		return [[],[]]
	
	elif(vb == 0):
		return overdGreidslurMan(H, n, v, umfram, nafn, auka)
	elif(v == 0): 
		return verdAfborganirMan(H, n, 0, vb, umfram, nafn, auka)
	else:
		A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
		if((1+vb)*H > (1+vb)*A-v*H+0.99*umfram):
			return temp(H, nt, vt, vbt, umfram)
		else:
			return temp(H, nt, vt, vbt, 0)