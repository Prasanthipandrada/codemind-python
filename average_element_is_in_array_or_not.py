n=int(input())
l=list(map(int, input().split()))
k=sum(l)
j=len(l)
m=k//j
if m in l:
    print("True")
else:
    print("False")