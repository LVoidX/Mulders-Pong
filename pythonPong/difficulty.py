import turtle
import start_screen

# Variables
game_running = True
against_cpu = False
turtle_start = turtle.Turtle()
turtle_question = turtle.Turtle()
turtle_easy_text = turtle.Turtle()
turtle_medium_text = turtle.Turtle()
turtle_hard_text = turtle.Turtle()
vs_cpu = start_screen.against_cpu
cpu_difficulty = 0
highscore_difficulty = start_screen.highscore_mode
universal_background_colour = start_screen.universal_background_colour

# Window Settings
window_resolution = 700
window = turtle.Screen()
window.title(start_screen.game_name)
window.bgcolor(universal_background_colour)
window.setup(width=window_resolution, height=window_resolution)
window.tracer(0)


def easy_click(x, y):
    global game_running
    global cpu_difficulty
    cpu_difficulty = "EASY"
    print(cpu_difficulty)
    game_running = False


def medium_click(x, y):
    global game_running
    global cpu_difficulty
    cpu_difficulty = "MEDIUM"
    print(cpu_difficulty)
    game_running = False


def hard_click(x, y):
    global game_running
    global cpu_difficulty
    cpu_difficulty = "HARD"
    print(cpu_difficulty)
    game_running = False


def start_screen():
    turtle_start.clear()
    turtle_start.penup()
    turtle_start.goto(0, 100)
    turtle_start.pendown()
    turtle_start.color("black")
    turtle_start.shape("blank")
    turtle_start.write("Mulders Pong!!", align="center", font=("Arial", 40, "bold"))


def start_question():
    turtle_question.clear()
    turtle_question.penup()
    turtle_question.goto(0, 50)
    turtle_question.pendown()
    turtle_question.color("black")
    turtle_question.shape("blank")
    turtle_question.write("Select CPU Difficulty", align="center", font=("Arial", 25, "bold"))


# create a turtle button for Easy mode
easy_button = turtle.Turtle()
easy_button.penup()
easy_button.goto(-225, -50)
easy_button.color("black")
easy_button.shape("square")
easy_button.shapesize(2.5, 6)
easy_button.onclick(easy_click)
easy_button.stamp()
easy_button.write("Easy", align="center", font=("Arial", 16, "normal"))

# create a turtle button for Medium mode
medium_button = turtle.Turtle()
medium_button.penup()
medium_button.goto(0, -50)
medium_button.color("black")
medium_button.shape("square")
medium_button.shapesize(2.5, 6)
medium_button.onclick(medium_click)
medium_button.stamp()
medium_button.write("Medium", align="center", font=("Arial", 16, "normal"))

# create a turtle button for Hard mode
hard_button = turtle.Turtle()
hard_button.penup()
hard_button.goto(225, -50)
hard_button.color("black")
hard_button.shape("square")
hard_button.shapesize(2.5, 6)
hard_button.onclick(hard_click)
hard_button.stamp()
hard_button.write("Hard", align="center", font=("Arial", 16, "normal"))


def easy_text():
    turtle_easy_text.clear()
    if game_running:
        turtle_easy_text.clear()
        turtle_easy_text.penup()
        turtle_easy_text.goto(-225, -25)
        turtle_easy_text.pendown()
        turtle_easy_text.color("white")
        turtle_easy_text.shape("blank")
        turtle_easy_text.write("Easy", align="center", font=("Arial", 20, "bold"))


def medium_text():
    turtle_medium_text.clear()
    if game_running:
        turtle_medium_text.clear()
        turtle_medium_text.penup()
        turtle_medium_text.goto(0, -25)
        turtle_medium_text.pendown()
        turtle_medium_text.color("white")
        turtle_medium_text.shape("blank")
        turtle_medium_text.write("Medium", align="center", font=("Arial", 20, "bold"))


def hard_text():
    turtle_hard_text.clear()
    if game_running:
        turtle_hard_text.clear()
        turtle_hard_text.penup()
        turtle_hard_text.goto(225, -25)
        turtle_hard_text.pendown()
        turtle_hard_text.color("white")
        turtle_hard_text.shape("blank")
        turtle_hard_text.write("Hard", align="center", font=("Arial", 20, "bold"))


# Main Game loop
while game_running:
    # Starting Updates
    if not vs_cpu:
        game_running = False
    if highscore_difficulty:
        cpu_difficulty = "HIGHSCORE"
        game_running = False
    easy_text()
    medium_text()
    hard_text()
    window.update()
    start_screen()
    start_question()
    turtle_easy_text.clear()
    turtle_easy_text.hideturtle()
    turtle_medium_text.clear()
    turtle_medium_text.hideturtle()
    turtle_hard_text.clear()
    turtle_hard_text.hideturtle()

window.bgcolor("black")
easy_button.clear()
easy_button.hideturtle()
medium_button.clear()
medium_button.hideturtle()
hard_button.clear()
hard_button.hideturtle()
turtle_start.hideturtle()
turtle_start.clear()
turtle_question.hideturtle()
turtle_question.clear()
window.update()
