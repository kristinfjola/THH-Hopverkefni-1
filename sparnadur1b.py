##Kerfið reiknar framvindu óbreyts reiknings

##L = lagt fyrir á mánuði
##nt = mánuðir í sparnað 
##v = vextir í prósentum
##vb = verðbólga í prósentum
##stodur = fylki, stak fyrir hvern mánuð, staða á reikning á hverjum tímapunkti
##vextir = fylki, stak fyrir hvern mánuð, vextir sem maður fær í hverjum mánuði, lagt við í lok 
##summa = heildarupphæð á tímapunkti á reikningi
import math




"""Ef vextir eru borgaðir mánaðalega"""


#Óverðtryggt, vextir greiddir mánaðalega
def overdtryggtMan(L, nt, v):
	summa = 0
	stodur = [L]
	for i in range(0,nt):
		summa = summa + L
		stada = (summa * (1 + (v/12)))
		summa = math.ceil(stada)
		stodur.append(summa)
	for i in range(0, len(stodur)):
		print stodur[i]


#Verðtryggt, vextir og verðbætur borgaðar mánaðalega (verðbólga sú sama allt árið)
def verdtryggtMan(L, nt, v, vb):
	summa = 0
	stodur = [L]
	for i in range(0,nt):
		summa = summa + L
		stada = (summa * ((1+(v/12))*(1+(vb/12))))
		summa = math.ceil(stada)
		stodur.append(summa)
	for i in range(0, len(stodur)):
		print stodur[i]





"""Ef vextir eru borgaðir í árslok"""


#Óverðtryggt, vextir borgaðir 31.des
def overdtryggtArs(L, nt, v):
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
	for i in range(0, len(stodur)):
		print stodur[i]
	print sum(vextir) 			##Heildarvextir sem greiddir eru út í árslok


#Verðtryggt, vextir og verðbætur borgað 31.des (verðbólga sú sama út allt árið)
def verdtryggtArs(L, nt, v, vb):
	summa = 0
	stodur = [L]
	vextir = []
	for i in range(0,nt):
		summa = summa + L
		vextir.append((summa * ((1+(v/12))*(1+(vb/12))))-summa)
		if i == 11:
			stodur.append(summa + sum(vextir))
		else:
			stodur.append(math.ceil(summa))
	for i in range(0, len(stodur)):
		print stodur[i]
	print sum(vextir)			##Heildarvextir og verðbætur sem greiddar eru út í árslok