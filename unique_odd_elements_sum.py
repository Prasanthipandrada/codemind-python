n=int(input())
l=list(map(int, input().split()))
k=set(l)
s=0
for i in k:
    if i%2!=0:
        s=s+i
print(s)