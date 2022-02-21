def main():
  D={"T":1.5,"O":1.25,"P":3.50,"M":3.75,"A":0.40}
  chs=[]
  for i in range(7):
    ch=input()
    chs.append(ch)
  Re=[]
  for ch in chs:
    Prix=15
    L=[]
    for i in ch:
       if(i in D and i not in L):
          Prix+=D[i]
          L.append(i)
    if( Prix>20):
        Prix-=Prix*0.05
        Prix=round(Prix,2)
    if(len(str(Prix))<5 and len(str(Prix))>3 ):
        Re.append((str(Prix)+"0").strip())
    elif(len(str(Prix))==2):
        Re.append((str(Prix)+".00").strip())
    else:
        Re.append(str(Prix).strip())  
  for i in range(len(chs)):
    if i ==len(chs)-1:
      print(Re[i],end="")
    else:
      print(Re[i])
         
main()   
