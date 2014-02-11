# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

##Kerfið reiknar framvindu óbreyts reiknings

##L = lagt fyrir á mánuði
##nt = mánuðir í sparnað 
##v = vextir í prósentum
##vb = verðbólga í prósentum
##stodur = fylki, stak fyrir hvern mánuð, staða á reikning á hverjum tímapunkti
##vextir = fylki, stak fyrir hvern mánuð, vextir sem maður fær í hverjum mánuði, lagt við í lok 
##summa = heildarupphæð á tímapunkti á reikningi
import math

#=========================================================

"""
====
Reiknar raunvexti reiknings. Ef verðtryggður breytast vextirnir með verðbólgunni
Ef óverðtryggður minnka/hækka raunvextir m.t.t. verðbólgu
Notkun: raunvx(vt,b,vb)
Fyrir: 	vt er 1 ef verðtryggður reikningur, 0 annars. 
		b er binditíminn í mánuðum.
		vb er verðbólga sem reiknað er með (ef 3 prósent verðbólga er vb = 0.03)
Eftir: 	vextir eru vextirnir á viðeigandi reikningi m.t.t. verðbólgu 
"""
def raunvx(vt,b,vb):
	#óverðtryggt - breytist ekki með verðbólgu
	#raunvextir = nafnvextir - verðbólga
	if vt==0:
		if b==0:
			vextir = 0.036-vb
		elif b==12:
			vextir = 0.046-vb
		elif b==18:
			vextir = 0.048-vb
		elif b==24:
			vextir = 0.048-vb
		else:
			vextir = 1000
	#verðtryggt - breytist með verðbólgu
	else:
		if vt==1:
			if b==36:
				vextir = 0.0175
			elif b==48:
				vextir = 0.0185
			elif b==60:
				vextir = 0.0195
			else:
				vextir = 1000
	return vextir
#======================================================0
v = raunvx(vt,b,vb)
fjarmagns = 0.8
#eingreiðsla = 0
#Mánaðalega = 1

##Notkun: spar(Umframgreiðsla, mánuðir sparað, verðbólga síðustu x mánaða, verðtryggt, eingreiðsla eða mánaðaleg greiðsla)
def spar(L, nt, verdb, verdtrygg, manadagr): ##Núna er ekki hægt að velja í GUI-inu mánaðalega eða árlega vexti, svo mánaðalegir eru default
	if(verdb == 0): 		#verðbólga núna
		vb = 0.031
	elif(verdb == 5): 		#verðbólga 5 ár
		vb = 0.0607868852459016
	elif(verdb == 10): 		#verðbólga 10 ár
		vb = 0.0619421487603305
	elif(verdb == 15):		#verðbólga 15 ár
		vb = 0.0560276243093922
	else:					#verðbólga 0 ef allt klikkar
		vb = 0.0

	if verdtrygg == 1:
		if manadagr == 1:
			return manadalega(L, nt, v, vb)
		else:
			return eingreidsla(L, nt, v, vb)
	else:
		if manadagr == 1:
			return manadalega(L, nt, v, 0.0)
		else:
			return eingreidsla(L, nt, v, 0.0)



#Verðtryggt, vextir og verðbætur borgað 31.des (verðbólga sú sama út allt árið)
#Notkun: verdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
def manadalega(L, nt, v, vb):
	summa = 0
	stodur = [L]
	vextir = []
	x = []
	skil = []
	for i in range(0,nt):
		x.append(i)
		summa = summa + L
		vextir.append((summa * ((1+(v/12))*(1+(vb/12))))-summa)
		if (i+1)%12 == 0 and i != 0:		
			stodur.append(math.ceil(summa + sum(vextir)*fjarmagns))
			summa = summa + sum(vextir)*fjarmagns
		else:
			stodur.append(math.ceil(summa))
	x.append(nt)
	skil.append(x)
	skil.append(stodur)
	return skil


##Eingreiðsla, verðtryggð, vextir og verðbætur greiddar 31. des
#Notkun: eingreidslaArs(Lagt fyrir í upphafi, fjöldi mánaða, vextir, verðbólga)
def eingreidsla(L, nt, v, vb):
	summa = L
	stodur = [L]
	vextir = []
	x = []
	skil = []
	for i in range(0, nt):
		x.append(i)
		vextir.append((summa * ((1+(v/12))*(1+(vb/12))))-summa)
		if (i+1)%12 == 0 and i != 0:
			stodur.append(math.ceil(summa + sum(vextir)*fjarmagns))
			summa = summa + sum(vextir)*fjarmagns
		else:
			stodur.append(math.ceil(summa))
	x.append(nt)
	skil.append(x)
	skil.append(stodur)
	return skil



"""Óþörf föll??"""
#Óverðtryggt, vextir greiddir mánaðalega
#Notkun: overdtryggtMan(Lagt fyrir á mán, fjöldi mánaða, vextir)
"""def overdtryggtMan(L, nt, v):
	summa = 0
	stodur = [L]
	for i in range(0,nt):
		summa = summa + L
		stada = (summa * (1 + (v/12)))
		summa = math.ceil(stada)
		stodur.append(summa)
	print "Óverðtryggt, vextir greiddir mánaðalega"
	print str(stodur[0]) + " er innistæða í upphafi 1. mánaðar"
	for i in range(1, len(stodur)):
		print str(stodur[i]) + " er innistæða eftir " + str(i) + " mánuði"
"""
#Óverðtryggt, vextir borgaðir 31.des
#Notkun: overdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir)
"""def overdtryggtArs(L, nt, v):
	print "Óverðtryggt, vextir greiddir árlega"
	summa = 0
	stodur = [L]
	vextir = []
	for i in range(0,nt):
		summa = summa + L
		vextir.append(summa * (v/12))
		if i == 11:
			stodur.append(summa+sum(vextir)) ##Ef það er 31.des, leggjum við vexti við summuna
		else:
			stodur.append(math.ceil(summa))
	print str(stodur[0])+ " innistæða í upphafi 1. mánaðar"
	for i in range(1, len(stodur)):
		print str(stodur[i]) + " er innistæða eftir " + str(i) + " mánuði" 
	print "Vextir á þessu tímabili eru " + sum(vextir) 			##Heildarvextir sem greiddir eru út í árslok
"""
##Eingreiðsla, verðtryggð, vextir og verðbætur greiddar mánaðalega
#Notkun: eingreidslaArs(Lagt fyrir í upphafi, fjöldi mánaða, vextir, verðbólga)
"""def eingreidslaMan(L, nt, v, vb):
	summa = L
	stodur = [L]
	for i in range(0, nt):
		stada = (summa * ((1+(v/12))*(1+(vb/12))))
		summa = math.ceil(stada)
		stodur.append(summa)
	return stodur
"""
#Verðtryggt, vextir og verðbætur borgaðar mánaðalega (verðbólga sú sama allt árið)
#Notkun: verdtryggtMan(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
"""def verdtryggtMan(L, nt, v, vb):
	summa = 0
	stodur = [L]
	for i in range(0,nt):
		summa = summa + L
		stada = (summa * ((1+(v/12))*(1+(vb/12))))
		summa = math.ceil(stada)
		stodur.append(summa)
	return stodur"""
