# -*- coding: cp1252 -*-


# nafn, vextir, bindist�mi, ver�trygging, l�sing
vaxtasproti = ['Vaxtasproti', 0.036, 0, '�ver�trygg�ur', 'Vaxtasproti er óbundinn sparnaðarreikningur sem hægt er að leggja inn á og taka út af hvenær sem er. Hann er óverðtryggður innlánsreikningur með 3,60% vexti.']
overd12 = ['Óverðtryggður 12', 0.046, 12, '�ver�trygg�ur', 'Bundinn óverðtryggður innlánsreikningur með 4,60% til 12 mánaða. Reikningurinn hentar vel fyrir reglulegan sparnað.']
overd18 = ['Óverðtryggður 18', 0.048, 18, '�ver�trygg�ur', 'Bundinn óverðtryggður innlánsreikningur með 4,80% vexti til 18 mánaða. Reikningurinn hentar vel fyrir reglulegan sparnað.					']
overd24 = ['Óverðtryggður 24', 0.053, 24, '�ver�trygg�ur', 'Bundinn óverðtryggður innlánsreikningur með 5,30% vexti til 24 mánaða. Reikningurinn hentar vel fyrir reglulegan sparnað.			']

verd36 = ['Verðtryggður 36', 0.0175, 36, 'ver�trygg�ur', 'Verðtryggður sparireikningur er góð lausn fyrir reglulegan sparnað og gefur góða ávöxtun. Hver innborgun er bundin í 36 mánuði. Eftir það er innborgunin laus til útborgunar í einn mánuð í senn á sex mánaða fresti. Vextirnir 1,75%, eru bókfærðir í árslok og þeir eru lausir til útborgunar eftir hverja vaxtafærslu.					']
verd48 = ['Verðtryggður 48', 0.0185, 48, 'ver�trygg�ur', 'Verðtryggður sparireikningur er góð lausn fyrir reglulegan sparnað og gefur góða ávöxtun. Hver innborgun er bundin í 48 mánuði. Eftir það er innborgunin laus til útborgunar í einn mánuð í senn á sex mánaða fresti. Vextirnir, 1,85%, eru bókfærðir í árslok og þeir eru lausir til útborgunar eftir hverja vaxtafærslu.					']
verd60 = ['Verðtryggður 60', 0.0195, 60, 'ver�trygg�ur', 'Verðtryggður sparireikningur er góð lausn fyrir reglulegan sparnað og gefur góða ávöxtun. Hver innborgun er bundin í 60 mánuði. Eftir það er innborgunin laus til útborgunar í einn mánuð í senn á sex mánaða fresti. Vextirnir, 1,95%, eru bókfærðir í árslok og þeir eru lausir til útborgunar eftir hverja vaxtafærslu.					']

sparnadarleidir = [vaxtasproti, overd12, overd18, overd24, verd36, verd48, verd60]

# d�mi um lykkju til a� fara i gegnum
for i in range(len(sparnadarleidir)):
    for j in range(len(sparnadarleidir[0])):
        print(sparnadarleidir[i][j])
        #if [i][2] == bindistimi:
            #'r�tta lei�in'
            #sparnadarleidir[i][0] = nafni� � r�ttu lei�inni
