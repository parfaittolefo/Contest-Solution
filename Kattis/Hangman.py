
word=list(input())
lst=list(input())
lose=0
for i in range(len(lst)):
    if(len(word)!=0):
        if(lst[i] in word):
            word=[j for j in word if j!=lst[i]]
        else:
            lose+=1
    else:
        break
if(lose<10):
    print("WIN")
else:
    print("LOSE")