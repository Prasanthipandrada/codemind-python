n=int(input())
l=list(map(int, input().split()))
k=int(input())
s=''
c=0
m=[]
for i in l:
    s=s+str(i)
for i in s:
    c=s.count(i)
    if c==k:
        if i not in m:
            m.append(i)
if m==[]:
    print("-1")
else:
    print(*m)