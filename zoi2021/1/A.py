b, w = map(int, input().split())
x, y, z = map(int, input().split())

if x > y + z:
    res = w * y + b * (y + z)
elif y > x + z:
    res = b * x + w * (x + z)
else:
    res = b*x + w*y
print(res)