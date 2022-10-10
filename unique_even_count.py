n=int(input())
l=list(map(int, input().split()))
k=set(l)
c=0
s=[]
for i in k:
    if i!=0 and i%2==0:
        c+=1
print(c)