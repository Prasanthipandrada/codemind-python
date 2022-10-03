def e_sum(l):
    return sum([i for i in l if i%2==0])
n=int(input())
l=list(map(int, input().split()))
print(e_sum(l))