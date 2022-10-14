n=int(input())
a=n
while True:
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if a%i==0:
            is_prime=False
            break
    if is_prime==True:
        break
    else:
        a+=1
b=n
while True:
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if b%i==0:
            is_prime=False
            break
    if is_prime==True:
        break
    else:
        b-=1
s1=a-n
s2=n-b
if s1>s2:
    print(s2)
else:
    print(s1)