n=int(input())
vmx=0
l=input().split()
pt=int(l[0])
pd=int(l[1])
for i in range(n-1):
    l=input().split()
    v=(int(l[1])-pd)/(int(l[0])-pt)
    pd=int(l[1])
    pt=int(l[0])
    if(v>vmx):
        vmx=v
print(int(vmx))