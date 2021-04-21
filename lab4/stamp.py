import turtle as t

t.reset()
t.title('Петухон - лучший язык программирования')

t.pd()
t.st()


def move():
    t.lt(90)
    t.shape('turtle')
    t.color('yellow', 'green')

    for i in range(1, 4):
        t.shapesize(9-2*i, 9 - 2*i, 2)
        t.stamp()


move()
t.exitonclick()
