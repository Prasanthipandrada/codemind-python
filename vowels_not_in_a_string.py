s=input()
v="aeiou"
c=[]
for i in v:
    if i not in s:
        c.append(i)
if len(v)==5 and len(c)==0:
    print("0")
else:
    print(*c)
    