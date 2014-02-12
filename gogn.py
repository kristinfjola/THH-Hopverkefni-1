# -*- coding: cp1252 -*-


# nafn, vextir, bindistími, verðtrygging, lýsing
vaxtasproti = ['Vaxtasproti', 0.036, 0, 'óverðtryggður', 'lýsing']
overd12 = ['Óverðtryggður 12', 0.046, 12, 'óverðtryggður', 'lýsing']
overd18 = ['Óverðtryggður 18', 0.048, 18, 'óverðtryggður', 'lýsing']
overd24 = ['Óverðtryggður 24', 0.053, 24, 'óverðtryggður', 'lýsing']

verd36 = ['Verðtryggður 36', 0.0175, 36, 'verðtryggður', 'lýsing']
verd48 = ['Verðtryggður 48', 0.0185, 48, 'verðtryggður', 'lýsing']
verd60 = ['Verðtryggður 60', 0.0195, 60, 'verðtryggður', 'lýsing']

sparnadarleidir = [vaxtasproti, overd12, overd18, overd24, verd36, verd48, verd60]

# dæmi um lykkju til að fara i gegnum
for i in range(len(sparnadarleidir)):
    for j in range(len(sparnadarleidir[0])):
        print(sparnadarleidir[i][j])
        #if [i][2] == bindistimi:
            #'rétta leiðin'
            #sparnadarleidir[i][0] = nafnið á réttu leiðinni
