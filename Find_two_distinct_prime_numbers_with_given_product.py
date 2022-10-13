n=int(input())
c=0
s=[]
for i in range(2,(n//2)+1):
    if n%i==0:
        c=c+1
        s.append(i)
        if c==2:
            break
if c!=0:
    print(*s)
else:
    print("-1")