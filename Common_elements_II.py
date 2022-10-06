n,m=map(int, input().split())
l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
s1=set(l1)
s2=set(l2)
k=[]
for i in l1:
    if i not in l2:
        k.append(i)
for j in l2:
    if j not in l1:
        k.append(j)
print(*k)