n=int(input())
temp=n
s=str(n)
if n>0:
    print(int(s[::-1]))
else:
    n=abs(n)
    s=str(n)
    a=int(s[::-1])
    print(-a)


