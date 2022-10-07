from math import ceil
n=int(input())
l=list(map(int, input().split()))
k=len(l)
s1=[]
s2=[]
for i in l:
    if i in range(1,(k//2)+1):
        s1.append(i)
    else:
        s2.append(i)
print(abs(sum(s1)-sum(s2))) 