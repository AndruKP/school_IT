import turtle as t

t.reset()
t.title('Петухон — лучший язык программирования')
t.setup(1920, 1080, 0, 0)  # set resolution and start point

t.pd()
t.ht()


def bird():
    t.pensize(3)
    t.color('black', '#CACACA')

    t.pu()
    t.goto(0, 100)
    t.pd()

    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.pu()
    t.goto(-150, -150)
    t.pd()

    t.begin_fill()
    t.circle(150)
    t.end_fill()

    t.pu()
    t.goto(-100, -50)
    t.pd()

    t.color('black', '#B8B8B8')
    t.begin_fill()
    t.goto(-100, 100)
    t.goto(-250, -25)
    t.goto(-100, -50)
    t.end_fill()

    t.pu()
    t.goto(-200, -200)
    t.pd()

    t.color('black', '#A6A6A6')
    t.begin_fill()
    t.goto(-150, -200)
    t.goto(-200, -150)
    t.goto(-200, -200)
    t.end_fill()

    t.pu()
    t.goto(-450, 50)
    t.pd()

    t.color('black', '#D2D2D2')
    t.begin_fill()
    t.goto(-350, 200)
    t.goto(-300, 50)
    t.goto(-450, 50)
    t.end_fill()
    t.goto(-300, 50)
    t.goto(-400, 125)

    t.color('black', '#E5E5E5')

    t.pu()
    t.goto(25, 200)
    t.pd()

    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.pu()
    t.goto(-25, 250)
    t.pd()
    t.goto(5, 245)

    t.pu()
    t.goto(0, 260)
    t.pd()
    t.goto(15, 250)

    t.pu()
    t.goto(10, 275)
    t.pd()
    t.goto(25, 250)

    t.pu()
    t.goto(80, 255)
    t.pd()

    t.color('black', '#E68422')
    t.begin_fill()
    t.goto(100, 200)
    t.goto(150, 250)
    t.goto(80, 255)
    t.end_fill()

    t.pu()
    t.goto(40, 225)
    t.pd()

    t.color('black','white')
    t.begin_fill()
    t.circle(5)
    t.end_fill()


bird()
t.exitonclick()
