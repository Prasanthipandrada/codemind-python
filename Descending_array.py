def des_ary(l):
    s=999
    flag=0
    for i in l:
        if s>i:
            s=i
        else:
            flag+=1
    return flag
n=int(input())
l=list(map(int, input().split()))
res=des_ary(l)
if res==0:
    print("yes")
else:
    print("no")
            