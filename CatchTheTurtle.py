import turtle
from random import randint
import random


screen = turtle.Screen()
screen.bgcolor("light sky blue")
screen.title("Catch The Turtle")
score = 0
game_over = False 

Style = ('Arial', 23, 'italic')

# Turtle List
turtle_list = []

# Countdown Turtle
countdown_turtle = turtle.Turtle()

# Score Turtle 
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score : 0", move=False, align="center", font= Style )



grid_size = 10

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_clik(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score : {score}", move=False, align="center", font= Style )

         
        #print(x,y)

    t.onclick(handle_clik)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("indian red")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


# Make Turtle Properties
x_cordinates = [-20, -10, 0, 10, 20]
y_cordinates = [20, 10, 0, -10, -20]


def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


# recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setposition(0, y)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time : {time}", move=False, align="center", font= Style )
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg=f"Game Over!", move=False, align="center", font= Style )



def start_game_up():
    turtle.tracer(0)

    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(15)

    turtle.tracer(1)

start_game_up()
turtle.mainloop()