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

v = 0.05  ##erum ekki enn með reikninga til þess að velja svo allir vextir eru bara 5% atm

##Notkun: spar(Umframgreiðsla, mánuðir sparað, verðbólga síðustu x mánaða, verðtryggt,  )
def spar(L, nt, verdb, verdtrygg, man):
	if verdb == 0:
		vb = 0.02
	elif verdb == 5:
		vb = 0.04
	elif verdb == 10:
		vb = 0.06
	elif verdb == 15:
		vb = 0.08
	else:
		vb = 0.0

	if verdtrygg == 1:
		if man == 1:
			verdtryggtMan(L, nt, v, vb)
		else:
			verdtryggtArs(L, nt, v, vb)
	else:
		if man == 1:
			overdtryggtMan(L, nt, v)
		else:
			overdtryggtArs(L, nt, v)



"""Ef vextir eru borgaðir mánaðalega"""




#Óverðtryggt, vextir greiddir mánaðalega
#Notkun: overdtryggtMan(Lagt fyrir á mán, fjöldi mánaða, vextir)
def overdtryggtMan(L, nt, v):
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


#Verðtryggt, vextir og verðbætur borgaðar mánaðalega (verðbólga sú sama allt árið)
#Notkun: verdtryggtMan(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
def verdtryggtMan(L, nt, v, vb):
	summa = 0
	stodur = [L]
	for i in range(0,nt):
		summa = summa + L
		stada = (summa * ((1+(v/12))*(1+(vb/12))))
		summa = math.ceil(stada)
		stodur.append(summa)
	print "Verðtryggt, vextir greiddir mánaðalega"
	print str(stodur[0]) + " er innistæða í upphafi 1. mánaðar"
	for i in range(1, len(stodur)):
		print str(stodur[i]) + " er innistæða eftir " + str(i) + "mánuð"





"""Ef vextir eru borgaðir í árslok"""




#Óverðtryggt, vextir borgaðir 31.des
#Notkun: overdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir)
def overdtryggtArs(L, nt, v):
	summa = 0
	stodur = [L]
	vextir = []
	for i in range(0,nt):
		summa = summa + L
		vextir.append(summa * (v/12))
		if i == 11:
			stodur.append(summa+sum(vextir)) ##Ef það er 31.des, leggjum við vexti við summuna
			print "Óverðtryggt, vextir borgaðir 31. des"
		else:
			stodur.append(math.ceil(summa))
	for i in range(0, len(stodur)):
		print stodur[i]
	print sum(vextir) 			##Heildarvextir sem greiddir eru út í árslok


#Verðtryggt, vextir og verðbætur borgað 31.des (verðbólga sú sama út allt árið)
#Notkun: verdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
def verdtryggtArs(L, nt, v, vb):
	summa = 0
	stodur = [L]
	vextir = []
	for i in range(0,nt):
		summa = summa + L
		vextir.append((summa * ((1+(v/12))*(1+(vb/12))))-summa)
		if i%11 == 0 and i != 0:
			stodur.append(summa + sum(vextir))
			summa = summa + sum(vextir)
			print "Verðtryggt, vextir og verðbætur borgaðar 31. des"
		else:
			stodur.append(math.ceil(summa))
	for i in range(0, len(stodur)):
		print stodur[i]
	print "Vextir og verðbætur á þessu tímabili eru "+ sum(vextir)			##Heildarvextir og verðbætur sem greiddar eru út í árslok
