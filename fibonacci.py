n=int(input())
s=0
f=0
se=1
for i in range(0, n):
    print(f,end=" ")
    s=s+f
    next=f+se
    f=se
    se=next
    
    