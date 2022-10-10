n=int(input())
l=list(map(int, input().split()))
k=set(l)
s=0
c=0
for i in k:
    if i!=0 and i%2==0:
        s=s+i
        c=c+1
print(s)