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