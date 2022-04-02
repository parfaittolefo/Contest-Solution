n=input()
n+="$"
new=[]
for i in range(len(n)):
    try:
        if(n[i]!=n[i+1]):
            new.append(n[i])
    except:
        pass
new=''.join(new)
print(new)