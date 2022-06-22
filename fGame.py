from pydoc import plain
import turtle
from typing import Text

# set the name of turtle library as window
window = turtle.Screen();
window.title("Ping Pong Game")
window.setup(width=800 , height=600)
# عدم وضع فاصل زمني باللعبه مشان التقطيع
window.tracer(0)
window.bgcolor(0.12,0.12,0.12)

# Setup game object
ball = turtle.Turtle() #To creat an objects
ball.speed(0) #From 1 to 10
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1 , stretch_wid=1) # Which is equal in default (20px * 20px)
ball.goto(x=0,y=0) # start postions
ball.penup() # stop drwing lines when it't moving (leg)
ball_dx,ball_dy = 1 , 1
ball_speed = .37

# Center line -----------------
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=.1,stretch_wid=25)
center_line.penup()
center_line.goto(0,0)

# Player 1 -------------------
plr1 = turtle.Turtle()
plr1.shape("square")
plr1.speed(0)
plr1.penup()
plr1.color("light Green")
plr1.goto(-350,0)
plr1.shapesize(stretch_len=1,stretch_wid=6)


# Player 2 -------------------
plr2 = turtle.Turtle()
plr2.shape("square")
plr2.speed(0)
plr2.penup()
plr2.color("light blue")
plr2.goto(350,0)
plr2.shapesize(stretch_len=1,stretch_wid=6)
 
#score text 
scoretxt = turtle.Turtle()
scoretxt.speed(0)
scoretxt.penup()
scoretxt.color("White")
scoretxt.goto(0,260)
scoretxt.write("Player1: 0  Player2: 0", align="center", font=("Courier",14,"normal"))
scoretxt.hideturtle()  # we hide the shpae of the object >
p1_score, p2_score = 0, 0

# Player Movement ------------
Player_speed = 20

def p1_move_up():
    plr1.sety(plr1.ycor()+Player_speed)  #ycor the place of player 1
    
def p1_move_down():
    plr1.sety(plr1.ycor()-Player_speed)

def p2_move_up():
    plr2.sety(plr2.ycor()+Player_speed)  #ycor the place of player 1
    
def p2_move_down():
    plr2.sety(plr2.ycor()-Player_speed)
    
# Get User Inputs ------------
window.listen()
window.onkeypress(p1_move_up,"w")
window.onkeypress(p1_move_down,"s")
window.onkeypress(p2_move_up,"Up")
window.onkeypress(p2_move_down,"Down")
    
    
# game loop
while True:
    window.update()
    
    # Ball Movement --------
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))
    
    # Ball borders ---------
    if(ball.ycor() > 290): # Top-border = 300 , half-ball-size = 10
        ball.sety(290)
        ball_dy *= -1  # Oposite (go to the another direction) 
        
    if(ball.ycor() < -290): # Top-border = 300 , half-ball-size = 10
        ball.sety(-290)
        ball_dy *= -1  # Oposite (go to the another direction)    
        
    # ball & players collisions =====================
    # collision with player 1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (plr1.ycor()-60) and ball.ycor() < (plr1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    # collision with player 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (plr2.ycor()-60) and ball.ycor() < (plr2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1
        
    
    # score handling
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1  # invert X direction
        scoretxt.clear()
        p1_score += 1
        scoretxt.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))

    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1  # invert X direction
        scoretxt.clear()
        p2_score += 1
        scoretxt.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                    font=("Courier", 14, "normal"))
        
        
        
        
    
    