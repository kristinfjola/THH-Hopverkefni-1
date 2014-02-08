# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

def lan(H, v, gb, n, verdtrygging, jafnar, verdbolga):
	v = float(v)/100
	if(verdbolga == 0): 		#verðbólga núna
		vb = 0.02
	elif(verdbolga == 5): 		#verðbólga 5 ár
		vb = 0.04
	elif(verdbolga == 10): 		#verðbólga 10 ár
		vb = 0.06
	else:						#verðbólga 15 ár
		vb = 0.08
	if(jafnar == 1):
		if(verdtrygging == 0):
			overdAfborganir(H, n, v)			#afborganir, óverðtryggt
		else:
			verdAfborganir(H, n, v, vb)			#afborganir, verðtryggt
	else:
		if(verdtrygging == 0):
			overdGreidslur(H, n, v)				#greiðslur, óverðtryggt
		else:
			verdGreidslur(H, n, v, vb)			#greiðslur, verðtryggt


#verdbolga = 0	gefur verðbólguna núna => 2%
#verdbolga = 5	gefur meðaltal síðustu 5 ár => 4%
#verdbolga = 10	gefur meðaltal síðustu 10 ár => 6%
#verdbolga = 15	gefur meðaltal síðustu 15 ár => 8%

#óverðtryggt gefur		verdtrygging = 0
#verðtryggt gefur 		verdtrygging = 1
#jafnar greiðslur gefa 	jafnar = 0
#jafnar afborganir gefa jafnar = 1


# Óverðtryggt, jafnar afborganir, reiknað mánaðarlega
# Notkun: overdAfborganir(höfuðstóll, fjöldi ára, vextir(%))
def overdAfborganir(H, n, v):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir'
	nt = n*12	#fjöldi mán
	vt = float(v)/12	#vextur á mán
	if(nt == 0):
		afb = 0
	else:
		afb = float(H)/nt
	eftirs = H
	summa = 0
	stodur = [eftirs]
	for i in range(0, nt):
		if (round(eftirs) != 0):
			greidsla = afb + vt*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
	print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
	for i in range(0, len(stodur)):
		print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(abs(stodur[i]))
	print '--------------'


# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað mánaðarlega (er ennþá að vinna í þessu, ég gerði bara (vextir+verðbólga))
# Noktun: verdAfborganir(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))
def verdAfborganir(H, n, v, vb):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir og ' + str(vb*100) + '% verðbólgu'
	nt = n*12	#fjöldi mán
	vt = float(v)/12	#vextur á mán
	vbt = float(vb)/12	#verðbólga á mán
	if(n == 0):
		afb = 0
	else:
		afb = float(H)/nt
	eftirs = H
	summa = 0
	stodur = [eftirs]
	for i in range(0, nt):
		if (round(eftirs) != 0):
			greidsla = afb + (vt+vbt)*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
			stodur.append(round(eftirs))
	print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
	for i in range(0, len(stodur)):
		print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(abs(stodur[i]))
	print '--------------'


# Óverðtryggt, jafnar greiðslur, reiknað mánaðarlega
# Notkun: overdGreidslur(höfuðstóll, fjöldi ára, vextir(%))
def overdGreidslur(H, n, v):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir'
	nt = n*12	#fjöldi mán
	vt = float(v)/12	#vextur á mán
	def temp(H, n, v):
		greidsla = A
		eftirs = H
		summa = 0
		stodur = [eftirs]
		for i in range(0, n):
			if(round(eftirs) > 0):
				vextir = v*eftirs
				afb = greidsla - vextir
				eftirs = eftirs - afb
				summa = summa + greidsla
				stodur.append(round(eftirs))
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' mán er: '+ str(abs(stodur[i])) + ' kr'
		print '--------------'
	if(nt <= 0):
		A = 0
		temp(H, nt, vt)
	else:
		if(vt <= 0):
			overdAfborganir(H, nt, 0)
		else:
			A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
			temp(H, nt, vt)


# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað mánaðarlega (er í lagi ef eyjan.is	er ok)
# Notkun: verdGreidslur(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))	
def verdGreidslur(H, n, v, vb):
def bla(H, n, v, vb):
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir og ' + str(vb*100) + '% verðbólgu'
	nt = n*12	#fjöldi mán
	vt = float(v)/12	#vextur á mán
	vbt = float(vb)/12	#verðbólga á mán
	def temp(H, n, v, vb):
		eftirs = H
		greidsla = A
		summa = 0
		stodur = [eftirs]
		for i in range(0, n+1):
			if (round(eftirs) > 0):
				eftirs = eftirs + vb*eftirs
				greidsla = (1+vb)*greidsla
				afb = greidsla - v*eftirs
				eftirs = eftirs - afb
				summa = summa + greidsla
				stodur.append(eftirs)
		print 'Heildargreiðslan er: ' + str(round(summa)) + ' kr'
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' ár er: '+ str(abs(round(stodur[i])))
		print '--------------'
	if(nt <= 0):
		A = 0
		temp(H, nt, vt, vbt)
	else:
		if(vbt <= 0):
			overdGreidslur(H, nt, vt)
		elif(v <= 0): 
			verdAfborganir(H, nt, 0, vbt)
		else:
			A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))
			temp(H, nt, vt, vbt)