i,r,k=map(int, input().split())
c=0
for i in range(i,r+1):
    if i%k==0:
        c=c+1
print(c)