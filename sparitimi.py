# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
## I thessu skjali er virknin fyrir tab 2. 

import math
globfjarmagns = 0
globvextir = 0

## Fall sem kallad er a ur vidmdti til thess að fa upp hversu mikid tharf ad leggja inn til thess ad ná uppi tiltekna upphaed á tilteknum tima.
## sparitimi.innlogn(upphaed sem safna á uppi, vextir, ar, eingreidsla eda ekki (0 eða 1))
def innlogn(heild, v, nt, manada):
	v = v/100.0
	nt = nt * 12
	if manada:
		return manadalegurSparInnlogn(nt, v, heild)
	else:
		return eingreidslaSparInnlogn(nt, v, heild)

## 0 = óverðtryggður
## 1 = verðtryggður
## Fall sem kallad er a ur vidmoti til thess ad fa upp hversu lengi tharf að spara til þess að na uppi tiltekna upphaed thegar tiltekin upphaed er logd inn.
## sparitimi.timabil(Upphaed sem leggja a inn a manudi, vextir, upphaed sem safna a uppa, eingreidsla eða ekki (0 eða 1))
def timabil(L, v, heild, manada, vt):
	v = v/100.0
	verdb15 = 0.0560276243093922
	if vt == 0:
		if manada:
			return manadalegurSparTimi(L, v, vt, heild)
		else:
			return eingreidslaSparTimi(L, v, vt, heild)
	else:
		if manada:
			return manadalegurSparTimi(L, v, verdb15, heild)
		else:
			return eingreidslaSparTimi(L, v, verdb15, heild)


## Fall sem skilar hversu mikid thu tharft ad leggja inn a manudi til thess ad eiga akvedna upphaed eftir tiltekid marga manudi

##Notkun: innlogn = manadalegurSparInnlogn(nt, v, heild)
##Fyrir: nt er timabil i arum, v er vextir a float formi (0.0X fyrir X prosent vexti) og heild er upphaed sem safna a uppi
##Eftir: innlogn er strengur sem segir notanda hversu mikid hann tharf ad leggja inn a manudi
def manadalegurSparInnlogn(nt, v, heild):
	temp = 0.0
	i = 0
	for i in range(1, nt+1):
		temp = temp + (1+(v/12))**i
	return "Þú þarft að leggja inn " + str(int(1.0*heild/temp)) + " kr. á mánuði til þess að komast uppí " + str(heild) + " kr."


## Fall sem skilar hversu mikið þú þarft að leggja inn í upphafi til þess að eiga ákveðna upphæð eftir eitthvað marga mánuði

##Notkun: innlogn = eingreidslaSparInnlogn(nt, v, heild)
##Fyrir: nt er timabil i arum, v er vextir a float formi (0.0X fyrir X prosent vexti) og heild er upphaed sem safna a uppi
##Eftir: innlogn er strengur sem segir notanda hversu mikið hann tharf ad leggja inn i upphafi
def eingreidslaSparInnlogn(nt, v, heild):
	innlogn = heild/(pow((1+v),(nt/12.0)))
	return "Þú þarft að leggja inn "+ str(int(innlogn)) + " kr. í upphafi til þess að ná uppí " + str(heild) + " kr."


##Fall sem skiar manudum i manudum og arum

## Notkun: strengur = manudirIAr(tala)
## Fyrir: tala >= 0
## Eftir: strengur er tala skippt nidur í manudi og ar
def manudirIAr(tala):
	ar = tala / 12
	man = tala % 12
	if ar == 0:
		if man == 1:
			return str(man) + " mánuð"
		else:	
			return str(man) + " mánuði"
	elif man == 0:
		return str(ar) + " ár"
	else:
		if man == 1:
			return str(ar) + " ár og " + str(man) + " mánuð"
		else:	
			return str(ar) + " ár og " + str(man) + " mánuði"


## Timinn sem tekur að spara uppí ákveðna upphæð
## Fallið gerir ráð fyrir vöxtum greiddum árlega, verðbólgu og þar með verðbótum greiddum mánaðalega ef reikningur er verðtryggður og fjármagnstekjuskatti sem er dreginn frá árlega.
## Ekki í samræmi við bankanetreiknivélar þar sem þar eru vextir greiddir út strax. (Þessi aðferð segir lengri tíma)

## Notkun: timi = manadalegurSpar(L, v, vt, heild)
## Fyrir: L er mánaðaleg innlögn, v er ársvextir, vt er verðbólga og heild er upphæð sem notandi vill safna uppí.
## Eftir: timi er strengur sem segir notanda hversu lengi hann er að safna uppí tiltekna upphæð með tiltekinni innlögn á mánuði
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
			manAr = manudirIAr(i)
			if vt == 0:
				return "Þú þarft að spara í "+ str(manAr) + " til þess að ná uppí "+ str(heild) + " kr."
			else:
				return "Þú þarft að spara í "+ str(manAr) + " til þess að ná uppí "+ str(heild) + " kr. miðað við verðbólgu síðustu 15 ára"
		elif i == 12000:
			manAr = manudirIAr(i)
			return "Þú þarft að spara í "+ str(manAr) + " eða lengur. Reyndu að leggja meira fyrir."
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

## Fall sem skilar tíma sem það tekur að safna uppí ákveðna upphæð með eingreiðslu

## Notkun: timi = eingreidsla(L, nt, v, vt)
## Fyrir: L er mánaðaleg innlögn, v er ársvextir, vt er verðbólga og heild er upphæð sem notandi vill safna uppí.
## Eftir: timi er strengur sem segir notanda hversu lengi hann er að safna uppí tiltekna upphæð með tiltekinni eigreiðslu.
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
			manAr = manudirIAr(i)
			if vt == 0:
				return "Þú þarft að spara í " + str(manAr) + " til þess að ná uppí " + str(heild) + " kr."
			else:
				return "Þú þarft að spara í " + str(manAr) + " til þess að ná uppí " + str(heild) + " kr. miðað við verðbólgu síðustu 15 ára"
		elif i == 12000:
			manAr = manudirIAr(i)
			return "Þú þarft að spara í " + str(manAr) + " eða lengur. Reyndu að leggja meira fyrir."
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