from math import ceil, floor, sqrt

s = input()
s = s.replace(' ', '')
n = len(s)

row = floor(sqrt(n))
column = ceil(sqrt(n))

l1 = []
_ = 0
l_i = ''
for i in s:
    if _ < column:
        l_i = l_i + i
        _ += 1
    else:
        l1.append(l_i)
        _ = 1
        l_i = i
l1.append(l_i)

res = ['' for i in range(column)]
for i in l1:
    for ind in range(len(i)):
        res[ind] = res[ind] + i[ind]
print(*res)
