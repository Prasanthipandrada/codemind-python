n=int(input())
m=str(n)
k=m[::-1]
l=int(k)
s=n**2
p=str(l**2)[::-1]
#print(s,p)
if s==int(p):
    print("True")
else:
    print("False")