l=input().split()
a=int(l[0])
b=int(l[1])
a1=min(a,b)
b1=max(a,b)
for i in range(a1,b1+1):
    print(i+1)