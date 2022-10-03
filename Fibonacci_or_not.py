n=int(input())
s=0
f=0
se=1
flag=0
for i in range(n):
    s=s+f
    next=f+se
    f=se
    se=next
    if next==n:
        flag+=1
if flag==1:
    print("True")
else:
    print("False")
    