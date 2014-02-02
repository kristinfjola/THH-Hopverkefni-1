#Formúlur fyrir 1 mánuð

		#Formúla fyrir vertryggt lán





		#Formúla fyrir óverðtryggt lán
		#Dæmi
		int nidurstada = hofudstoll * vextir + ......;




		#Formúla fyrir verðtryggðan 



#Formúlur fyrir 1 ár

		#Formúla fyrir verðtryggt lán



		#.............
		


		
#------------------------------------------------------------------------------------------------

#Jóhanna:

#H - höfuðstóll
#n - fjöldi tímabila
#v - vextir (%)
#vb - verðbólga
#greidsla - greiðsla (hvað hann er að greiða þetta tímabil)
#vextir - kostnaður sem fer í vexti
#afb - afborgun - FASTI
#eftirs - eftirstaða (hversu mikið að láninu er eftir)
#summa - heildarkostnaðurinn sem hann er búinn að borga


#óverðtryggt - jafnar afborganir:
def bla(H, n, v):
	afb = H/n
	def asdf(greidsla, eftirs, summa):
		if (eftirs == 0):
			print summa
		else:
			asdf(afb + v*eftirs, eftirs - afb, summa + (afb + v*eftirs))
			#greidsla = afb + v*eftirs
			#eftirs = eftirs - afb
			#summa = summa + greidsla
	asdf(0, H, 0)


#verðtryggt - jafnar afborganir:
def bla(H, n, v, vb):
	afb = H/n
	def asdf(greidsla, eftirs, summa):
		if (eftirs == 0):
			print summa
		else:
			asdf(afb + (v+vb)*eftirs, eftirs - afb, summa + (afb + (v+vb)*eftirs))
			#greidsla = afb + (v+vb)*eftirs
			#eftirs = eftirs - afb
			#summa = summa + greidsla
	asdf(0, H, 0)

	
#---------------------------------------------------------------


#H - höfuðstóll
#n - fjöldi tímabila
#v - vextir (%)
#vb - verðbólga
#greidsla - greiðsla (hvað hann er að greiða þetta tímabil) - FASTI
#vextir - kostnaður sem fer í vexti
#afb - afborgun
#eftirs - eftirstaða (hversu mikið að láninu er eftir)
#summa - heildarkostnaðurinn sem hann er búinn að borga

#ATH annaðhvort þarf að vera math.ceil fyrir A (ekki alveg rétt niðurstaða) eða gera if (eftirs < 1) (sem er ekki heldur alveg rétt)

#óverðtryggt - jafnar greiðslur:
def bla(H, n, v):
	import math
	A = H*((v*(1+v)**n)/(((1+v)**n)-1))	#Jafna til að finna greiðslu
	greidsla = math.ceil(A) #námunda upp
	def asdf(vextir, afb, eftirs, summa):
		if(eftirs <= 0):
			print summa
		else:
			asdf(v*eftirs, greidsla - v*eftirs, eftirs - (greidsla - v*eftirs), summa + greidsla)
			#vextir = v*eftirs
			#afb = greidsla - vextir
			#eftirs = eftirs - afb
			#summa = summa + greidsla
	asdf(0, 0, H, 0)


#verðtryggt - jafnar greiðslur:
def bla(H, n, v, vb):
	import math
	A = H*((v*(1+v)**n)/(((1+v)**n)-1))
	greidsla = math.ceil(A) #námunda upp
	def asdf(vextir, afb, eftirs, summa):
		if(eftirs <= 0):
			print summa
		else:
			asdf((v+vb)*eftirs, greidsla - (v+vb)*eftirs, eftirs - (greidsla - (v+vb)*eftirs), summa + greidsla)
			#vextir = (v+vb)*eftirs
			#afb = greidsla - vextir
			#eftirs = eftirs - afb
			#summa = summa + greidsla	
	asdf(0, 0, H, 0)
