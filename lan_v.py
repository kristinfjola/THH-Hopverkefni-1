# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

def lan(H, v, gb, n, verdtrygging, jafnar, verdbolga):
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
			
		
	
#verdbolga:	
#0: verðbólgan núna => 2%
#5: meðaltal síðustu 5 ár =>4%
#10: meðaltal síðustu 10 ár => 6%
#15: meðaltal síðustu 15 ár => 8%

#verdtrygging = 0	óverðtryggt
#verdtrygging = 1	verðtryggt
#jafnar = 0			jafnar greidslur
#jafnar = 1			jafnar afborganir



# Óverðtryggt, jafnar afborganir, reiknað árlega
# Notkun: overdAfborganir(höfuðstóll, fjöldi ára, vextir(%))
def overdAfborganir(H, n, v):
	print 'Verðtryggt lán með jöfnum afborgunum:'
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir'
	print '--------------'
	afb = H/n
	stodur = []
	eftirs = H
	summa = 0
	for i in range(0, n+1):
		if (round(eftirs) == 0):
			stodur.append(eftirs)
			print 'Heildargreiðsla er: ' + str(round(summa))
		else:
			stodur.append(eftirs)
			greidsla = afb + v*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
	for i in range(0, len(stodur)):
		print 'Eftirstaðan eftir ' + str(i) + ' ár er: '+ str(round(stodur[i]))


# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað árlega (er ennþá að vinna í þessu, ég gerði bara (vextir+verðbólga))
# Noktun: verdAfborganir(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))
def verdAfborganir(H, n, v, vb):
	print 'Verðtryggt lán með jöfnum afborgunum:'
	print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir og verðbólgu ' + str(vb*100) + '%'
	print '--------------'
	afb = H/n
	stodur = []
	eftirs = H
	summa = 0
	for i in range(0, n+1):
		if (round(eftirs) == 0):
			stodur.append(eftirs)
			print 'Heildargreiðsla er: ' + str(round(summa))
		else:
			stodur.append(eftirs)
			greidsla = afb + (v+vb)*eftirs
			eftirs = eftirs - afb
			summa = summa + greidsla
	for i in range(0, len(stodur)):
		print 'Eftirstaðan eftir ' + str(i) + ' ár er: '+ str(round(stodur[i]))
		

# Óverðtryggt, jafnar greiðslur, reiknað árlega
# Notkun: overdGreidslur(höfuðstóll, fjöldi ára, vextir(%))
def overdGreidslur(H, n, v):
	def temp(H, n, v):
		print 'Óverðtryggt lán með jöfnum greiðslum:'
		print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir'
		print '--------------'
		import math
		greidsla = math.ceil(A*10)/10
		stodur = []
		eftirs = H
		summa = 0
		for i in range(0, n+1):
			if(round(eftirs) <= 0):
				stodur.append(eftirs)
				print 'Heildargreiðsla er: ' + str(round(summa))
			else:
				stodur.append(eftirs)
				vextir = v*eftirs
				afb = greidsla - vextir
				eftirs = eftirs - afb
				summa = summa + greidsla
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' ár er: '+ str(round(stodur[i]))
	if(n <= 0):
		A = 0
		temp(H, n, v)
	else:
		if(v <= 0):
			overdAfborganir(H, n, 0)
		else:
			A = H*((v*(1+v)**n)/(((1+v)**n)-1))
			temp(H, n, v)

		
# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað árlega (er í lagi ef eyjan.is	er ok)
# Notkun: verdGreidslur(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))	
def verdGreidslur(H, n, v, vb):
	def temp(H, n, v, vb):
		print 'Verðtryggt lán með jöfnum greiðslum:'
		print 'Höfuðstóll ' + str(H) + ' kr í ' + str(n) + ' ár með ' + str(v*100) + '% vextir og verðbólgu ' + str(vb*100) + '%'
		print '--------------'
		stodur = []
		eftirs = H
		greidsla = A
		summa = 0
		for i in range(0, n+1):
			if (round(eftirs) <= 0):
				stodur.append(eftirs)
				print 'Heildargreiðsla er: ' + str(round(summa))
			else:
				stodur.append(eftirs)
				eftirs = eftirs + vb*eftirs
				greidsla = (1+vb)*greidsla
				afb = greidsla - v*eftirs
				eftirs = eftirs - afb
				summa = summa + greidsla
		for i in range(0, len(stodur)):
			print 'Eftirstaðan eftir ' + str(i) + ' ár er: '+ str(round(stodur[i]))	
			
	if(n <= 0):
		A = 0
		temp(H, n, v, vb)
	else:
		if(vb <= 0):
			overdGreidslur(H, n, v)
		elif(v <= 0): 
			verdAfborganir(H, n, 0, vb)	###### ATH
		else:
			A = H*((v*(1+v)**n)/(((1+v)**n)-1))
			temp(H, n, v, vb)