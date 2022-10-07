n=int(input())
l=list(map(int, input().split()))
a,b=map(int, input().split())
j=str(a)
k=str(b)
s=0
for i in l:
    if i in range(a,b+1):
        s=s+i
if s!=0:
    print(s)
else:
    print("0")
    
        
        