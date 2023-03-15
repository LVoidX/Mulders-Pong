import sys
import main
import turtle
import start_screen

window_resolution = 700
highscore = main.score_player_a
highscore_gamemode = main.highscore_difficulty
game_running = True
save_highscore = False

window = turtle.Screen()
window.title(start_screen.game_name)
window.bgcolor()
window.setup(width=window_resolution, height=window_resolution)
window.tracer(0)


def yes_click(x, y):
    global game_running
    global save_highscore
    save_highscore = True
    print(save_highscore)
    game_running = False


def no_click(x, y):
    global game_running
    global save_highscore
    save_highscore = False
    print(save_highscore)
    game_running = False
    turtle.bye()
    sys.exit()


def yes_text():
    yes = turtle.Turtle()
    yes.clear()
    yes.penup()
    yes.goto(150, -75)
    yes.pendown()
    yes.color("white")
    yes.shape("blank")
    yes.write("Yes", align="center", font=("Arial", 20, "bold"))


def no_text():
    no = turtle.Turtle()
    no.clear()
    no.penup()
    no.goto(-150, -75)
    no.pendown()
    no.color("white")
    no.shape("blank")
    no.write("No", align="center", font=("Arial", 20, "bold"))


yes_button = turtle.Turtle()
yes_button.penup()
yes_button.goto(150, -100)
yes_button.color("white")
yes_button.shape("square")
yes_button.shapesize(2.5, 6)
yes_button.onclick(yes_click)
yes_button.stamp()
yes_button.write("Yes", align="center", font=("Arial", 16, "normal"))

no_button = turtle.Turtle()
no_button.penup()
no_button.goto(-150, -100)
no_button.color("white")
no_button.shape("square")
no_button.shapesize(2.5, 6)
no_button.onclick(no_click)
no_button.stamp()
no_button.write("No", align="center", font=("Arial", 16, "normal"))


def save_high_score_text():
    save_text = turtle.Turtle()
    save_text.penup()
    save_text.goto(0, 0)
    save_text.pendown()
    save_text.color("white")
    save_text.shape("blank")
    save_text.write("Would you like to save your score?: ", align="center", font=("Arial", 20, "bold"))


while game_running:
    window.update()
    save_high_score_text()
    yes_text()
    no_text()
