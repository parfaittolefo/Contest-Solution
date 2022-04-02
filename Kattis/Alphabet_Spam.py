n=input()
lt=len(n)
esp=n.count("_")
lc=0
uc=0
for i in n:
    if(97<=ord(i)<=122):
        lc+=1
    elif(65<=ord(i)<=90):
        uc+=1
cb=lt-esp-uc-lc
print(str(esp/lt)+"\n"+str(lc/lt)+"\n"+str(uc/lt)+"\n"+str(cb/lt))