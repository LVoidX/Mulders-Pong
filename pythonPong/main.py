# Pong by L_Void_X

import turtle
import time
import difficulty
import start_screen
import random

score_player_b = 0
score_player_a = 0
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle_timer = turtle.Turtle()
window_resolution = 700
paddle_b_x_position = window_resolution / 2 - 50
paddle_b_y_position = 0
paddle_a_x_position = -window_resolution / 2 + 50
paddle_a_y_position = 0
ball_speed = 0.35
game_running = True
countdown_value: int = 0
start_time = time.time()
cpu_speed = 0
times_looped = 0
vs_cpu = difficulty.vs_cpu
cpu_difficulty = difficulty.cpu_difficulty
highscore_difficulty = difficulty.highscore_difficulty
theme = start_screen.theme
background_color = "black"
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ball_directions = [0.35, -0.35]

window = turtle.Screen()
window.title(start_screen.game_name)
window.bgcolor(background_color)
window.setup(width=window_resolution, height=window_resolution)
window.tracer(0)

if cpu_difficulty == "EASY":
    cpu_speed = 0.33
elif cpu_difficulty == "MEDIUM":
    cpu_speed = 0.67
elif cpu_difficulty == "HARD":
    cpu_speed = 1

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(paddle_a_x_position, paddle_a_y_position)
paddle_a.shapesize(stretch_wid=5.5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(6)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(paddle_b_x_position, paddle_b_y_position)
paddle_b.shapesize(stretch_wid=5.5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.dx = random.choice(ball_directions)
ball.dy = random.choice(ball_directions)

# White Line
line = turtle.Turtle()
line.shape("square")
line.color("white")
line.goto(0, 0)
line.shapesize(stretch_wid=200000, stretch_len=0.1)


def win_screen():
    global score_player_a
    win_text = turtle.Turtle()
    win_text.penup()
    win_text.goto(0, 0)
    win_text.pendown()
    win_text.color("white")
    win_text.shape("blank")
    if highscore_difficulty:
        win_text.goto(0, 35)
        win_text.write("         YOU DIED :(\nYOUR SCORE WAS: " + str(score_player_a), align="center",
                       font=("Arial", 37, "bold"))
    if score_player_a == 3 and not highscore_difficulty:
        win_text.write("PLAYER 1 WINS!!", align="center", font=("Arial", 50, "bold"))
    elif score_player_b == 3:
        if not vs_cpu:
            win_text.write("PLAYER 2 WINS!!", align="center", font=("Arial", 50, "bold"))
        elif vs_cpu:
            win_text.write(cpu_difficulty + " BOT WINS!!", align="center", font=("Arial", 50, "bold"))


def timer():
    global ball_speed
    line.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()
    window.update()
    ball_speed = 0
    time_shown = 3
    turtle_timer.clear()
    turtle_timer.penup()
    turtle_timer.goto(0, 50)
    turtle_timer.pendown()
    turtle_timer.color("white")
    turtle_timer.shape("blank")
    turtle_timer.write("Game Starts in:\n            " + str(time_shown), align="center", font=("Arial", 50, "bold"))
    window.update()
    time.sleep(1)
    time_shown -= 1
    turtle_timer.clear()
    turtle_timer.write("Game Starts in:\n            " + str(time_shown), align="center", font=("Arial", 50, "bold"))
    window.update()
    time.sleep(1)
    time_shown -= 1
    turtle_timer.clear()
    turtle_timer.write("Game Starts in:\n            " + str(time_shown), align="center", font=("Arial", 50, "bold"))
    window.update()
    time.sleep(1)
    time_shown -= 1
    turtle_timer.clear()
    ball_speed = 0.35
    window.update()
    turtle_timer.hideturtle()
    turtle_timer.showturtle()
    line.showturtle()
    paddle_a.showturtle()
    paddle_b.showturtle()


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)


def display_text_player_b():
    turtle1.clear()
    turtle1.penup()
    turtle1.goto(window_resolution / 4, window_resolution / 2 - 50)
    turtle1.pendown()
    turtle1.color("white")
    turtle1.shape("blank")
    if not vs_cpu and not highscore_difficulty:
        turtle1.write("PLAYER 2 SCORE: " + str(score_player_b), align="center", font=("Arial", 25, "bold"))
    elif vs_cpu and not highscore_difficulty:
        turtle1.write(cpu_difficulty + " BOT: " + str(score_player_b), align="center", font=("Arial", 25, "bold"))


def display_text_player_a():
    turtle2.clear()
    turtle2.penup()
    turtle2.goto(-window_resolution / 4, window_resolution / 2 - 50)
    turtle2.pendown()
    turtle2.color("white")
    turtle2.shape("blank")
    if not highscore_difficulty:
        turtle2.write("PLAYER 1 SCORE: " + str(score_player_a), align="center", font=("Arial", 25, "bold"))
    if highscore_difficulty:
        turtle2.write("HIGHSCORE: " + str(score_player_a), align="center", font=("Arial", 25, "bold"))


# Keyboard Binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_up, "Up")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_a_down, "Down")
if not vs_cpu:
    window.onkeypress(paddle_b_up, "Up")
    window.onkeypress(paddle_b_down, "Down")

# Timer
timer()

# Main Game loop
while game_running:

    # Starting Updates
    window.update()
    display_text_player_b()
    display_text_player_a()
    if times_looped % 10 == 0:
        if theme == "EPILEPTIC":
            if background_color == "black":
                background_color = "white"
                window.bgcolor("white")
            elif background_color == "white":
                background_color = "black"
                window.bgcolor("black")
        if theme == "GAY":
            random_color = random.choice(rainbow_colors)
            window.bgcolor(random_color)
        times_looped += 1
    else:
        times_looped += 1
    turtle.Screen()
    if highscore_difficulty:
        if score_player_b == 1:
            ball_speed = 0
            ball.goto(0, 0)
            win_screen()
            window.update()
            game_running = False
            break
    if not highscore_difficulty:
        if score_player_a == 3 or score_player_b == 3:
            ball_speed = 0
            ball.goto(0, 0)
            win_screen()
    if ball.dx > 0:
        ball.dx = ball_speed
    else:
        ball.dx = -1 * ball_speed
    if ball.dy > 0:
        ball.dy = ball_speed
    else:
        ball.dy = -1 * ball_speed

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > window_resolution / 2 - 20:
        ball.sety(window_resolution / 2 - 20)
        ball.dy *= -1

    if ball.ycor() < -window_resolution / 2 + 20:
        ball.sety(-window_resolution / 2 + 20)
        ball.dy *= -1

    if ball.xcor() > window_resolution / 2 - 20:
        ball.setx(window_resolution / 2 - 20)
        ball.dx *= -1
        start_time = time.time()
        score_player_a += 1
        ball_speed = 0.35

    if ball.xcor() < -window_resolution / 2 + 20:
        ball.setx(-window_resolution / 2 + 20)
        ball.dx *= -1
        start_time = time.time()
        score_player_b += 1
        ball_speed = 0.35

    # Paddle and Ball Collisions
    if (paddle_b_x_position - 30 < ball.xcor() < paddle_b_x_position + 50) and (
            paddle_b.ycor() + 55 > ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(paddle_b_x_position - 30)
        ball.dx *= -1
        ball_speed += 0.025

    if (paddle_a_x_position + 30 > ball.xcor() > paddle_a_x_position - 50) and (
            paddle_a.ycor() + 55 > ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(paddle_a_x_position + 30)
        ball.dx *= -1
        ball_speed += 0.025
        if highscore_difficulty:
            score_player_a += 1

    if paddle_b.ycor() > window_resolution / 2 - 55:
        paddle_b.sety(window_resolution / 2 - 55)

    if paddle_b.ycor() < -window_resolution / 2 + 55:
        paddle_b.sety(-window_resolution / 2 + 55)

    if paddle_a.ycor() > window_resolution / 2 - 55:
        paddle_a.sety(window_resolution / 2 - 55)

    if paddle_a.ycor() < -window_resolution / 2 + 55:
        paddle_a.sety(-window_resolution / 2 + 55)

    if vs_cpu:
        if not highscore_difficulty:
            if ball.ycor() <= paddle_b.ycor():
                paddle_b.sety(paddle_b.ycor() - cpu_speed)
            elif ball.ycor() >= paddle_b.ycor():
                paddle_b.sety(paddle_b.ycor() + cpu_speed)
        if highscore_difficulty:
            paddle_b.sety(ball.ycor())

turtle1.clear()
turtle2.clear()
line.clear()
line.hideturtle()
ball.clear()
ball.hideturtle()
paddle_b.clear()
paddle_b.hideturtle()
paddle_a.clear()
paddle_a.hideturtle()
