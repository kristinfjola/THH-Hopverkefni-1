# -*- coding: cp1252 -*-


# nafn, vextir, bindist�mi, ver�trygging, l�sing
vaxtasproti = ['Vaxtasproti', 0.036, 0, '�ver�trygg�ur', 'l�sing']
overd12 = ['�ver�trygg�ur 12', 0.046, 12, '�ver�trygg�ur', 'l�sing']
overd18 = ['�ver�trygg�ur 18', 0.048, 18, '�ver�trygg�ur', 'l�sing']
overd24 = ['�ver�trygg�ur 24', 0.053, 24, '�ver�trygg�ur', 'l�sing']

verd36 = ['Ver�trygg�ur 36', 0.0175, 36, 'ver�trygg�ur', 'l�sing']
verd48 = ['Ver�trygg�ur 48', 0.0185, 48, 'ver�trygg�ur', 'l�sing']
verd60 = ['Ver�trygg�ur 60', 0.0195, 60, 'ver�trygg�ur', 'l�sing']

sparnadarleidir = [vaxtasproti, overd12, overd18, overd24, verd36, verd48, verd60]

# d�mi um lykkju til a� fara i gegnum
for i in range(len(sparnadarleidir)):
    for j in range(len(sparnadarleidir[0])):
        print(sparnadarleidir[i][j])
        #if [i][2] == bindistimi:
            #'r�tta lei�in'
            #sparnadarleidir[i][0] = nafni� � r�ttu lei�inni
