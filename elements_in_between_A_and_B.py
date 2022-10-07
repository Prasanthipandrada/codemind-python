n=int(input())
l=list(map(int, input().split()))
a,b=map(int, input().split())
j=str(a)
k=str(b)
s=[]
c=0
for i in l:
    if i in range(a,b+1):
        s.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(*s)
        