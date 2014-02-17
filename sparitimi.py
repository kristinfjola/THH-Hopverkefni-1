# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
import math
globfjarmagns = 0
globvextir = 0

## Fall sem skilar hversu mikið þú þarft að leggja inn á mánuði til þess að eiga ákveðna upphæð eftir eitthvað marga mánuði
"""
Notkun: 
Fyrir:
Eftir:
"""
def manadalegurSparInnlogn(upphaed, nt, v):
	temp = 0.0
	i = 0
	for i in range(1, nt+1):
		temp = temp + (1+(v/12)*0.9)**i
	return 1.0*upphaed/temp


## Fall sem skilar hversu mikið þú þarft að leggja inn í upphafi tiþess að eiga ákveðna upphæð eftir eitthvað marga mánuði
"""
Notkun:
Fyrir:
Eftir:
"""
def eingreidslaSparInnlogn(nt, v, heild):
	innlogn = heild/(pow((1+v),(nt/12.0)))
	return math.ceil(innlogn)


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
			return str(i)
		elif i == 9999:
			return str(i) + " eda lengur"
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
			return str(i)
		elif i == 9999:
			return str(i) + " eda lengur"
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