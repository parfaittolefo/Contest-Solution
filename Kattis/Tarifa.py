t=int(input())
n=int(input())
d=t*(n+1)
s=0
for i in range(n):
    s+=int(input())
print(d-s)