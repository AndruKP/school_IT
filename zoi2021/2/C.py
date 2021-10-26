n, k =map(int,input().split())
l = list(map(lambda x: int(x)%k,input().split()))

rem = []
for i in range(k):
    rem.append(l.count(i))

pair = []
for i in range(1,k//2+1):
    pair.append([rem[i],rem[k-i]])

res = 0

for i in pair[:-1]:
    res+=max(i)

if k%2:
    res+=max(pair[-1])

else:
    if pair[-1][0]>0:
        res+=1
if rem[0]>0:
    res+=1

print(res)
