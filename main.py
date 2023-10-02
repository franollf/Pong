# A Simple Pong Game
# Franoll Fnatu
# September 13th, 2023


import turtle 
import os
import sys
import pygame
import random

pygame.mixer.init()

# Sounds
wall_hit_sound = pygame.mixer.Sound('pongame.py/sounds/wall.wav')
paddle_hit_sound = pygame.mixer.Sound('pongame.py/sounds/paddle.wav')
score_sound = pygame.mixer.Sound('pongame.py/sounds/score.wav')
win_sound = pygame.mixer.Sound('pongame.py/sounds/winner.wav')

# Setting up the Main Screen
win_sound.play()
wn = turtle.Screen()
wn.title("Pong by Franoll Fantu")
wn.bgcolor("Black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


 # Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2



# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)


# Functions
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y += -20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y += -20
    pad_b.sety(y)

def start_game():
    global game_started
    game_started = True
    start_screen.clear()

def quit():
    turtle.bye()

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

    
# Setting the movement Keys
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

# Making the Start Screen
start_screen = turtle.Turtle()
start_screen.speed(0)
start_screen.color("white")
start_screen.penup()
start_screen.hideturtle()
start_screen.goto(0, 0)
start_screen.write("Press Enter to Play", align="center", font=("Courier", 50, "normal"))


game_started = False
wn.listen()
wn.onkeypress(start_game, "Return")

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-10, 260)
pen.write(f"Player A: 0 Player B: 0", align="center", font=("Courier", 35, "normal"))




# Main loop
while True: 
    wn.update()

    if not game_started:
        continue
   
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        wall_hit_sound.play()
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        wall_hit_sound.play()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_sound.play()
        score_a += 1
        pen.clear()
        pen.write(f"Player A: turtle{score_a} Player B: {score_b}", align="center", font=("Courier", 35, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_sound.play()
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 35, "normal"))


    # Win Message
    if score_a  == 7:
        wina = turtle.Turtle()
        wina.speed(0)
        wina.color("white")
        wina.penup()
        wina.hideturtle()
        wina.goto(-10, 260)
        pen.clear()
        wina.write(f"Congratulations! Player A Wins!", align="center", font=("Courier", 35, "normal"))
        winb.write("Press R to Restart or Q to Quit", align="center", font=("Courier", 35, "normal"))
        ball.goto(0,0)
        ball.dx = 0
        ball.dy = 0
        wina.penup()
        wina.goto(0, -wn.window_height() / 2 + 20)  # Position at the bottom center
        # Display to Quit
        wina.write("Press R to Restart or Q to Quit", align="center", font=("Courier", 35, "normal"))
        wn.listen()
        wn.onkeypress(restart_program, "r")
        wn.onkeypress(quit, "q")



    if score_b  == 7:
        winb = turtle.Turtle()
        winb.speed(0)
        winb.color("white")
        winb.penup()
        winb.hideturtle()
        winb.goto(-10, 260)
        pen.clear()
        winb.write(f"Congratulations! Player B Wins!", align="center", font=("Courier", 35, "normal"))
        ball.goto(0,0)
        ball.dx = 0
        ball.dy = 0
        winb.penup()  # Lift the pen to move without drawing
        winb.goto(0, -wn.window_height() / 2 + 20)  # Position at the bottom center
        # Display to Quit
        winb.write("Press R to Restart or Q to Quit", align="center", font=("Courier", 35, "normal"))
        wn.listen()
        wn.onkeypress(restart_program, "r")
        wn.onkeypress(quit, "q")
        
        
       

        
    # TODO: MAKE IT SLEEP WITHOUT CRASHING AND BIND A RESTART LOOP TO "R" AND QUIT TO "Q"

    # Paddle V.S. Ball

    # Basically, if the ball x and y cord matches up with either paddle a or paddle b make it bounce off
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        paddle_hit_sound.play()
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        paddle_hit_sound.play()
        

        #AI PLAYER

    if pad_b.ycor() < ball.ycor() and abs(pad_b.ycor() - ball.ycor()) > 10:
        pad_b_up()

    elif pad_b.ycor() > ball.ycor() and abs(pad_b.ycor() - ball.ycor()) > 10:
       pad_b_down()





