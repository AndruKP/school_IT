import turtle as t

t.reset()
t.title('Петухон — лучший язык программирования')

t.pd()
t.ht()


def wing():
    t.pu()
    t.home()
    t.pd()

    t.pensize(4)
    t.color('light blue', 'dark blue')

    t.begin_fill()
    t.goto(250, 0)
    t.goto(150, -50)
    t.goto(250, -50)
    t.goto(150, -100)
    t.goto(200, -100)
    t.goto(100, -150)
    t.goto(-100, -150)
    t.goto(-100, -50)
    t.goto(0, 0)
    t.end_fill()

    t.pu()


def body():
    t.pu()
    t.goto(300, 150)
    t.pd()

    t.pensize(4)
    t.color('dark blue')

    t.goto(300, -100)
    t.goto(150, -250)
    t.goto(-150, -250)
    t.goto(-250, -150)
    t.goto(-250, 0)
    t.goto(-150, 100)
    t.goto(-150, 150)
    t.goto(-250, 150)
    t.goto(-200, 200)
    t.goto(-250, 250)
    t.goto(-200, 250)
    t.goto(-150, 300)
    t.goto(-100, 300)
    t.goto(-50, 250)
    t.goto(-50, 100)
    t.goto(-100, 50)
    t.goto(-100, 0)
    t.goto(-50, 50)
    t.goto(200, 50)
    t.goto(300, 150)


body()
wing()
t.exitonclick()
