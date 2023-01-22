s=input()
c=[]
for word in s.split():
    c.append(len(word))
print(*c)