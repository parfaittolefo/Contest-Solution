n=int(input())
l=input().split()
l=[float(i) for i in l]
pt=l[0]
pv=l[1]
ans=0
for i in range(n-1):
    l=input().split()
    l=[float(i) for i in l]
    ans+=((((l[1]+pv)*0.5)*(l[0]-pt))/1000)
    pt=l[0]
    pv=l[1]
print(ans)