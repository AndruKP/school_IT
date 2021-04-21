import turtle as t

t.reset()
t.title('Петухон - лучший язык программирования')

t.pu()
t.ht()


def turtle():
    t.shape('turtle')
    t.color('yellow', 'green')

    for i in range(1, 4):
        t.shapesize(9 - 2 * i, 9 - 2 * i, 2)
        t.stamp()


def squares():
    t.shape('square')
    t.shapesize(6, 6, 2)
    t.color('red', 'teal')
    t.stamp()

    t.shape('circle')
    t.color('red', 'white')
    t.stamp()

    t.shape('square')
    t.shapesize(4, 4, 2)
    t.color('red', 'teal')
    t.stamp()


def triangles():
    #t.lt(90)
    t.shape('triangle')
    t.color('blue', 'light blue')
    for i in range(5):
        t.shapesize(6 - i, 6 - i, 2)
        t.stamp()


def arrows():
    t.lt(90)
    t.shape('arrow')
    t.color('red', 'misty rose')
    for i in range(5):
        t.shapesize(6 - i, 6 - i, 2)
        t.stamp()


def square():
    t.shape('square')
    t.color('green', 'light green')
    for i in range(3):
        t.shapesize(6 - 2 * i, 6 - 2 * i, 2)
        t.stamp()


def rainbow():
    t.shape('circle')

    t.color('red')
    t.shapesize(7, 7, 2)
    t.stamp()

    t.color('orange')
    t.shapesize(6, 6, 2)
    t.stamp()

    t.color('yellow')
    t.shapesize(5, 5, 2)
    t.stamp()

    t.color('green')
    t.shapesize(4, 4, 2)
    t.stamp()

    t.color('blue')
    t.shapesize(3, 3, 2)
    t.stamp()

    t.color('dark blue')
    t.shapesize(2, 2, 2)
    t.stamp()

    t.color('purple')
    t.shapesize(1, 1, 2)
    t.stamp()


rainbow()
t.setpos(-300,0)
square()
t.setpos(0,200)
arrows()
t.setpos(-150,200)
triangles()
t.setpos(-150,0)
turtle()
t.setpos(-300,200)
squares()
t.exitonclick()
