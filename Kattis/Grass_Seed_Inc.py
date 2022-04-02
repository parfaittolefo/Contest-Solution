c=float(input())
n=int(input())
s=0
for i in range(n):
    l=input().split(" ")
    s+=float((float(l[0])*float(l[1]))*c)
    
print("{0:.7f}".format(s))