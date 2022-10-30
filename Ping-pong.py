from ast import alias
from tkinter.font import ITALIC
import turtle as t
from time import sleep
import time
game: bool = True

#creating a window
window = t.Screen()
window.title("The Pong game")
window.bgcolor('black')
window.setup(width= 1050, height= 650)
window.tracer(0)

#creating a ball
ball = t.Turtle()
ball.speed()
ball.shape('circle')
ball.color('Red')
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

#Right paddle
rpaddle = t.Turtle()
rpaddle.speed(0)
rpaddle.shape('square')
rpaddle.color('white')
rpaddle.shapesize(stretch_wid=6, stretch_len=0.5)
rpaddle.penup()
rpaddle.goto(400, 0)

#Left paddle
lpaddle = t.Turtle()
lpaddle.speed(0)
lpaddle.shape('square')
lpaddle.color('white')
lpaddle.shapesize(stretch_wid=6, stretch_len=0.5)
lpaddle.penup()
lpaddle.goto(-400, 0)

#creating score variables
player_1 = 0
player_2 = 0

#Score board
score = t.Turtle()
score.speed(0)
score.color('orange')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0    Player 2: 0", align='center', font=('Courier', 24, 'normal'))

#Timer
count = 0
timer = t.Turtle()
timer.speed(0)
timer.color('purple')
timer.hideturtle()
timer.goto(-500, 280)
timer.write("Timer: 0", align='left',font=('Times New Roman', 18, 'normal', 'bold'))
            
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
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #creating a border
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    
    #collsion of the right paddle and ball
    if(ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < rpaddle.ycor() + 66) and (ball.ycor() > rpaddle.ycor() - 66):
        ball.setx(360)
        ball.dx *= -1
    #collsion of the left paddle and ball
    if(ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < lpaddle.ycor() + 66) and (ball.ycor() > lpaddle.ycor() - 66):
        ball.setx(-360)
        ball.dx *= -1

    #Moving the paddles
    if rpaddle.move_up:
        if rpaddle.ycor() + 100 < 300:
            y = rpaddle.ycor()
            y += 15
            rpaddle.sety(y)

    if rpaddle.move_down:
        if rpaddle.ycor() - 45 > -300:
            y = rpaddle.ycor()
            y -= 15
            rpaddle.sety(y)

    if lpaddle.move_up:
        if lpaddle.ycor() + 100 < 300:
            y = lpaddle.ycor()
            y += 15
            lpaddle.sety(y)

    if lpaddle.move_down:
        if lpaddle.ycor() - 45 > -300:
            y = lpaddle.ycor()
            y -= 15
            lpaddle.sety(y)
     
    #updating score
    if ball.xcor() > 500:
        ball.goto(0,0)
        ball.dy *= -1
        player_1 += 1
        score.clear()
        score.write("Player_1: {}   Player_2: {}".format(player_1, player_2), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -500:
        ball.goto(0,0)
        ball.dy *= -1
        player_2 += 1
        score.clear()
        score.write("Player_1: {}   Player_2: {}".format(player_1, player_2), align='center', font=('Courier', 24, 'normal'))
    
    #Timer
    count += 1
    timer.clear()
    timer.speed(0)
    timer.write("Timer: {}".format(count/100),align='left', font=('Times New Roman', 18, 'normal', 'bold'))

    sleep(0.0001)
    window.update()
    

