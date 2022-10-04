t=int(input())
for i in range(t):
    n,a,b,k=map(int, input().split())
    s1=0
    s2=0
    if n//a>=k or n//b>=k or n//a+n//b>=k:
        print("Win")
    else:
        print("Lose")