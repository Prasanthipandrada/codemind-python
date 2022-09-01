def abundant_number(n):
    s=0
    op=''
    for i in range(1,n,1):
        if n%i==0:
            s=s+i
    if s>n:
        op=True
    else:
        op=False
    return op
n=int(input())
res=abundant_number(n)
print(res)
            