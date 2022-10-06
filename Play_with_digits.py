def sum_ele(l):
    s=0
    for i in l:
        n=i
        while n>0:
            r=n%10
            s=s+r
            n=n//10
    return s
n=int(input())
l=list(map(int, input().split()))
print(sum_ele(l))