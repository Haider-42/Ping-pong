#Python libraries
import math
import turtle as t
from time import sleep
import random

t.colormode (255)

game: bool = True
pic = "Ping-pong/nasa_wallpaper.gif"

#creating a window
window = t.Screen()
window.title("The Pong game")
window.bgpic(pic)
window.setup(width= 1050, height= 650)
window.tracer(0)

#creating a ball
ball = t.Turtle()
ball.speed()
ball.shape('circle')
ball.color('red')
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
score.write("Player_1: 0        Player_2: 0", align='center', font=('Courier', 24, 'normal'))

#Timer
count = 0
timer = t.Turtle()
timer.speed(0)
timer.color('green')
timer.hideturtle()
timer.goto(0, 260)
timer.write("0", align='center',font=('Lining and tabular', 24, 'normal'))
            
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

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #random color
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = r,g,b

    #creating a border
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    
    #collsion of the right paddle and ball
    if(ball.xcor() > 360 and ball.xcor() < 375) and (ball.ycor() < rpaddle.ycor() + 66) and (ball.ycor() > rpaddle.ycor() - 66):
        rpaddle.color(rgb)
        ball.setx(360)
        ball.dx *= -1 
    #collsion of the left paddle and ball
    if(ball.xcor() < -360 and ball.xcor() > -375) and (ball.ycor() < lpaddle.ycor() + 66) and (ball.ycor() > lpaddle.ycor() - 66):
        lpaddle.color(rgb)
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
        score.write("Player_1: {}        Player_2: {}".format(player_1, player_2), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -500:
        ball.goto(0,0)
        ball.dy *= -1
        player_2 += 1
        score.clear()
        score.write("Player_1: {}        Player_2: {}".format(player_1, player_2), align='center', font=('Courier', 24, 'normal'))

    #Updating timer
    count += 1.65
    timer.clear()
    timer.speed(0)
    timer.write("{}".format(math.trunc(count/100)),align='center', font=('Lining and tabular', 24, 'normal'))

    sleep(0.0001) #Refreshing speed
    window.update()
