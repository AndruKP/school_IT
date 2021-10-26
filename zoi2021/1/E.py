###### РАХУЄМО З ОДИНИЦІ
def calc(y, x, r_):
    if y > (m + 1) / 2:
        y_mir = m - y + 1
    else:
        y_mir = y
    if x > (n + 1) / 2:
        x_mir = n - x + 1
    else:
        x_mir = x
    #print(y_mir, x_mir)

    square_n = min(x_mir, y_mir)
    #print(square_n)

    n_mir = n - 2 * (square_n - 1)
    m_mir = m - 2 * (square_n - 1)

    x_min, x_max = square_n, n - square_n + 1
    y_min, y_max = square_n, m - square_n + 1

    P = 2 * (n_mir + m_mir - 2)
    r_ = r_ % P

    while r_ > 0:
        if x > x_min and y == y_min:
            if r_ >= x - x_min:
                r_ -= x - x_min
                x = x_min
            else:
                x = x - r_
                r_ = 0

        if x == x_min and y < y_max:
            if r_ >= y_max - y:
                r_ -= y_max - y
                y = y_max
            else:
                y = y + r_
                r_ = 0

        if x < x_max and y == y_max:
            if r_ >= x_max - x:
                r_ -= x_max - x
                x = x_max
            else:
                x = x + r_
                r_ = 0

        if x == x_max and y > y_min:
            if r_ >= y - y_min:
                r_ -= y - y_min
                y = y_min
            else:
                y = y - r_
                r_ = 0
    return (y, x)


m, n, r = map(int, input().split())

M = []
for _ in range(m):
    l = list(map(int, input().split()))
    M.append(l)

res = [[0 for i in range(n)] for i in range(m)]

for i, l in enumerate(M):
    for j, value in enumerate(l):
        y, x = calc(i + 1, j + 1, r)
        res[y-1][x-1] = value

for i in res:
    print(*i)
#print(calc(2, 2, 12))