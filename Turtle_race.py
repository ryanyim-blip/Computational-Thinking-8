import turtle, time, random
from utils import *
import time
# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-200
y1 =225
x2 =-200
y2 =75
x3 =-200
y3 =-75
x4 =-200
y4 =-225


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("grid")
t1 = create_sprite("astronaut",x1,y1)
t2 = create_sprite("alien",x2,y2)
t3 = create_sprite("balloon",x3,y3)
t4 = create_sprite("baseball",x4,y4)

# section 2.5 - prediction
print("Hello, I want you to guess who will win")
print("astronaut: 4*10-6+16+5÷11+5")
#equation answer is 10
print("alien: ???")
print("balloon: 8+8-5*7÷11")
#equation answer is 7
print("baseball: ∞")
predict = input("please write who you think will win. 1. astronaut 2. alien 3. balloon 4. baseball")
time.sleep(5)
# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(40):
     x1 +=10
     #astronaut moves 10
     x2 +=-5
     #alien goes backwards
     y3 +=7
     #instead of moving on the x axis, the balloon moves upwards on the y axis because its a balloon.
     x4 +=100
     #baseball moves 100

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("astronaut wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
     print("alien wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
     print("balloon wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
     print("baseball wins!")

if predict == "1": print("sorry astronaut didn't win :(")
if predict == "2": print("um... I don't really know if alien won or not. They might have escaped the matrix so yeah I guess they won???")
if predict == "3": print("into the sky!!!")
if predict == "4": print("zoom!!!")
turtle.exitonclick()