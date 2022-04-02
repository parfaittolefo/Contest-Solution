
def conv(n,b):
    n=int(n)
    s=[]
    while(n!=0):
        s.append(str((n%b)))
        n=n//b
    return s

re=[]
n=int(input())
for i in range(n):
    l=input().split(" ")
    s=conv(l[2],int(l[1]))
    p=0
    for j in s:
        p+=int(j)**2
    re.append(p)
for i in range(len(re)):
    print(str(i+1)+" "+str(re[i]))
    
    
    