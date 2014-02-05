##lan_v.py
# def lan(lan_upph, lan_vextir, lan_verdbolga, lan_greidslubyrgdi, lan_timabil, lan_verdtrygging, lan_jafnar):

def lan(H, v, verdbolga, gb, n, verdtrygging, jafnar)
	if(verdbolga == 0): 			#verðbólga núna
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
	afb = H/n
	stodur = []
	def temp(greidsla, eftirs, summa):
		if (eftirs == 0):
			stodur.append(eftirs)
			print summa
		else:
			stodur.append(eftirs)
			#greidsla = afb + v*eftirs
			#eftirs = eftirs - afb
			#summa = summa + greidsla
			temp(afb + v*eftirs, eftirs - afb, summa + (afb + v*eftirs))
	temp(0, H, 0)
	
	print '--------------'
	# Prenta stöðu lánsins á hverjum tíma t (checka hvort stodur[] virkar)
	for i in range(0, len(stodur)):
		print round(stodur[i])	


# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað árlega (er ennþá að vinna í þessu, ég gerði bara (vextir+verðbólga))
# Noktun: verdAfborganir(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))
def verdAfborganir(H, n, v, vb):
	afb = H/n
	stodur = []
	def temp(greidsla, eftirs, summa):
		if (eftirs == 0):
			stodur.append(eftirs)
			print summa
		else:
			stodur.append(eftirs)
			#greidsla = afb + (v+vb)*eftirs
			#eftirs = eftirs - afb
			#summa = summa + greidsla
			temp(afb + (v+vb)*eftirs, eftirs - afb, summa + (afb + (v+vb)*eftirs))
	temp(0, H, 0)
	
	print '--------------'
	# Prenta stöðu lánsins á hverjum tíma t (checka hvort stodur[] virkar)
	for i in range(0, len(stodur)):
		print round(stodur[i])
		

# Óverðtryggt, jafnar greiðslur, reiknað árlega
# Notkun: overdGreidslur(höfuðstóll, fjöldi ára, vextir(%))
def overdGreidslur(H, n, v):
	import math
	A = H*((v*(1+v)**n)/(((1+v)**n)-1))	#Jafna til að finna greiðslu
	greidsla = math.ceil(A*10)/10 #námunda með einn aukastaf
	stodur = []
	def temp(vextir, afb, eftirs, summa):
		if(eftirs <= 0):
			stodur.append(eftirs)
			print math.ceil(summa)
		else:
			stodur.append(eftirs)
			vextir = v*eftirs
			afb = greidsla - vextir
			eftirs = eftirs - afb
			summa = summa + greidsla
			temp(vextir, afb, eftirs, summa)
	temp(0, 0, H, 0)
	
	print '--------------'
	# Prenta stöðu lánsins á hverjum tíma t (checka hvort stodur[] virkar)
	for i in range(0, len(stodur)):
		print round(stodur[i])

		
# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað árlega (er í lagi ef eyjan.is	er ok)
# Notkun: verdGreidslur(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))	
def verdGreidslur(H, n, v, vb):
	vt = v 
	nt = n 
	stodur = []
	A = H*((vt*(1+vt)**nt)/(((1+vt)**nt)-1))	
	
	def temp(eftirs, greidsla, summa):
		if (round(eftirs) == 0):
			stodur.append(eftirs)
			print round(summa)
		else:
			stodur.append(eftirs)
			eftirs = eftirs + vb*eftirs
			greidsla = (1+vb)*greidsla
			afb = greidsla - v*eftirs
			temp(eftirs-afb, greidsla, summa+greidsla)
	temp(H, A, 0)
	print '--------------'
	for i in range(0, len(stodur)):
		print round(stodur[i])