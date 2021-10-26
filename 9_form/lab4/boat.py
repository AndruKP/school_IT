import turtle as t

t.reset()
t.title('Петухон - лучший язык программирования')

t.pd()
t.st()


def move():
    # човен
    t.fd(65)
    t.rt(135)
    t.fd(50)
    t.rt(45)
    t.fd(60)
    t.rt(45)
    t.fd(50)
    t.home()
    # парус
    t.lt(90)
    t.fd(100)
    t.rt(160)
    t.fd(59)
    t.home()
    t.ht()


move()
t.exitonclick()
