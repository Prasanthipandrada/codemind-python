n,m=map(int, input().split())
l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
k=set(l1)
m=set(l2)
c=0
for i in k:
    if i not in m:
        c+=1
for j in m:
    if j not in k:
        c+=1
print(c)