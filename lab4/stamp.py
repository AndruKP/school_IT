import turtle as t

t.reset()
t.title('Петухон - лучший язык программирования')

t.pd()
t.st()


def turtle():
    t.lt(90)
    t.shape('turtle')
    t.color('yellow', 'green')

    for i in range(1, 4):
        t.shapesize(9 - 2 * i, 9 - 2 * i, 2)
        t.stamp()


def squares():
    t.fd(100)
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


turtle()
t.pu()
t.fd(100)
squares()
t.exitonclick()
