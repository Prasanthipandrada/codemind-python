def e_p_sum(l):
    return l[0::2]
def o_p_sum(l):
    return l[1::2]
n=int(input())
l=list(map(int, (input().split())))
print(abs(sum(o_p_sum(l))-sum(e_p_sum(l))))