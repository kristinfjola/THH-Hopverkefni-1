# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
import math
globfjarmagns = 0
globvextir = 0
vt = 0

## Kall á fall til að reikna innlogn
## sparitimi.innlogn(upphæð sem safna á uppí, vextir, mánuðir, eingreiðsla eða ekki (0 eða 1))


def innlogn(heild, v, nt, eingr):
	v = v/100.0
	if !eingr:
		return eingreidslaSparInnlogn(nt, v, heild)
	else:
		return manadalegurSparInnlogn(nt, v, heild)

## Kall á fall til að reikna timabil
## sparitimi.timabil(Upphæð sem leggja á inn á mánuði, vextir, upphæð sem safna á uppí, eingreiðsla eða ekki (0 eða 1))

def timabil(L, v, heild, eingr):
	v = v/100.0
	if !eingr:
		return eingreidslaSparTimi(L, v, vt, heild)
	else:
		return manadalegurSparTimi(L, v, vt, heild)






## Fall sem skilar hversu mikið þú þarft að leggja inn á mánuði til þess að eiga ákveðna upphæð eftir eitthvað marga mánuði
"""
Notkun: 
Fyrir:
Eftir:
"""
def manadalegurSparInnlogn(nt, v, heild):
	temp = 0.0
	i = 0
	for i in range(1, nt+1):
		temp = temp + (1+(v/12)*0.9)**i
	return "Thu tharft ad spara " + str(math.ceil(1.0*heild/temp)) + " a manudi til thess ad komast uppi " + str(heild)


## Fall sem skilar hversu mikið þú þarft að leggja inn í upphafi tiþess að eiga ákveðna upphæð eftir eitthvað marga mánuði
"""
Notkun:
Fyrir:
Eftir:
"""
def eingreidslaSparInnlogn(nt, v, heild):
	innlogn = heild/(pow((1+v),(nt/12.0)))
	return "Thu tharft ad leggja inn "+str(math.ceil(innlogn)) + " i upphafi til thess ad na uppi " + str(heild)


##heild = innlogn * pow((1+v), nt/12))

## Timinn sem tekur að spara uppí ákveðna upphæð
## Fallið gerir ráð fyrir vöxtum, verðbólgu og fjármagnstekjuskatti
## (og er því ekki í samræmi við bankareiknivélar því flestar gera ekki ráð fyrir verðbólgu eða fjármagnstekjuskatti)
"""
Notkun: timi = manadalegurSpar(L, v, vt, heild)
Fyrir: L er mánaðaleg innlögn, v er ársvextir, vt er verðbólga og heild er upphæð sem notandi vill safna uppí.
Eftir: timi er sá tími sem tekur að safna uppí heild með L innlögn á mánuði. timi er strengur í mánuðum.
"""
def manadalegurSparTimi(L, v, vt, heild):
	global globvextir
	global globfjarmagns
	fjarmagns = 0.8
	summa = 0
	stodur = [L]
	vextir = []
	vextirAr = []
	verdbaetur = []
	verdbaeturAr = []
	for i in range(0,10000):
		if summa >= heild:
			return "Thu tarft ad spara i "+str(i)+ " manudi til thess ad na uppi "+ str(heild)
		elif i == 9999:
			return "Thu tharft ad spara i "+ str(i) + " manudi eda lengur"
		summa = (summa + L)*(1+(vt/12))
		verdbaetur.append(summa*(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextir.append(summa * v/12)
		vextirAr.append(summa * v/12)
		if (i+1)%12 == 0 and i != 0:		
			stodur.append(math.ceil(summa + sum(vextirAr)*fjarmagns))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(math.ceil(summa))
	globvextir = sum(vextir)*fjarmagns + sum(verdbaetur)*fjarmagns
	globfjarmagns = sum(vextir)*(1-fjarmagns) + sum(verdbaetur)*(1-fjarmagns)
	return "Virkaði ekki"


## Fall sem skilar tíma sem það tekur að safna uppí ákveðna upphæð með .....................
"""
Notkun: tala = eingreidsla(L, nt, v, vt)
Fyrir:  
Eftir: 
"""
def eingreidslaSparTimi(L, v, vt, heild):
	global globvextir
	global globfjarmagns
	fjarmagns = 0.8
	summa = L
	stodur = [L]
	vextir = []
	vextirAr = []
	verdbaetur = []
	verdbaeturAr = []
	x = []
	skil = []
	for i in range(0, 10000):
		if summa >= heild:
			return "Thu tharft ad spara i " + str(i) + " manudi til thess ad na uppi " + str(heild)
		elif i == 9999:
			return "Thu tharft ad spara i " + str(i) + " eda lengur"
		summa = summa * (1+(vt/12))
		verdbaetur.append(summa*(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextir.append(summa * (v/12))
		vextirAr.append(summa * (v/12))
		if (i+1)%12 == 0 and i != 0:
			stodur.append(math.ceil(summa + sum(vextirAr)*fjarmagns))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(math.ceil(summa))
	globvextir = sum(vextir)*fjarmagns + sum(verdbaetur)*fjarmagns
	globfjarmagns = sum(vextir)*(1-fjarmagns) + sum(verdbaetur)*(1-fjarmagns)
	return "Virkaði ekki"