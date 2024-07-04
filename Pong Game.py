# PONG GAME 
import turtle as t
import random
import winsound
wn=t.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


score_a = 0
score_b = 0
#Paddle B
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.color("purple")
paddle_a.shape("square")  #default size 20*20 pixel
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #100 *20
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.color("purple")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #100 *20
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=t.Turtle()
ball.speed(0)
ball.color("yellow")
ball.shape("circle")
ball.penup()
ball.goto(0,0)

ball.dx=1
ball.dy=1

#Pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font=("courier",24,"normal"))

#function paddle movement
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    if y>=250:
        y=250
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    if y<=-250:
        y=-250
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    if y>=250:
        y=250
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    if y<=-250:
        y=-250
    paddle_b.sety(y)

#keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
   
while True:
    wn.update()

    # move the ball regular update
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1
        winsound.Playsound("hit.wav", winsound.SND_ASYNC)
        #ball.dy *= random.choice([-1.1])
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.Playsound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b), align = "center", font=("courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a,score_b), align = "center", font=("courier",24,"normal"))

    #import random

    #if ball.xcor() > 390:
       # ball.goto(0,0)
       # ball.dy += random.choice([-1,1])
    #if ball.xcor() <-390:
        #ball.goto(0,0)
        #ball.dy *= random.choice([-1,1])
    

    # paddle and bal collide
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50) and (ball.ycor() > paddle_b.ycor()-50):
      ball.setx(330)
      ball.dx *= -1
      winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50) and (ball.ycor() > paddle_a.ycor()-50):
      ball.setx(-330)
      ball.dx *= -1
      winsound.Playsound("hit.wav", winsound.SND_ASYNC)


