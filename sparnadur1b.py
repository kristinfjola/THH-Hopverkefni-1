# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
## I thessu skjali er virkni fyrir sparnad � tab 1.

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
Fyrir: 	b er bindit�minn sem notandi valdi
Eftir:	besta_leid er fylki me� nafni og vaxtauppl um valda bestu lei�
	best_ad_gera skilar streng um hvort s� betra a� leggja inn � sparna� e�a borga l�n
"""
def hvad_er_best_ad_gera(b):
	global vb
	global besta_leid
	global verstu_lan
	global besta_spar
	#finnum bestu sparna�arlei� mi�a� vi� bindit�ma
	for i in range(len(gogn.sparnadarleidir)):
		for j in range(len(gogn.sparnadarleidir[0])):
			if gogn.sparnadarleidir[i][2] == b:
				besta_spar = gogn.sparnadarleidir[i] #fylki me� �llum uppl um bestu sparna�arlei�
				break
	# f� h�stu l�navexti
	verstu_lan = lan_v.raunvLan()[1] # h�stu vextir l�ns
	# reikna me� ver�b�lgu ver�trygg�ra reikninga
	if (besta_spar[3]==1):
		bestu_spar_vx = besta_spar[1]+vb 
	else:
		bestu_spar_vx = besta_spar[1]

	# bera saman l�na og sparna�arvexti
	if (verstu_lan < bestu_spar_vx):
		besta_leid = besta_spar #besta_leid er fylki fyrir sparna�arlei�
	else:
		if (verstu_lan >= bestu_spar_vx):
			besta_leid = lan_v.raunvLan() #besta_leid er fylki me� nafni og v�xtum l�ns
	# segja hva� er best a� gera � streng t.d. return 'a� leggja inn� ' + besta_leid
	besta_leidin = str(besta_leid[0])
	if (besta_leidin=='lan1'):
		besta_leidin = 'L�n 1'
	if (besta_leidin=='lan2'):
		besta_leidin = 'L�n 2'
	if (besta_leidin=='lan3'):
		besta_leidin = 'L�n 3'
	return 'a� borga inn � ' + besta_leidin 
	return 'Ad borga inn a ' + str(besta_leid[0])

"""
Notkun: fa_bestu_sparnadarleid()
Fyrir: 	Besta sparna�arlei� hefur veri� valin
Eftir:	besta_spar er strengur me� nafni � valinni sparna�arlei�
"""
def fa_bestu_sparnadarleid():
	return besta_spar[0]
"""
Notkun: fa_uppl_um_bestu_sparnadarleid()
Fyrir: 	Besta sparna�arlei� hefur veri� valin
Eftir:	uppl_um_bestu_leid er strengur me� l�singu � valinni sparna�arlei�
"""
def fa_uppl_um_sparnadarleid():
	return besta_spar[4]
"""
====
Reiknar raunvexti reiknings. Ef ver�trygg�ur breytast vextirnir me� ver�b�lgunni
Ef �ver�trygg�ur minnka/h�kka raunvextir m.t.t. ver�b�lgu
Notkun: raunvx(vt,b,vb)
Fyrir: 	vt er 1 ef ver�trygg�ur reikningur, 0 annars. 
		b er bindit�minn � m�nu�um.
		vb er ver�b�lga sem reikna� er me� (ef 3 pr�sent ver�b�lga er vb = 0.03)
Eftir: 	vextir eru vextirnir � vi�eigandi reikningi m.t.t. ver�b�lgu 
"""
def raunvx(vt,b):
	#�ver�tryggt - breytist ekki me� ver�b�lgu
	#raunvextir = nafnvextir - ver�b�lga
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
	#ver�tryggt - breytist me� ver�b�lgu
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

Fall sem skilar v�xtum reiknings, �h�� ver�b�lgu.
Notkun: sparivx(vt,b)
Fyrir: 	vt er 1 ef ver�trygg�ur reikningur, 0 annars. 
		b er bindit�minn � m�nu�um.
Eftir: 	vextir eru vextirnir � vi�eigandi reikningi.
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









"""F�ll sem sn�a a� sparna�i og gr�fum"""


##L = lagt fyrir � m�nu�i
##nt = m�nu�ir � sparna� 
##v = vextir � pr�sentum
##vb = ver�b�lga � pr�sentum
##stodur = fylki, stak fyrir hvern m�nu�, sta�a � reikning � hverjum t�mapunkti
##vextir = fylki, stak fyrir hvern m�nu�, vextir sem ma�ur f�r � hverjum m�nu�i, lagt vi� � lok 
##summa = heildarupph�� � t�mapunkti � reikningi

#eingrei�sla = 0
#M�na�alega = 1

## Fall sem tekur inn breytur �r GUI og sendir � sparna�arf�ll og vistar ver�b�lgu � global breytu.
## Notkun: spar(Umframgrei�sla, m�nu�ir spara�, ver�b�lga s��ustu x m�na�a(0, 5, 10, 15), ver�tryggt e�a ekki (0/1), 
##	eingrei�sla e�a m�na�aleg grei�sla(0/1), bundi� � x m�nu�i (12, 18, 24, 36...))
"""
Notkun: fylki = spar(L, verdb, verdtrygg, manadagr, bundid)
Fyrir: L er umframgrei�sla (gildi int tala), verdb er gildi sem kemur �r dropdown �egar notandi velur ver�b�lgu (gildi 0, 5, 10, 15), 
		verdtrygg er hvort notandi valdi ver�trygg�an sparna� e�a ekki (gildi 0 e�a 1), 
		manadagr er hvort notandi valdi eingrei�slu e�a m�na�agei�slu (gildi 0 e�a 1) og 
		bundid er val notanda �r dropdown hversu lengi hann var tilb�inn a� binda sparna� (gildi 12, 18, 24, 36, 48, 60)
Eftir: fylki er fylki �r f�llunum manadalega eda eingreidsla eftir innputi
"""
def spar(L, verdb, verdtrygg, manadagr, bundid):
	global vb
	if(verdb == 0): 		#ver�b�lga n�na
		vb = 0.031
	elif(verdb == 5): 		#ver�b�lga 5 �r
		vb = 0.0607868852459016
	elif(verdb == 10): 		#ver�b�lga 10 �r
		vb = 0.0619421487603305
	elif(verdb == 15):		#ver�b�lga 15 �r
		vb = 0.0560276243093922
	else:					#ver�b�lga 0 ef allt klikkar
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



#Ver�tryggt, vextir og ver�b�tur borga� 31.des (ver�b�lga s� sama �t allt �ri�)
#Notkun: verdtryggtArs(Lagt fyrir � m�n, fj�ldi m�na�a, vextir, ver�b�lga/b�tur)
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


##Fall sem reiknar upph�� eftir tiltekinn t�ma �egar eingrei�sla er valin
## Falli� tekur tilit til ver�b�lgu. Vextir, ver�b�tur og fj�rmagnstekjuskattur greitt 31. des

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
Eftir: ars eru vextir sem notandi f�kk � s��asta sparna�
"""
def fa_arsvexti():
	global globvextir
	return int(math.ceil(globvextir))

"""
Notkun: fjarmagns = fa_fjarmagnstekjuskatt()
Fyrir: global breytan globalfjarmagns er til
Eftir: fjarmagns er fj�rmagnstekjuskatturinn sem notandi �urfti a� grei�a af s��asta sparna�i
"""
def fa_fjarmagnstekjuskatt():
	global globfjarmagns
	return int(math.ceil(globfjarmagns))




































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

