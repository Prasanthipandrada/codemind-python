s1=input()
s2=input()
sum1=0
sum2=0
for i in s1: 
    sum1+=ord(i)
for j in s2:
    sum2+=ord(j)
if sum1==sum2:
    print("True")
else:
    print("False")
    