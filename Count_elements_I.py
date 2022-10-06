n,m=map(int, input().split())
l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
k=set(l1)
p=set(l2)
s1=[]
s2=[]
c=0
for i in k:
    if i in p:
        c+=1
        s1.append(i)
for j in p:
    if (j in k) and (j not in s1):
        c+=1
print(c)