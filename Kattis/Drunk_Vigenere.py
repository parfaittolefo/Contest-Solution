c=input()
k=input()
cl=""
for i in range(len(k)):
    if i%2==0:
        de=ord(k[i])-65
        dc=ord(c[i])-65
        pt=((65)+(dc-de)%26)
        cl+=chr(pt)
    else:
        de=ord(k[i])-65
        dc=ord(c[i])-65
        pt=((65)+(dc+de)%26)
        cl+=chr(pt)  
print(cl)