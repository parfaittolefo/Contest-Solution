l=[268,413,110,190,426,419,108,229,310,379,323,373,385,236,92,96,169,321,284,185,154,137,186]

flag=""
for i in l:
    modInv=pow(i,-1,41)
    
    if(1<=modInv<=26):
        flag+=chr(65+modInv-1).lower()
    if(27<=modInv<=36):
        flag+=str((modInv-27))
    elif(modInv==37):
        flag+='_'
print("picoCTF{"+flag+"}")



.-- .... ....- --... .... ....- --... .... ----. ----- -.. .-- ..--- ----- ..- ----. .... --...

WH47_H47H_90D_W20U9H7