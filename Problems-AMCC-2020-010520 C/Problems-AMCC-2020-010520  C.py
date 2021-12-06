"""AUTOR: TOLEFO Parfait
   email: parfaittolefo23@gmail.com
   Tel:+229 61474698/ +229 52422809
"""  

Tests=int(input())
Resultats=[]

for i in range(Tests):
    depenseProchaine=int(input())
    quotatRestant=int(input())
    if (quotatRestant!=0 )and (depenseProchaine> quotatRestant+60):
        montant=((quotatRestant+60)*1500)+((depenseProchaine-quotatRestant-60)*3000)
        Resultats.append(montant)
    elif(quotatRestant!=0) and (depenseProchaine<=quotatRestant+60):
        montant=depenseProchaine*1500
    elif(quotatRestant==0 )and( depenseProchaine>60):
        montant=(depenseProchaine-60)*300+60*1500
        Resultats.append(montant)
    elif(quotatRestant==0 )and (depenseProchaine<=60):
        montant=depenseProchaine*1500
        Resultats.append(montant)
for i in Resultats:
    print(i)
