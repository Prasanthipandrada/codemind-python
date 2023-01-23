s=input()
c=0
for i in s:
    if i.islower()==False and i.isupper()==False and i.isdigit()==False and i.isspace()==False:
        c+=1
print(c)