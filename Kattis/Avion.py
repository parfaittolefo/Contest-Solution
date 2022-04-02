l=[]
for i in range(5):
    s=input()
    if("FBI" in s):
        l.append(1+i)
if(len(l)==0):
    print("HE GOT AWAY!")
else:
    for i in l:
        print(i)