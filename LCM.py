a,b=map(int, input().split())
k=max(a,b)
i=1
while True:
    m=k*i
    if m%a==0 and m%b==0:
        print(m)
        break
    i+=1