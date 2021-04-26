import turtle as t

t.reset()
t.title('Петухон — лучший язык программирования')

t.pd()
t.ht()


def cat():
    t.pu()
    t.goto(0, 50)
    t.pd()

    t.pensize(4)
    t.color('brown', 'yellow')

    t.begin_fill()
    t.goto(200, 50)
    t.goto(200, 0)
    t.goto(200, 50)
    t.goto(200, 250)
    t.goto(300, 150)
    t.goto(300, -50)
    t.goto(200, -150)
    t.goto(0, -150)
    t.goto(0, -100)
    t.goto(-50, -150)
    t.goto(-200, -150)
    t.goto(-100, -50)
    t.goto(-200, 50)
    t.goto(-200, 250)
    t.goto(-100, 150)
    t.goto(0, 250)
    t.goto(0, 50)
    t.end_fill()


def mouse():
    t.pu()
    t.goto(-100, 0)
    t.pd()

    t.pensize(4)
    t.color('black', 'gray')

    t.begin_fill()
    t.goto(-150, -50)
    t.goto(-150, 50)
    t.goto(-100, 50)
    t.goto(-100, 150)
    t.goto(-150, 150)
    t.goto(-250, 200)
    t.goto(-150, 250)
    t.goto(-100, 300)
    t.goto(-100, 350)
    t.goto(0, 450)
    t.goto(50, 450)
    t.goto(100, 400)
    t.goto(100, 300)
    t.goto(50, 250)
    t.goto(50, 150)
    t.goto(100, -50)
    t.goto(200, -50)
    t.goto(200, 200)
    t.goto(200, -50)
    t.goto(100, -50)
    t.goto(100, -150)
    t.goto(50, -200)
    t.goto(150, -200)
    t.goto(150, -300)
    t.goto(100, -300)
    t.goto(100, -250)
    t.goto(0, -250)
    t.goto(0, -200)
    t.goto(-100, -200)
    t.goto(-100, -300)
    t.goto(-200, -300)
    t.goto(-200, -250)
    t.goto(-150, -250)
    t.goto(-150, -150)
    t.goto(-100, -150)
    t.goto(-100, 0)
    t.end_fill()

    eye()


def eye():
    t.pu()
    t.goto(-100, 250)
    t.shape('circle')
    t.color('black')
    t.shapesize(1, 1, 1)
    t.stamp()


mouse()
t.exitonclick()
