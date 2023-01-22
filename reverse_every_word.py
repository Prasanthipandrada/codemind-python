s=input()
c=[]
for word in s.split():
    c.append(word[::-1])
print(*c)