def rev_ele(l):
    m=[]
    for i in l:
        n=i
        r=0
        while n>0:
            r=r*10+n%10
            n=n//10
        m.append(r)
    return m
n=int(input())
l=list(map(int, input().split()))
print(*rev_ele(l))