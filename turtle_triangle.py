import turtle as t

b = t.Turtle()


def triangle(taille, color):
    b.color(color)
    for i in range(0, 3):
        b.forward(taille)
        b.left(120)
        b.forward(taille)


triangle(150, 'red')
