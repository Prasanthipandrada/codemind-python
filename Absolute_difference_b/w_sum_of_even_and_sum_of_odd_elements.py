def esum(l):
    return sum([i for i in l if i%2==0])
def osum(l):
    return sum([i for i in l if i%2!=0])
n=int(input())
l=list(map(int, input().split()))
print(abs(osum(l)-esum(l)))