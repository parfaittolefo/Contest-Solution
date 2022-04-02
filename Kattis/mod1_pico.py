l=[54,396,131,198,225,258,87,258,128,211,57,235,114,258,144,220,39,175,330,338,297,288]
flag=""
for i in l:
    mod=i%37
    
    if(0<=mod<=25):
        flag+=chr(65+mod).lower()
    if(26<=mod<=35):
        flag+=str((mod-26))
    elif(mod==36):
        flag+='_'
print("picoCTF{"+flag+"}")
    