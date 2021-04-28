import turtle as t

t.reset()
t.title('Петухон — лучший язык программирования')
t.setup(1920, 1080, 0, 0)

t.pd()
t.ht()


def worm():
    t.pensize(3)
    t.color('black', 'green')

    t.pu()
    t.goto(-400, 100)
    t.pd()

    t.begin_fill()
    t.circle(-100)
    t.end_fill()

    t.pu()
    t.goto(-250, 25)
    t.pd()

    t.begin_fill()
    t.circle(-100)
    t.end_fill()

    t.pu()
    t.goto(-50, 0)
    t.pd()

    t.begin_fill()
    t.circle(-100)
    t.end_fill()

    t.pu()
    t.goto(100, -125)
    t.pd()

    t.begin_fill()
    t.circle(-100)
    t.end_fill()

    t.pu()
    t.goto(250, -200)
    t.pd()

    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.pu()
    t.goto(350, -25)
    t.pd()

    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.pu()
    t.goto(300, 50)
    t.pd()

    t.color('red')
    t.goto(350, 25)
    t.goto(400, 50)

    t.pu()
    t.goto(325, 175)
    t.pd()

    t.color('black')
    t.goto(300, 250)
    t.goto(250, 200)

    t.pu()
    t.goto(375, 175)
    t.pd()

    t.goto(400, 250)
    t.goto(450, 200)


worm()
t.exitonclick()
