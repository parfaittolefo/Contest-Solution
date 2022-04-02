from math import cos,sin,pi
n=int(input())
l=[]
for i in range(n):
    ch=input().split()
    ch=[float(j) for j in ch]
    t=ch[2]/(ch[0]*cos((ch[1]*pi)/180))
    y=(ch[0]*t*sin((ch[1]*pi)/180))-0.5*(9.81*t**2)
    
    if(y-1>=ch[3] and y+1<=ch[4]):
        l.append("Safe")
    else:
        l.append("Not Safe")
for i in l:
    print(i)
    