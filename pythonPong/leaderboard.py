import sys
import time
import turtle
import os

# Turtle Variables
turtle_leaderboard_title = turtle.Turtle()
turtle_close_text = turtle.Turtle()

# Other Variables
leaderboard_running = True
universal_background_colour = "blue"
game_name = "Mulders Pong v1.6 by L_Void_X"

# Window Settings
window_resolution = 700
window = turtle.Screen()
window.title(game_name)
window.bgcolor(universal_background_colour)
window.setup(width=window_resolution, height=window_resolution)
window.tracer(0)


def leaderboard_title(lines):
    turtle_leaderboard_title.clear()
    turtle_leaderboard_title.penup()
    turtle_leaderboard_title.goto(0, 250)
    turtle_leaderboard_title.pendown()
    turtle_leaderboard_title.color("black")
    turtle_leaderboard_title.shape("blank")
    turtle_leaderboard_title.write("Top 10 Mulders Pong Players:", align="center", font=("Arial", 30, "bold"))

    # write each line of the leaderboard at a different y-coordinate
    turtle_leaderboard_title.penup()
    turtle_leaderboard_title.goto(0, 165)
    turtle_leaderboard_title.pendown()
    turtle_leaderboard_title.color("black")
    turtle_leaderboard_title.shape("blank")
    for i, line in enumerate(lines[:10]):
        turtle_leaderboard_title.write(line.strip(), align="center", font=("Arial", 20, "bold"))
        turtle_leaderboard_title.penup()
        turtle_leaderboard_title.goto(0, 165 - (i + 1) * 37)
        turtle_leaderboard_title.pendown()


def close_text():
    turtle_close_text.clear()
    turtle_close_text.penup()
    turtle_close_text.goto(0, -250)
    turtle_close_text.pendown()
    turtle_close_text.color("white")
    turtle_close_text.shape("blank")
    turtle_close_text.write("Back", align="center", font=("Arial", 16, "bold"))


def close_click(x, y):
    global leaderboard_running
    leaderboard_running = False
    turtle.bye()
    os.system("python highscores.py")
    time.sleep(0.5)
    sys.exit()


close_button = turtle.Turtle()
close_button.penup()
close_button.goto(0, -275)
close_button.color("black")
close_button.shape("square")
close_button.shapesize(2.5, 7.5)
close_button.onclick(close_click)

with open("highscores.txt", "r") as f:
    lines = f.readlines()
    sorted_lines = sorted(lines, key=lambda line: int(line.split(":")[1]), reverse=True)

while leaderboard_running:
    window.update()
    leaderboard_title(sorted_lines)
    close_text()

if not leaderboard_running:
    leaderboard_title(sorted_lines[:10])
    turtle_leaderboard_title.hideturtle()
    turtle_leaderboard_title.clear()
turtle_close_text.hideturtle()
turtle_close_text.clear()
close_button.hideturtle()
close_button.clear()
turtle.bye()
sys.exit()
