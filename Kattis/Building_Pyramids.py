n=int(input())
i=0
t=1
while n>=t**2:
        n=n-t**2
        t+=2
        i+=1
print(i)