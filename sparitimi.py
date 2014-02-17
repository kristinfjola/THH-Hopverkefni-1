
import math
globfjarmagns = 0
globvextir = 0


#innlogn = upphaed/(1+vextir)^nt


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



"""
Notkun: tala = eingreidsla(L, nt, v, vt)
Fyrir:  
Eftir: 
"""
def eingreidslaSparTimi(L, v, vt, heild):
	global globvextir
	global globfjarmagns
	fjarmagn = 0.8
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