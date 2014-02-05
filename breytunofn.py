#LÁN

#lánsupphæðir
lan1_upph
lan2_upph
lan3_upph

#lánavextir

lan1_vextir
lan2_vextir
lan3_vextir

#greiðslubyrgði

lan1_greidslubyrgdi
lan2_greidslubyrgdi
lan3_greidslubyrgdi

#tímabil lána

lan1_timabil
lan2_timabil
lan3_timabil

#lán-verðtryggð/óverðtryggt

lan1_verdtrygging
lan2_verdtrygging
lan3_verdtrygging

gildið í breytunum er svo bara annaðhvort: 'Óverðtryggt' eða 'Verðtryggt'
getum breytt gildunum í 0 og 1 eða eitthvað sem við viljum ef það er betra

#jafnar greiðslur/jafnar afborganir

lan1_jafnar
lan2_jafnar
lan3_jafnar

setti gildið hérna sem: 0 ef Greiðslur, 1 ef Afborganir
líka hægt að hafa gildið hérna sem strengina 'Greiðslur' og 'Afborganir'

#------------------------------------------------------------#


#SPARNAÐUR

#l�navextir

#lengd tímabils sem umframgreiðsla er bundin
innist_bundin

#umframgreiðsla
umframgr
        	
#verðbólga (tímabil)
verdb
        	
#verðtryggð/óverðtryggð sparnaðarleið
verdSparn
        	

#grei�slubyrg�i


#l�n-ver�trygg�/�ver�tryggt







##Föll


#########################
##         Lán
#########################

# Óverðtryggt, jafnar afborganir, reiknað árlega
# Notkun: overdAfborganir(höfuðstóll, fjöldi ára, vextir(%))
def overdAfborganir(H, n, v):

# Verðtryggt, jafnar afborganir, verðbólga alltaf sú sama, reiknað árlega (er ennþá að vinna í þessu, ég gerði bara (vextir+verðbólga))
# Noktun: verdAfborganir(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))
def verdAfborganir(H, n, v, vb):

# Óverðtryggt, jafnar greiðslur, reiknað árlega
# Notkun: overdGreidslur(höfuðstóll, fjöldi ára, vextir(%))
def overdGreidslur(H, n, v):

# Verðtryggt, jafnar greiðslur, verðbólga alltaf sú sama, reiknað árlega (er í lagi ef eyjan.is	er ok)
# Notkun: verdGreidslur(höfuðstóll, fjöldi ára, vextir(%), verðbólga(%))	
def verdGreidslur(H, n, v, vb):






#########################
##     Sparnaður
#########################

"""Ef vextir eru borgaðir mánaðalega"""
#Óverðtryggður, vextir greiddir mánaðalega
#Notkun: overdtryggtMan(Lagt fyrir á mán, fjöldi mánaða, vextir)
def overdtryggtMan(L, nt, v):


#Verðtryggður, vextir og verðbætur borgaðar mánaðalega (verðbólga sú sama allt árið)
#Notkun: verdtryggtMan(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
def verdtryggtMan(L, nt, v, vb):



"""Ef vextir eru borgaðir í árslok"""
#Óverðtryggður, vextir borgaðir 31.des
#Notkun: overdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir)
def overdtryggtArs(L, nt, v):


#Verðtryggður, vextir og verðbætur borgaðar 31.des (verðbólga sú sama út allt árið)
#Notkun: verdtryggtArs(Lagt fyrir á mán, fjöldi mánaða, vextir, verðbólga/bætur)
def verdtryggtArs(L, nt, v, vb):
