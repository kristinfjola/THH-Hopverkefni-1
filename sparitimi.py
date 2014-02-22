# -*- coding: cp1252 -*-
## I thessu skjali er virknin fyrir tab 2. 

import math
globfjarmagns = 0
globvextir = 0

## Fall sem kallad er a ur vidmoti til thess a� fa upp hversu mikid tharf ad leggja inn til thess ad n� uppi tiltekna upphaed � tilteknum tima.
## sparitimi.innlogn(upphaed sem safna � uppi, vextir, ar, eingreidsla eda ekki (0 e�a 1))
def innlogn(heild, v, nt, manada):
	v = v/100.0
	nt = nt * 12
	if manada:
		return manadalegurSparInnlogn(nt, v, heild)
	else:
		return eingreidslaSparInnlogn(nt, v, heild)

## 0 = �ver�trygg�ur
## 1 = ver�trygg�ur
## Fall sem kallad er a ur vidmoti til thess ad fa upp hversu lengi tharf a� spara til �ess a� na uppi tiltekna upphaed thegar tiltekin upphaed er logd inn.
## sparitimi.timabil(Upphaed sem leggja a inn a manudi, vextir, upphaed sem safna a uppa, eingreidsla e�a ekki (0 e�a 1))
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
	return "�� �arft a� leggja inn " + str(int(1.0*heild/temp)) + " kr. � m�nu�i til �ess a� komast upp� " + str(heild) + " kr."


## Fall sem skilar hversu miki� �� �arft a� leggja inn � upphafi til �ess a� eiga �kve�na upph�� eftir eitthva� marga m�nu�i

##Notkun: innlogn = eingreidslaSparInnlogn(nt, v, heild)
##Fyrir: nt er timabil i arum, v er vextir a float formi (0.0X fyrir X prosent vexti) og heild er upphaed sem safna a uppi
##Eftir: innlogn er strengur sem segir notanda hversu miki� hann tharf ad leggja inn i upphafi
def eingreidslaSparInnlogn(nt, v, heild):
	innlogn = heild/(pow((1+v),(nt/12.0)))
	return "�� �arft a� leggja inn " + str(int(innlogn)) + " kr. � upphafi til �ess a� n� upp� " + str(heild) + " kr."


##Fall sem skiar manudum i manudum og arum

## Notkun: strengur = manudirIAr(tala)
## Fyrir: tala >= 0
## Eftir: strengur er tala skippt nidur � manudi og ar
def manudirIAr(tala):
	ar = tala / 12
	man = tala % 12
	if ar == 0:
		if man == 1:
			return str(man) + " m�nu�"
		else:	
			return str(man) + " m�nu�i"
	elif man == 0:
		return str(ar) + " �r"
	else:
		if man == 1:
			return str(ar) + " �r og " + str(man) + " m�nu�"
		else:	
			return str(ar) + " �r og " + str(man) + " m�nu�i"


## Timinn sem tekur a� spara upp� �kve�na upph��
## Falli� gerir r�� fyrir v�xtum greiddum �rlega, ver�b�lgu og �ar me� ver�b�tum greiddum m�na�alega ef reikningur er ver�trygg�ur og fj�rmagnstekjuskatti sem er dreginn fr� �rlega.
## Ekki � samr�mi vi� bankanetreikniv�lar �ar sem �ar eru vextir greiddir �t strax. (�essi a�fer� segir lengri t�ma)

## Notkun: timi = manadalegurSpar(L, v, vt, heild)
## Fyrir: L er m�na�aleg innl�gn, v er �rsvextir, vt er ver�b�lga og heild er upph�� sem notandi vill safna upp�.
## Eftir: timi er strengur sem segir notanda hversu lengi hann er a� safna upp� tiltekna upph�� me� tiltekinni innl�gn � m�nu�i
def manadalegurSparTimi(L, v, vt, heild):

	global globvextir
	global globfjarmagns

	fjarmagns = 0.8
	summa = 0
	stodur = [L]
	vextirAr = []
	verdbaeturAr = [] 
	for i in range(0,10000):
		
		## Ef summan er or�in h�rri en markmidsupphaed, tha skilum vid manudum
		if summa >= heild:
			manAr = manudirIAr(i)
			if vt == 0:
				return "�� �arft a� spara � "+ str(manAr) + " til �ess a� n� upp� "+ str(heild) + " kr."
			else:
				return "�� �arft a� spara � "+ str(manAr) + " til �ess a� n� upp� "+ str(heild) + " kr. mi�a� vi� ver�b�lgu s��ustu 15 �ra"
		elif i == 12000:
			manAr = manudirIAr(i)
			return "�� �arft a� spara � "+ str(manAr) + " e�a lengur. Reyndu a� leggja meira fyrir."
		
		summa = (summa + L)*(1+(vt/12))
		## B�tum � fylkin fyrir ver�b�tur og vextir 
		verdbaeturAr.append(summa*(vt/12))
		vextirAr.append(summa * v/12)
		if (i+1)%12 == 0 and i != 0:		
			stodur.append(int(math.ceil(summa + sum(vextirAr)*fjarmagns - sum(verdbaeturAr)*(1-fjarmagns))))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))

			## N�llstillum svo fylkin fyrir n�sta �r
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(math.ceil(summa))
	return "Virka�i ekki"

## Fall sem skilar t�ma sem �a� tekur a� safna upp� �kve�na upph�� me� eingrei�slu

## Notkun: timi = eingreidsla(L, nt, v, vt)
## Fyrir: L er m�na�aleg innl�gn, v er �rsvextir, vt er ver�b�lga og heild er upph�� sem notandi vill safna upp�.
## Eftir: timi er strengur sem segir notanda hversu lengi hann er a� safna upp� tiltekna upph�� me� tiltekinni eigrei�slu.
def eingreidslaSparTimi(L, v, vt, heild):
	global globvextir
	global globfjarmagns

	fjarmagns = 0.8
	summa = L
	stodur = [L]
	vextirAr = []
	verdbaeturAr = []

	for i in range(0, 10000):
		
		## Ef summan er or�in h�rri en markmidsupphaedin tha skilum vid manudunum
		if summa >= heild:
			manAr = manudirIAr(i)
			if vt == 0:
				return "�� �arft a� spara � " + str(manAr) + " til �ess a� n� upp� " + str(heild) + " kr."
			else:
				return "�� �arft a� spara � " + str(manAr) + " til �ess a� n� upp� " + str(heild) + " kr. mi�a� vi� ver�b�lgu s��ustu 15 �ra"
		elif i == 12000:
			manAr = manudirIAr(i)
			return "�� �arft a� spara � " + str(manAr) + " e�a lengur. Reyndu a� leggja meira fyrir."
		
		## B�tum � fylkin fyrir ver�b�tur og vexti
		summa = summa * (1+(vt/12))
		verdbaeturAr.append(summa*(vt/12))
		vextirAr.append(summa * (v/12))
		if (i+1)%12 == 0 and i != 0:
			stodur.append(int(math.ceil(summa + sum(vextirAr)*fjarmagns - sum(verdbaeturAr)*(1-fjarmagns))))
			summa = summa + sum(vextirAr)*fjarmagns - (sum(verdbaeturAr)*(1-fjarmagns))

			## N�llstillum svo fylkin fyrir n�sta �r
			vextirAr = []
			verdbaeturAr = []
		else:
			stodur.append(math.ceil(summa))		
	return "Virka�i ekki"
