Ch1=input()
Ch2=input()
cmpt=0

for i in range(4):
    if Ch1[i]!=Ch2[i]:
        cmpt+=1
print(2**cmpt)