# import turtle as t

# score_A = 0
# score_B = 0

# window = t.Screen()
# window.title("Ping_Pong")
# window.bgcolor("green")
# window.setup(width=800, height=600)
# window.tracer(0)

# # Creating of left padle
# leftPadle = t.Turtle()
# leftPadle.speed(0)
# leftPadle.shape('square')
# leftPadle.color('white')
# leftPadle.shapesize(stretch_wid=5, stretch_len=1)
# leftPadle.goto(-350, 0)

# # Creating of right padle
# rightPadle = t.Turtle()
# rightPadle.speed(0)
# rightPadle.shape('square')
# rightPadle.color('white')
# rightPadle.shapesize(stretch_wid=5, stretch_len=1)
# rightPadle.goto(350, 0)

# # Creating a ball
# ball = t.Turtle()
# ball.shape('circle')
# ball.speed(0)
# ball.color('red')
# ball.penup()
# ball.goto(5, 5)
# ballXDirection = 0.2
# ballYdirection = 0.2

# # Creating a pen for score
# p = t.Turtle()
# p.color = 'blue'
# p.speed(0)
# p.penup()
# p.hideturtle()
# p.goto(0, 260)
# p.write('score', align='center', font=('arial', 24, 'normal'))

# # Moving leftPadle


# def leftBadleUp():
#     y = leftPadle.ycor()
#     y = y + 90
#     leftPadle.sety()


# def leftBadleDown():
#     y = leftPadle.ycor()
#     y = y - 90
#     leftPadle.sety()


# # Moving rightPadle

# def rightBadleUp():
#     y = rightPadle.ycor()
#     y = y + 90
#     leftPadle.sety()


# def rightBadleDown():
#     y = rightPadle.ycor()
#     y = y - 90
#     rightPadle.sety()


# window.listen()
# window.onkeypress(leftBadleUp, 'w')
# window.onkeypress(leftBadleDown, 's')
# window.onkeypress(rightBadleUp, 'Up')
# window.onkeypress(rightBadleDown, 'Down')

# while True:

#     # Moving the ball
#     window.update()
#     ball.setx(ball.xcor()+ballXDirection)
#     ball.sety(ball.ycor()+ballYdirection)


# # Making border
#     if ball.xcor() > 290:
#         ball.setx(290)
#         ballYdirection = ballYdirection*-1
#     if ball.xcor() > -290:
#         ball.setx(-290)
#         ballYdirection = ballYdirection*-1

#     if ball.xcor() > 390:
#         ball.goto(0, 0)
#         ballXDirection = ballXDirection
#         score_A += 1
#         p.clear()
#         p.write(f'Player A : {score_A} ; Player B : {score_B}',
#                 align='center', font=("arial"))

#     if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() > rightPadle.ycor()+40 and ball.ycor() > rightPadle.ycor()+40):
#         ball.setx(340)
#         ballXDirection = ballXDirection+-1

#     if (ball.xcor() > -340) and (ball.xcor() < -350) and (ball.ycor() > rightPadle.ycor()+40 and ball.ycor() > rightPadle.ycor()+40):
#         ball.setx(-340)
#         ballXDirection = ballXDirection+-1


# t.done()
