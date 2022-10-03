def find(num):
    return sum([i for i in num if i%2!=0])
n =int(input())
num=list(map(int, input().split()))
print(find(num))