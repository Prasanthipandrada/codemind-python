def ase_ary(l):
    s=0
    flag=0
    for i in l:
        if i>s:
            s=i
        else:
            flag+=1
    return flag
n=int(input())
l=list(map(int, input().split()))
res=ase_ary(l)
if res==0:
    print("yes")
else:
    print("no")