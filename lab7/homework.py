import turtle as t

t.reset()
t.title('Петухон — лучший язык программирования')
t.setup(1920, 1080, 0, 0)  # set resolution and start point

t.pd()
t.ht()


def train():
    t.pensize(3)
    t.color('green')

    t.begin_fill()
    t.circle(-25)
    t.end_fill()

    t.color('blue')
    t.pu()
    t.goto(-25, 0)
    t.pd()

    t.right(45)
    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.color('yellow')
    t.pu()
    t.goto(0, 75)
    t.left(45)
    t.pd()

    t.begin_fill()
    t.circle(40, steps=3)
    t.end_fill()

    t.color('brown')
    t.pu()
    t.goto(75, -5)
    t.left(45)
    t.pd()

    t.begin_fill()
    t.circle(-25)
    t.end_fill()

    t.color('green')
    t.pu()
    t.goto(50, 0)
    t.pd()

    t.right(90)
    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.color('green')
    t.pu()
    t.goto(50, 70)
    t.pd()

    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.color('yellow')
    t.pu()
    t.goto(70, 80)
    t.pd()

    t.begin_fill()
    t.circle(25, steps=4)
    t.end_fill()

    t.color('red')
    t.pu()
    t.goto(250, -5)
    t.pd()

    t.begin_fill()
    t.circle(-25)
    t.end_fill()

    t.color('brown')
    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.pu()
    t.goto(177, -5)
    t.pd()

    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.pu()
    t.goto(325, 64)
    t.lt(135)
    t.pd()

    t.color('blue')
    t.begin_fill()
    t.circle(75, extent=180)
    t.end_fill()

    t.color('darkblue')
    t.pu()
    t.goto(450, -5)
    t.lt(45)
    t.pd()

    t.begin_fill()
    t.circle(-25)
    t.end_fill()

    t.color('brown')
    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.pu()
    t.goto(377, -5)
    t.pd()

    t.begin_fill()
    t.circle(50, steps=4)
    t.end_fill()

    t.pu()
    t.goto(525, 64)
    t.lt(135)
    t.pd()

    t.color('yellow')
    t.begin_fill()
    t.circle(75, extent=180)
    t.end_fill()


train()
t.exitonclick()
