def find_hcf(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1, small+1):
        if((x%i==0) and (y%i==0)):
            hef=i
    return hef
x,y=map(int, input().split())
print(find_hcf(x,y))