l=input().split()
Nbr=int(l[0])
NbrD=int(l[1])
l=[]
fin=1
for i in range(NbrD):
    tmp=input()
    if(tmp not in l):
        l.append(tmp)
    if(len(l)!=Nbr):
        fin+=1
if(len(l)==Nbr):
    print(fin)
else:
    print("paradox avoided")
