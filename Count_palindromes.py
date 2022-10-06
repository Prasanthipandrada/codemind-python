def rev_palin(l):
    c=0
    for i in l:
        t=i
        r=0
        while t>0:
            r=r*10+t%10
            t=t//10
        if r==i:
            c+=1
    return c
n=int(input())
l=list(map(int, input().split()))
print(rev_palin(l))