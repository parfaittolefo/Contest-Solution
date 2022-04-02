n=int(input())

def hash(n)-> bool:
    s=0
    for i in str(n):
        s+=int(i)
    if(int(n)%s==0):
        return True
    else: return False
    
while True:
    if(hash(n)):
        print(n)
        break
    else:
        n+=1