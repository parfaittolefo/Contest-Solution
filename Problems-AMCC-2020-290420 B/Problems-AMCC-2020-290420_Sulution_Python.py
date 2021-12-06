import sys
listeElect=[]
"""AUTOR: Parfait TOELFO 
   email: parfaittolefo23@gmail.com
   Tel: +229 61474698 
        +229 52422809
"""
class Election:
    def __init__(self,nbrCand,nbrRes):
        self.nbrCand=nbrCand
        self.nbrRes=nbrRes
        listeResultat=[]
        self.listeResultat=listeResultat
    
    def enregistrement(self):
        listeCandi=[]
        for i in range(nbrCand):
            nom=input()
            listeCandi.append(nom)
        for i in range(nbrRes):
            UnResultat=input()
            UnResultat=UnResultat.split(" ")
            nom=UnResultat[0]
            score=int(UnResultat[1])
            lieu=(UnResultat[2])
            Res=Resultat(nom,score,lieu)
            self.listeResultat.append(Res)           
    
class Resultat:
    
    def __init__(self,nom,score,point):
        self.nom=nom
        self.score=score
        self.point=point

nbrElect=int(input())

for compt in range(nbrElect):
    entre1=input()
    entre1=entre1.split(" ")
    nbrCand=int(entre1[0])
    nbrRes=int(entre1[1])
    Elect=Election(nbrCand,nbrRes)
    Elect.enregistrement()
    listeElect.append(Elect)

FortP=0
i=0
for Elect in listeElect:
    Fort=''
    FortR=0
    l=0
    nomF=''
    listV=[""]
    
    k=Elect.nbrRes
    Res=Elect.listeResultat

    for j in range(k):
        nomp=Res[j].nom
        for l in range(k):
            nom=Res[l].nom
            if(nom==nomp and nomp not in listV):
                FortP+=Res[l].score
                nomF=nomp
        listV.append(nomp)
        
            
        if(FortP>FortR):
            Fort=f"VOTE {i+1}: THE WINNER IS {nomF} {FortP}"
        if(FortP==FortR):
            Fort=f"VOTE {i+1}:THERE IS A DILEMMA "
        if(FortP>FortR):
            FortR=FortP
        FortP=0
    print(Fort)
    i+=1
    
    FortP=0 
    FortR=0
    Fort=''
