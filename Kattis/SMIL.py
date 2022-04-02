l=[]
ch=input()

for i in range(len(ch)+3):
    try:
        if(ch[i:i+3] in [":)", ";)", ":-)", ";-)"] or ch[i:i+2] in [":)", ";)", ":-)", ";-)"] ):
            l.append(i)
    except:
        pass
for i in l:
    print(i)
    
        
        

