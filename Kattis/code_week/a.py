n=int(input()) 
l=["A"]
for i in range(n):
	cA=l.count("A")
	cB=l.count("B")
	l.clear()
	for i in range(cA):
		l.append("B")   
	for i in range(cB):
		l.append("B")
		l.append("A")
cA=l.count("A")
cB=l.count("B")
print(cA," ",cB,end="")