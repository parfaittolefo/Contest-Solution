n=int(input())
re={}
for i in range(n):
    eq=input().split()
    if(eq[0] not in re and len(re)<12):
        re[eq[0]]=eq[1]
for i in re:
    print(i+" "+re[i])