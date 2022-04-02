n=input().split("-")
n=''.join(n)
n=[int(i) for i in n]
s=4*n[0]+3*n[1]+2*n[2]+7*n[3]+6*n[4]+5*n[5]+4*n[6]+3*n[7]+2*n[8]+n[9]
if s%11==0:
    print(1)
else:
    print(0)