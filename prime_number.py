def prime(n):
    c=0
    op=''
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        op="prime"
    else:
        op="not a prime"
    return op
n=int(input())
res=prime(n)
print(res)