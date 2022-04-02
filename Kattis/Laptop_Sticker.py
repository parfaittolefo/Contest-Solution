l=input().split()
l=[int(i) for i in l]
if(l[0]>l[2]+1):
    if(l[1]>l[3]+1):
        print(1)
    else:
        print(0)
else:
    print(0)