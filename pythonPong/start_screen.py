import sys
import turtle
import os

# Variables
game_running = True
against_cpu = False
highscore_mode = False
leaderboard_activated = False
theme = 0
universal_background_colour = "blue"
turtle_start = turtle.Turtle()
turtle_question = turtle.Turtle()
turtle_theme = turtle.Turtle()
turtle_pvp_text = turtle.Turtle()
turtle_pve_text = turtle.Turtle()
turtle_highscore_text = turtle.Turtle()
turtle_normal_text = turtle.Turtle()
turtle_epileptic_text = turtle.Turtle()
turtle_gay_text = turtle.Turtle()

game_name = "Mulders Pong v1.6 by L_Void_X"

# Window Settings
window_resolution = 700
window = turtle.Screen()
window.title(game_name)
window.bgcolor(universal_background_colour)
window.setup(width=window_resolution, height=window_resolution)
window.tracer(0)

# Other Variables
window.register_shape("leaderboard_button.gif")


def pvp_click(x, y):
    global against_cpu
    global game_running
    against_cpu = False
    print(against_cpu)
    game_running = False


def pve_click(x, y):
    global against_cpu
    global game_running
    against_cpu = True
    print(against_cpu)
    game_running = False


def highscore_click(x, y):
    global against_cpu
    global game_running
    global highscore_mode
    against_cpu = True
    print(against_cpu)
    game_running = False
    highscore_mode = True


def normal_theme_click(x, y):
    global theme
    theme = "NORMAL"
    print(theme)
    normal_theme_button.color("green")
    epileptic_theme_button.color("black")
    gay_theme_button.color("black")


def epileptic_theme_click(x, y):
    global theme
    theme = "EPILEPTIC"
    print(theme)
    normal_theme_button.color("black")
    epileptic_theme_button.color("green")
    gay_theme_button.color("black")


def gay_theme_click(x, y):
    global theme
    theme = "GAY"
    print(theme)
    normal_theme_button.color("black")
    epileptic_theme_button.color("black")
    gay_theme_button.color("green")


def leaderboard_click(x, y):
    global leaderboard_activated
    global game_running
    game_running = False
    leaderboard_activated = True
    turtle.bye()
    os.system("python leaderboard.py")
    sys.exit()


def start_screen():
    turtle_start.clear()
    turtle_start.penup()
    turtle_start.goto(0, 200)
    turtle_start.pendown()
    turtle_start.color("black")
    turtle_start.shape("blank")
    turtle_start.write("Mulders Pong!!", align="center", font=("Arial", 40, "bold"))


def start_question():
    turtle_question.clear()
    turtle_question.penup()
    turtle_question.goto(0, 150)
    turtle_question.pendown()
    turtle_question.color("black")
    turtle_question.shape("blank")
    turtle_question.write("Select game mode:", align="center", font=("Arial", 25, "bold"))


def start_theme():
    turtle_theme.clear()
    turtle_theme.penup()
    turtle_theme.goto(0, -225)
    turtle_theme.pendown()
    turtle_theme.color("black")
    turtle_theme.shape("blank")
    turtle_theme.write("Select theme:", align="center", font=("Arial", 25, "bold"))


# create a turtle button for PvP mode
pvp_button = turtle.Turtle()
pvp_button.penup()
pvp_button.goto(-125, 75)
pvp_button.color("black")
pvp_button.shape("square")
pvp_button.shapesize(2.5, 7.5)
pvp_button.onclick(pvp_click)
pvp_button.stamp()
pvp_button.write("PvP", align="center", font=("Arial", 16, "normal"))

# create a turtle button for PvE mode
pve_button = turtle.Turtle()
pve_button.penup()
pve_button.goto(125, 75)
pve_button.color("black")
pve_button.shape("square")
pve_button.shapesize(2.5, 7.5)
pve_button.onclick(pve_click)
pve_button.stamp()
pve_button.write("PvE", align="center", font=("Arial", 16, "normal"))

highscore_button = turtle.Turtle()
highscore_button.penup()
highscore_button.goto(0, -50)
highscore_button.color("black")
highscore_button.shape("square")
highscore_button.shapesize(2.5, 7.5)
highscore_button.onclick(highscore_click)
highscore_button.stamp()
highscore_button.write("HighScore", align="center", font=("Arial", 16, "normal"))

normal_theme_button = turtle.Turtle()
normal_theme_button.penup()
normal_theme_button.goto(-225, -300)
normal_theme_button.color("black")
normal_theme_button.shape("square")
normal_theme_button.shapesize(2.5, 7.5)
normal_theme_button.onclick(normal_theme_click)
normal_theme_button.write("Normal", align="center", font=("Arial", 16, "normal"))

epileptic_theme_button = turtle.Turtle()
epileptic_theme_button.penup()
epileptic_theme_button.goto(0, -300)
epileptic_theme_button.color("black")
epileptic_theme_button.shape("square")
epileptic_theme_button.shapesize(2.5, 7.5)
epileptic_theme_button.onclick(epileptic_theme_click)
epileptic_theme_button.write("Epileptic", align="center", font=("Arial", 16, "normal"))

gay_theme_button = turtle.Turtle()
gay_theme_button.penup()
gay_theme_button.goto(225, -300)
gay_theme_button.color("black")
gay_theme_button.shape("square")
gay_theme_button.shapesize(2.5, 7.5)
gay_theme_button.onclick(gay_theme_click)
gay_theme_button.write("Gay", align="center", font=("Arial", 16, "normal"))

leaderboard_button = turtle.Turtle()
leaderboard_button.penup()
leaderboard_button.goto(280, 290)
leaderboard_button.color("black")
leaderboard_button.shape("leaderboard_button.gif")
leaderboard_button.shapesize(1, 1)
leaderboard_button.onclick(leaderboard_click)


def pvp_text():
    turtle_pvp_text.clear()
    if game_running:
        turtle_pvp_text.clear()
        turtle_pvp_text.penup()
        turtle_pvp_text.goto(-125, 100)
        turtle_pvp_text.pendown()
        turtle_pvp_text.color("white")
        turtle_pvp_text.shape("blank")
        turtle_pvp_text.write("PvP", align="center", font=("Arial", 20, "bold"))


def pve_text():
    turtle_pve_text.clear()
    if game_running:
        turtle_pve_text.clear()
        turtle_pve_text.penup()
        turtle_pve_text.goto(125, 100)
        turtle_pve_text.pendown()
        turtle_pve_text.color("white")
        turtle_pve_text.shape("blank")
        turtle_pve_text.write("PvE", align="center", font=("Arial", 20, "bold"))


def highscore_text():
    turtle_highscore_text.clear()
    if game_running:
        turtle_highscore_text.clear()
        turtle_highscore_text.penup()
        turtle_highscore_text.goto(0, -25)
        turtle_highscore_text.pendown()
        turtle_highscore_text.color("white")
        turtle_highscore_text.shape("blank")
        turtle_highscore_text.write("Highscore", align="center", font=("Arial", 20, "bold"))


def normal_text():
    turtle_normal_text.clear()
    if game_running:
        turtle_normal_text.clear()
        turtle_normal_text.penup()
        turtle_normal_text.goto(-225, -275)
        turtle_normal_text.pendown()
        turtle_normal_text.color("white")
        turtle_normal_text.shape("blank")
        turtle_normal_text.write("Normal", align="center", font=("Arial", 20, "bold"))


def epileptic_text():
    turtle_epileptic_text.clear()
    if game_running:
        turtle_epileptic_text.clear()
        turtle_epileptic_text.penup()
        turtle_epileptic_text.goto(0, -275)
        turtle_epileptic_text.pendown()
        turtle_epileptic_text.color("white")
        turtle_epileptic_text.shape("blank")
        turtle_epileptic_text.write("Epileptic", align="center", font=("Arial", 20, "bold"))


def gay_text():
    turtle_gay_text.clear()
    if game_running:
        turtle_gay_text.clear()
        turtle_gay_text.penup()
        turtle_gay_text.goto(225, -275)
        turtle_gay_text.pendown()
        turtle_gay_text.color("white")
        turtle_gay_text.shape("blank")
        turtle_gay_text.write("Gay", align="center", font=("Arial", 20, "bold"))


# Main Game loop
while game_running:
    # Starting Updates
    pvp_text()
    pve_text()
    highscore_text()
    normal_text()
    epileptic_text()
    gay_text()
    window.update()
    start_screen()
    start_question()
    start_theme()
    turtle_pvp_text.clear()
    turtle_pve_text.clear()
    turtle_highscore_text.clear()
    turtle_normal_text.clear()
    turtle_epileptic_text.clear()
    turtle_gay_text.clear()

pve_button.hideturtle()
pvp_button.hideturtle()
highscore_button.hideturtle()
normal_theme_button.hideturtle()
epileptic_theme_button.hideturtle()
gay_theme_button.hideturtle()
leaderboard_button.hideturtle()
highscore_button.clear()
pve_button.clear()
pvp_button.clear()
normal_theme_button.clear()
epileptic_theme_button.clear()
gay_theme_button.clear()
leaderboard_button.clear()
turtle_start.clear()
turtle_question.clear()
turtle_theme.clear()
window.bgcolor("black")
window.update()
