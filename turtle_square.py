import turtle as t

Bob = t.Turtle()


def square(taille, color):
    Bob.color(color)
    for x in range(0, 4):
        Bob.forward(taille)
        Bob.left(90)


square(100, 'red')
Bob.penup()
Bob.forward(150)
Bob.pendown()
square(150, 'brown')


t.done()
