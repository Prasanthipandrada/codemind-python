n=int(input())
s=''
while n>0:
    r=n%10
    s=str(r)+s
    n=n//10
print(max(s))