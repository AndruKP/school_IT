###### РАХУЄМО З ОДИНИЦІ
def calc(y,x,r):
    if y>(m+1)/2:
        y_mir = m-y + 1
    else:
        y_mir = y
    if x>(n+1)/2:
        x_mir = n-x + 1
    else:
        x_mir = x
    print(y_mir,x_mir)    

    square_n = min(x_mir,y_mir)
    print(square_n)

    n_mir = n-2*(square_n-1)
    m_mir = m-2*(square_n-1)

    x_min,x_max = square_n, n-square_n+1
    y_min,y_max = square_n, m-square_n+1

    P = 2*(n_mir+m_mir)
    r = r%P

    while r>0:
        if x>x_min and y==y_min:
            if r>=x-x_min:
                r-=x-x_min
                x=x_min
            else:
                x = x-r
                r = 0

        if x==x_min and y<y_max:
            if r>=y_max-y:
                r-= y_max-y
                y = y_max
            else:
                y = y+r
                r = 0

        if x<x_max and y==y_max:
            if r>=x_max-x:
                r-=x_max-x
                x=x_max
            else:
                x = x+r
                r = 0

        if x==x_max and y>y_min:
            if r>=y-y_min:
                r-= y-y_min
                y = y_min 
            else:
                y = y-r
                r = 0
    print(y,x)
m = 6
n = 7

calc(1,7,13)