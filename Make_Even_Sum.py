n=int(input())
arr=list(map(int, input().strip().split()))
k=sum(arr)
j=int(k)
if j%2==0:
    print("1")
else:
    print("0")