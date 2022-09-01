def positive_integer(n):
    s=0
    op=''
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        op=True
    else:
        op=False
    return op
n=int(input())
res=positive_integer(n)
print(res)