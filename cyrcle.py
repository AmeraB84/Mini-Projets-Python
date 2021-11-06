import turtle as t

b = t.Turtle()


def cyrcle():

    for i in range(1, 10):
        b.color = 'blue'
        b.circle(i*5)
        b.color = 'red'
        b.circle(-i*5)


cyrcle()
t.done()
