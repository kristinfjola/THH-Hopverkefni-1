# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
## I thessu skjali er virkni fyrir sparnad í tab 1.

import math
import gogn
import lan_v
besta_spar = [""]
fjarmagns = 0.8
globvextir = 0
globfjarmagns = 0
vb = 0
#=========================================================
"""
Notkun: hvad_er_best_ad_gera(b)
Fyrir: 	b er binditíminn sem notandi valdi
Eftir:	besta_leid er fylki með nafni og vaxtauppl um valda bestu leið
	best_ad_gera skilar streng um hvort sé betra að leggja inn á sparnað eða borga lán
"""
def hvad_er_best_ad_gera(b):
	global vb
	global besta_leid
	global verstu_lan
	global besta_spar
	#finnum bestu sparnaðarleið miðað við binditíma
	for i in range(len(gogn.sparnadarleidir)):
		for j in range(len(gogn.sparnadarleidir[0])):
			if gogn.sparnadarleidir[i][2] == b:
				besta_spar = gogn.sparnadarleidir[i] #fylki með öllum uppl um bestu sparnaðarleið
				break
	# fá hæstu lánavexti
	verstu_lan = lan_v.raunvLan()[1] # hæstu vextir láns
	# reikna með verðbólgu verðtryggðra reikninga
	if (besta_spar[3]==1):
		bestu_spar_vx = besta_spar[1]+vb 
	else:
		bestu_spar_vx = besta_spar[1]

	# bera saman lána og sparnaðarvexti
	if (verstu_lan < bestu_spar_vx):
		besta_leid = besta_spar #besta_leid er fylki fyrir sparnaðarleið
	else:
		if (verstu_lan >= bestu_spar_vx):
			besta_leid = lan_v.raunvLan() #besta_leid er fylki með nafni og vöxtum láns
	# segja hvað er best að gera í streng t.d. return 'að leggja inná ' + besta_leid
	besta_leidin = str(besta_leid[0])
	if (besta_leidin=='lan1'):
		besta_leidin = 'Lán 1'
	if (besta_leidin=='lan2'):
		besta_leidin = 'Lán 2'
	if (besta_leidin=='lan3'):
		besta_leidin = 'Lán 3'
	return 'að borga inn á ' + besta_leidin 
	return 'Ad borga inn a ' + str(besta_leid[0])

"""
Notkun: fa_bestu_sparnadarleid()
Fyrir: 	Besta sparnaðarleið hefur verið valin
Eftir:	besta_spar er strengur með nafni á valinni sparnaðarleið
"""
def fa_bestu_sparnadarleid():
	return besta_spar[0]
"""
Notkun: fa_uppl_um_bestu_sparnadarleid()
Fyrir: 	Besta sparnaðarleið hefur verið valin
Eftir:	uppl_um_bestu_leid er strengur með lýsingu á valinni sparnaðarleið
"""
def fa_uppl_um_sparnadarleid():
	return besta_spar[4]
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
def raunvx(vt,b):
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
#======================================================
"""

Fall sem skilar vöxtum reiknings, óháð verðbólgu.
Notkun: sparivx(vt,b)
Fyrir: 	vt er 1 ef verðtryggður reikningur, 0 annars. 
		b er binditíminn í mánuðum.
Eftir: 	vextir eru vextirnir á viðeigandi reikningi.
"""
def sparivx(vt,b):
	if vt==0:
		if b==0:
			vextir = 0.036
		elif b==12:
			vextir = 0.046
		elif b==18:
			vextir = 0.048
		elif b==24:
			vextir = 0.053
		else:
			vextir = 1000
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
#===========================================================









"""Föll sem snúa að sparnaði og gröfum"""


##L = lagt fyrir á mánuði
##nt = mánuðir í sparnað 
##v = vextir í prósentum
##vb = verðbólga í prósentum
##stodur = fylki, stak fyrir hvern mánuð, staða á reikning á hverjum tímapunkti
##vextir = fylki, stak fyrir hvern mánuð, vextir sem maður fær í hverjum mánuði, lagt við í lok 
##summa = heildarupphæð á tímapunkti á reikningi

#eingreiðsla = 0
#Mánaðalega = 1

## Fall sem tekur inn breytur úr GUI og sendir á sparnaðarföll og vistar verðbólgu í global breytu.
## Notkun: spar(Umframgreiðsla, mánuðir sparað, verðbólga síðustu x mánaða(0, 5, 10, 15), verðtryggt eða ekki (0/1), 
##	eingreiðsla eða mánaðaleg greiðsla(0/1), bundið í x mánuði (12, 18, 24, 36...))
"""
Notkun: fylki = spar(L, verdb, verdtrygg, manadagr, bundid)
Fyrir: L er umframgreiðsla (gildi int tala), verdb er gildi sem kemur úr dropdown þegar notandi velur verðbólgu (gildi 0, 5, 10, 15), 
		verdtrygg er hvort notandi valdi verðtryggðan sparnað eða ekki (gildi 0 eða 1), 
		manadagr er hvort notandi valdi eingreiðslu eða mánaðageiðslu (gildi 0 eða 1) og 
		bundid er val notanda úr dropdown hversu lengi hann var tilbúinn að binda sparnað (gildi 12, 18, 24, 36, 48, 60)
Eftir: fylki er fylki úr föllunum manadalega eda eingreidsla eftir innputi
"""
def spar(L, verdb, verdtrygg, manadagr, bundid):
	global vb
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

	v = sparivx(verdtrygg, bundid) 

	if verdtrygg == 1:
		if manadagr == 1:
			return manadalega(L, 12, v, vb)
		else:
			return eingreidsla(L, 12, v, vb)
	else:
		if manadagr == 1:
			return manadalega(L, 12, v, 0.0)
		else:
			return eingreidsla(L, 12, v, 0.0)



#Verðtryggt, vextir og verðbætur borgað 31.des (verðbólga sú sama út allt árið)
#Notkun: verdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
def manadalega(L, nt, v, vt):
	global globvextir
	global globfjarmagns
	summa = 0
	stodur = [L]
	vextir = []
	vextirAr = []
	verdbaetur = []
	verdbaeturAr = []
	x = []
	skil = []
	for i in range(0,nt):
		x.append(i)
		summa = (summa + L)*(1+(vt/12))
		verdbaetur.append(summa*(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextir.append(summa * (v/12))
		vextirAr.append(summa * (v/12))
		if (i+1)%12 == 0 and i != 0:		
			stodur.append(int(math.ceil(summa + sum(vextirAr)*fjarmagns)))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(int(math.ceil(summa)))
	globvextir = sum(vextir)*fjarmagns + sum(verdbaetur)*fjarmagns
	globfjarmagns = sum(vextir)*(1-fjarmagns) + sum(verdbaetur)*(1-fjarmagns)
	x.append(nt)
	skil.append(x)
	skil.append(stodur)
	return skil


##Fall sem reiknar upphæð eftir tiltekinn tíma þegar eingreiðsla er valin
## Fallið tekur tilit til verðbólgu. Vextir, verðbætur og fjármagnstekjuskattur greitt 31. des

def eingreidsla(L, nt, v, vt):
	global globvextir
	global globfjarmagns
	summa = L
	stodur = [L]
	vextir = []
	vextirAr = []
	verdbaetur = []
	verdbaeturAr = []
	x = []
	skil = []
	for i in range(0, nt):
		x.append(i)
		summa = summa * (1+(vt/12))
		verdbaetur.append(summa*(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextir.append(summa * (v/12))
		vextirAr.append(summa * (v/12))
		if (i+1)%12 == 0 and i != 0:
			stodur.append(int(math.ceil(summa + sum(vextirAr)*fjarmagns)))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(int(math.ceil(summa)))
	globvextir = sum(vextir)*fjarmagns + sum(verdbaetur)*fjarmagns
	globfjarmagns = sum(vextir)*(1-fjarmagns) + sum(verdbaetur)*(1-fjarmagns)
	x.append(nt)
	skil.append(x)
	skil.append(stodur)
	return skil



"""
Notkun: ars = fa_arsvexti()
Fyrir: global breytan globalvextir er til
Eftir: ars eru vextir sem notandi fékk á síðasta sparnað
"""
def fa_arsvexti():
	global globvextir
	return int(math.ceil(globvextir))

"""
Notkun: fjarmagns = fa_fjarmagnstekjuskatt()
Fyrir: global breytan globalfjarmagns er til
Eftir: fjarmagns er fjármagnstekjuskatturinn sem notandi þurfti að greiða af síðasta sparnaði
"""
def fa_fjarmagnstekjuskatt():
	global globfjarmagns
	return int(math.ceil(globfjarmagns))




































"""
Notkun: fa_bestu_sparnadarleid()
Fyrir: 	Besta sparnaÃ°arleiÃ° hefur veriÃ° valin
Eftir:	besta_spar er strengur meÃ° nafni Ã¡ valinni sparnaÃ°arleiÃ°
"""
def fa_bestu_sparnadarleid():
	return besta_spar[0]
"""
Notkun: fa_uppl_um_bestu_sparnadarleid()
Fyrir: 	Besta sparnaÃ°arleiÃ° hefur veriÃ° valin
Eftir:	uppl_um_bestu_leid er strengur meÃ° lÃ½singu Ã¡ valinni sparnaÃ°arleiÃ°
"""
def fa_uppl_um_sparnadarleid():
	return besta_spar[4]
"""
====
Reiknar raunvexti reiknings. Ef verÃ°tryggÃ°ur breytast vextirnir meÃ° verÃ°bÃ³lgunni
Ef Ã³verÃ°tryggÃ°ur minnka/hÃ¦kka raunvextir m.t.t. verÃ°bÃ³lgu
Notkun: raunvx(vt,b,vb)
Fyrir: 	vt er 1 ef verÃ°tryggÃ°ur reikningur, 0 annars. 
		b er binditÃ­minn Ã­ mÃ¡nuÃ°um.
		vb er verÃ°bÃ³lga sem reiknaÃ° er meÃ° (ef 3 prÃ³sent verÃ°bÃ³lga er vb = 0.03)
Eftir: 	vextir eru vextirnir Ã¡ viÃ°eigandi reikningi m.t.t. verÃ°bÃ³lgu 
"""
def raunvx(vt,b):
	#Ã³verÃ°tryggt - breytist ekki meÃ° verÃ°bÃ³lgu
	#raunvextir = nafnvextir - verÃ°bÃ³lga
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
	#verÃ°tryggt - breytist meÃ° verÃ°bÃ³lgu
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
#======================================================
"""

Fall sem skilar vÃ¶xtum reiknings, Ã³hÃ¡Ã° verÃ°bÃ³lgu.
Notkun: sparivx(vt,b)
Fyrir: 	vt er 1 ef verÃ°tryggÃ°ur reikningur, 0 annars. 
		b er binditÃ­minn Ã­ mÃ¡nuÃ°um.
Eftir: 	vextir eru vextirnir Ã¡ viÃ°eigandi reikningi.
"""
def sparivx(vt,b):
	if vt==0:
		if b==0:
			vextir = 0.036
		elif b==12:
			vextir = 0.046
		elif b==18:
			vextir = 0.048
		elif b==24:
			vextir = 0.053
		else:
			vextir = 1000
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
#===========================================================









"""FÃ¶ll sem snÃºa aÃ° sparnaÃ°i og grÃ¶fum"""


##L = lagt fyrir Ã¡ mÃ¡nuÃ°i
##nt = mÃ¡nuÃ°ir Ã­ sparnaÃ° 
##v = vextir Ã­ prÃ³sentum
##vb = verÃ°bÃ³lga Ã­ prÃ³sentum
##stodur = fylki, stak fyrir hvern mÃ¡nuÃ°, staÃ°a Ã¡ reikning Ã¡ hverjum tÃ­mapunkti
##vextir = fylki, stak fyrir hvern mÃ¡nuÃ°, vextir sem maÃ°ur fÃ¦r Ã­ hverjum mÃ¡nuÃ°i, lagt viÃ° Ã­ lok 
##summa = heildarupphÃ¦Ã° Ã¡ tÃ­mapunkti Ã¡ reikningi

#eingreiÃ°sla = 0
#MÃ¡naÃ°alega = 1

## Fall sem tekur inn breytur Ãºr GUI og sendir Ã¡ sparnaÃ°arfÃ¶ll og vistar verÃ°bÃ³lgu Ã­ global breytu.
## Notkun: spar(UmframgreiÃ°sla, mÃ¡nuÃ°ir sparaÃ°, verÃ°bÃ³lga sÃ­Ã°ustu x mÃ¡naÃ°a(0, 5, 10, 15), verÃ°tryggt eÃ°a ekki (0/1), 
##	eingreiÃ°sla eÃ°a mÃ¡naÃ°aleg greiÃ°sla(0/1), bundiÃ° Ã­ x mÃ¡nuÃ°i (12, 18, 24, 36...))
"""
Notkun: fylki = spar(L, verdb, verdtrygg, manadagr, bundid)
Fyrir: L er umframgreiÃ°sla (gildi int tala), verdb er gildi sem kemur Ãºr dropdown Ã¾egar notandi velur verÃ°bÃ³lgu (gildi 0, 5, 10, 15), 
		verdtrygg er hvort notandi valdi verÃ°tryggÃ°an sparnaÃ° eÃ°a ekki (gildi 0 eÃ°a 1), 
		manadagr er hvort notandi valdi eingreiÃ°slu eÃ°a mÃ¡naÃ°ageiÃ°slu (gildi 0 eÃ°a 1) og 
		bundid er val notanda Ãºr dropdown hversu lengi hann var tilbÃºinn aÃ° binda sparnaÃ° (gildi 12, 18, 24, 36, 48, 60)
Eftir: fylki er fylki Ãºr fÃ¶llunum manadalega eda eingreidsla eftir innputi
"""
def spar(L, verdb, verdtrygg, manadagr, bundid):
	global vb
	if(verdb == 0): 		#verÃ°bÃ³lga nÃºna
		vb = 0.031
	elif(verdb == 5): 		#verÃ°bÃ³lga 5 Ã¡r
		vb = 0.0607868852459016
	elif(verdb == 10): 		#verÃ°bÃ³lga 10 Ã¡r
		vb = 0.0619421487603305
	elif(verdb == 15):		#verÃ°bÃ³lga 15 Ã¡r
		vb = 0.0560276243093922
	else:					#verÃ°bÃ³lga 0 ef allt klikkar
		vb = 0.0

	v = sparivx(verdtrygg, bundid) 

	if verdtrygg == 1:
		if manadagr == 1:
			return manadalega(L, 12, v, vb)
		else:
			return eingreidsla(L, 12, v, vb)
	else:
		if manadagr == 1:
			return manadalega(L, 12, v, 0.0)
		else:
			return eingreidsla(L, 12, v, 0.0)



#VerÃ°tryggt, vextir og verÃ°bÃ¦tur borgaÃ° 31.des (verÃ°bÃ³lga sÃº sama Ãºt allt Ã¡riÃ°)
#Notkun: verdtryggtArs(Lagt fyrir Ã¡ mÃ¡n, fjÃ¶ldi mÃ¡naÃ°a, vextir, verÃ°bÃ³lga/bÃ¦tur)
def manadalega(L, nt, v, vt):
	global globvextir
	global globfjarmagns
	summa = 0
	stodur = [L]
	vextir = []
	vextirAr = []
	verdbaetur = []
	verdbaeturAr = []
	x = []
	skil = []
	for i in range(0,nt):
		x.append(i)
		summa = (summa + L)*(1+(vt/12))
		verdbaetur.append(summa*(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextir.append(summa * (v/12))
		vextirAr.append(summa * (v/12))
		if (i+1)%12 == 0 and i != 0:		
			stodur.append(int(math.ceil(summa + sum(vextirAr)*fjarmagns)))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(int(math.ceil(summa)))
	globvextir = sum(vextir)*fjarmagns + sum(verdbaetur)*fjarmagns
	globfjarmagns = sum(vextir)*(1-fjarmagns) + sum(verdbaetur)*(1-fjarmagns)
	x.append(nt)
	skil.append(x)
	skil.append(stodur)
	return skil


##Fall sem reiknar upphÃ¦Ã° eftir tiltekinn tÃ­ma Ã¾egar eingreiÃ°sla er valin
## FalliÃ° tekur tilit til verÃ°bÃ³lgu. Vextir, verÃ°bÃ¦tur og fjÃ¡rmagnstekjuskattur greitt 31. des

def eingreidsla(L, nt, v, vt):
	global globvextir
	global globfjarmagns
	summa = L
	stodur = [L]
	vextir = []
	vextirAr = []
	verdbaetur = []
	verdbaeturAr = []
	x = []
	skil = []
	for i in range(0, nt):
		x.append(i)
		summa = summa * (1+(vt/12))
		verdbaetur.append(summa*(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextir.append(summa * (v/12))
		vextirAr.append(summa * (v/12))
		if (i+1)%12 == 0 and i != 0:
			stodur.append(int(math.ceil(summa + sum(vextirAr)*fjarmagns)))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(int(math.ceil(summa)))
	globvextir = sum(vextir)*fjarmagns + sum(verdbaetur)*fjarmagns
	globfjarmagns = sum(vextir)*(1-fjarmagns) + sum(verdbaetur)*(1-fjarmagns)
	x.append(nt)
	skil.append(x)
	skil.append(stodur)
	return skil



"""
Notkun: ars = fa_arsvexti()
Fyrir: global breytan globalvextir er til
Eftir: ars eru vextir sem notandi fÃ©kk Ã¡ sÃ­Ã°asta sparnaÃ°
"""
def fa_arsvexti():
	global globvextir
	return int(math.ceil(globvextir))

"""
Notkun: fjarmagns = fa_fjarmagnstekjuskatt()
Fyrir: global breytan globalfjarmagns er til
Eftir: fjarmagns er fjÃ¡rmagnstekjuskatturinn sem notandi Ã¾urfti aÃ° greiÃ°a af sÃ­Ã°asta sparnaÃ°i
"""
def fa_fjarmagnstekjuskatt():
	global globfjarmagns
	return int(math.ceil(globfjarmagns))

