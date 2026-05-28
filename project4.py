from utils import *

# Section 1 - setup
#set a background using set_background()
set_background("cold")
#create at least two variables and set their starting value. ex: cookies = 0
fish = 0

health = 100


#creates the penguin
p2 = create_sprite("Pen", 0,80)
#w3 = create_sprite("KillerWhale", -200,0)

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -300,200)
m1.hideturtle()

m2 = create_sprite("fish", -200,180)
m2.hideturtle()

m3 = create_sprite("alien", -300,190)
m3.hideturtle()

m4 = create_sprite("alien", 0,180)
m4.hideturtle()
# Section 2 - controls
# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
fish_list = []


# TODO - make a second control

def make_fish():

#a3 = create_sprite("pointer", 300 0)
    global fish 
    global health
    fish += 1
    health +=10
   #fish is created in the sky
    x1 = random.randint (-200,200)
    y1 =200
    t1 = create_sprite("fish",x1,y1)
    fish_list.append(t1)
    #y = random.randint (-200,200)
    #create_sprite ("fish",x,y)
window.onkeypress(make_fish, "space")

def hi():
    m2.write("hi")


#writes hi after you press h
window.onkeypress(hi,"h")


def change_health():
    global health
    health -= 1
# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here
    #fish drops downwards from the sky.
    for t1 in fish_list:
        x1 = t1.xcor()
        y1 = t1.ycor()
        y1 -=10

        t1.goto(x1, y1)

    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"Fish:{fish}")
    m3.clear()
    m3.write(f"health:{health}")

    if i % 10 == 0:
        change_health()

    time.sleep(0.01)
    window.update()


    if health == 0:
        print("you lose")


