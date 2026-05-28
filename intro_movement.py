import time, turtle, random
from utils import *
# Section 1: Setup
set_background("White")
s1 = create_sprite("Pencil3",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+5)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-5)
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-5, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+5, y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 3: define other controls
# def hide():
#     s1.hideturtle()
# def show():
#     s1.showturtle()

# window.onkeypress(hide, "h")
# window.onkeyrelease(show, "h")

def draw():
    s1.pendown()
window.onkeypress(draw, "q")

def stop_drawing():
    s1.penup()
window.onkeypress(stop_drawing, "r")

def erase():
    s1.clear()
window.onkeypress(erase, "e")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()