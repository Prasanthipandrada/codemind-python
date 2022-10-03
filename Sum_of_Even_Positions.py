def solve(l):
    return l[0::2]
n=int(input())
l=list(map(int, input().split()))
print(sum(solve(l)))
        
    