l=[]
for i in range(10):
	tmp=int(input())
	tmp=tmp%42
	if tmp not in l:
		l.append(tmp)

print(len(l))