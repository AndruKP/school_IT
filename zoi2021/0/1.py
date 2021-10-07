from math import gcd

res=0
for a in range(1,2001):
    for b in range(1,2001):
        if a*b//gcd(a,b)==2000:
            res+=1
            print(a,b)
print(res)