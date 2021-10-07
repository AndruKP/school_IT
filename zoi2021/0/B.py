x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

res = [0, 0]

if x1 == x2:
    res[0] = x3
elif x1 == x3:
    res[0] = x2
else:
    res[0] = x1

if y1 == y2:
    res[1] = y3
elif y1 == y3:
    res[1] = y2
else:
    res[1] = y1
print(*res)
