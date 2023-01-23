s=input()
c=[]
for i in s:
    if i.isspace()==True:
        continue
    else:
        c.append(i)
print(len(c))