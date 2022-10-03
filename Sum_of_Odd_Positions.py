def solve(l):
    return l[1::2]
n=int(input())
l=list(map(int, input().split()))
print(sum(solve(l)))