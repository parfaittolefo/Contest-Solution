n=int(input())
ch1=input().split(" ")
ch2=input().split(" ")
for i in ch1:
    if(i not in ch2):
        print(i)