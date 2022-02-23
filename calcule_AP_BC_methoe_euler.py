def main():
    Lines=[]
    X0=5
    Y0=2
    Tr=int(input())
    OutTable=[]
    for i in range(Tr):
       Lines.append(input().split(" "))
    compt=0
    for Line in Lines:
        Line[0]=float(Line[0])
        Line[1]=float(Line[1])
        i=1; Xi=0; Xn=[]
        Xn.append(X0)

        while(Xi != Line[1]):
            Xi=X0+(Line[0]*i)
            Xn.append(Xi)
            i+=1
        Yp=Y0; Yn=[]; Yj=0; j=1 
        Yn.append(Yp)

        while(j<i):
            Yj=Yp+(Line[0]*((Xn[j-1]**Y0)-(6*(Yp*Yp))))
            Yn.append(Yj)
            Yp=Yj
            j+=1
        Out=str(round(Yn[len(Yn)-1],1))
        if "." not in Out:
            Out+=".0"
        OutTable.append(Out)
    for i in range(len(OutTable)):
        if(i==len(OutTable)-1):
            print(OutTable[i].strip(),end="")
        else:
            print(OutTable[i].strip())
main()

