import turtle as t

game: bool = True

#creating a window
window = t.Screen()
window.title("The Pong game")
window.bgcolor('black')
window.setup(width= 1050, height= 650)
window.tracer(1)

#creating a ball
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('Red')
ball.penup()
ball.goto(0,0)
ball.dx = 9
ball.dy = -9


#Right paddle
rpaddle = t.Turtle()
rpaddle.speed(0)
rpaddle.shape('square')
rpaddle.color('white')
rpaddle.shapesize(stretch_wid=6, stretch_len=1)
rpaddle.penup()
rpaddle.goto(400, 0)

#Left paddle
lpaddle = t.Turtle()
lpaddle.speed(0)
lpaddle.shape('square')
lpaddle.color('white')
lpaddle.shapesize(stretch_wid=6, stretch_len=1)
lpaddle.penup()
lpaddle.goto(-400, 0)

#default value
rpaddle.move_up = False
rpaddle.move_down = False
lpaddle.move_up = False
lpaddle.move_down = False
#Functions
def rpaddle_up_start():
    rpaddle.move_up = True
def rpaddle_up_end():
    rpaddle.move_up = False
def rpaddle_down_start():
    rpaddle.move_down = True
def rpaddle_down_end():
    rpaddle.move_down = False

def lpaddle_up_start():
    lpaddle.move_up = True
def lpaddle_up_end():
    lpaddle.move_up = False
def lpaddle_down_start():
    lpaddle.move_down = True
def lpaddle_down_end():
    lpaddle.move_down = False


#Binding keys for the paddles
window.listen()
window.onkeypress(rpaddle_up_start, 'Up')
window.onkeyrelease(rpaddle_up_end, 'Up')

window.onkeypress(rpaddle_down_start, 'Down')
window.onkeyrelease(rpaddle_down_end, 'Down')

window.onkeypress(lpaddle_up_start, 'w')
window.onkeyrelease(lpaddle_up_end, 'w')

window.onkeypress(lpaddle_down_start, 's')
window.onkeyrelease(lpaddle_down_end, 's')


while game:

    # window.update()

    # ball.setx(ball.xcor() + ball.dx)
    # ball.sety(ball.ycor() + ball.dy)

    #creating a border
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0,0)
        ball.dy *= -1

    if ball.xcor() < -500:
        ball.goto(0,0)
        ball.dy *= -1
    
    #collsion of paddle and ball
    if(ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < rpaddle.ycor() + 60) and (ball.ycor() > rpaddle.ycor() - 60):
        ball.setx(360)
        ball.dx *= -1

    if(ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < lpaddle.ycor() + 60) and (ball.ycor() > lpaddle.ycor() - 60):
        ball.setx(-360)
        ball.dx *= -1

    if rpaddle.move_up:
        if rpaddle.ycor() + 40 < 300:
            y = rpaddle.ycor()
            y += 25
            rpaddle.sety(y)

    if rpaddle.move_down:
        if rpaddle.ycor() - 45 > -300:
            y = rpaddle.ycor()
            y -= 25
            rpaddle.sety(y)

    if lpaddle.move_up:
        if lpaddle.ycor() + 40 < 300:
            y = lpaddle.ycor()
            y += 25
            lpaddle.sety(y)

    if lpaddle.move_down:
        if lpaddle.ycor() - 45 > -300:
            y = lpaddle.ycor()
            y -= 25
            lpaddle.sety(y)

    window.update()
    
input()