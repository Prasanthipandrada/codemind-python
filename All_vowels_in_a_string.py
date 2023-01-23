s=input()
up='AEIOU'
lo="aeiou"
flag=0
flag2=0
for i in up:
    if i not in s:
        flag+=1
for j in lo:
    if j not in s:
        flag2+=1
if flag==0 or flag2==0:
    print("True")
else:
    print("False")