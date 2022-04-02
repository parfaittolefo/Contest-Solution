l1=input().split(" ")
obs=int(l1[1])
l2=[]
for i in range(obs):
    t=input()
    if(t not in l2):
        l2.append(t)

for i in range(int(l1[0])):
    if(str(i)) not in l2:
        print(i)

print("Mario got "+str(len(l2))+" of the dangerous obstacles.")