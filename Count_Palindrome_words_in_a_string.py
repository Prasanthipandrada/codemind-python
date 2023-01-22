s=input()
p=s.casefold()
c=0
for word in p.split():
    if word==word[::-1]:
        c+=1
print(c)