Fear_of_Spiders_points = 0 
Fear_of_Hights_points = 0 
Fear_of_enclosed_spaces = 0

print("Hello, this is a quiz to guess your fears")
question1 = input("Would you rather be stuck inside of a tiny cave, a cave full of spiders or on an 200ft building?" 
" A. tiny cave B. cave of spiders. C 200ft building ")
if question1 == "A": 
    Fear_of_Spiders_points += 1
    Fear_of_Hights_points += 1
elif question1 == "B":
    Fear_of_enclosed_spaces += 1
    Fear_of_Hights_points
elif question1 == "C":
    Fear_of_enclosed_spaces += 1
    Fear_of_Spiders_points += 1
elif question1 == "":
    ("Please type your answer and A, B or C")
question2 = input("would you rather live in an apartment infested with spiders, live in an apartment high off the ground, or live in an apartment with a small celing?"
" A. Infested with spiders B. High off the ground C. Small ceiling")
if question1 == "A": 
    Fear_of_enclosed_spaces += 1
    Fear_of_Hights_points += 1
elif question1 == "B":
    Fear_of_enclosed_spaces += 1
    Fear_of_Spiders_points += 1
elif question1 == "C":
    Fear_of_Hights_points += 1
    Fear_of_Spiders_points += 1
elif question1 == "":
    ("Please type your answer and A, B or C")

question3 = input("would you rather have a pet taranchala, go to space for a day while witnessing the liftoff and landing, or weir a tight shirt"
"A. pet taranchala B. go to space C. Tight shirt")
if question1 == "A": 
    Fear_of_enclosed_spaces += 1
    Fear_of_Hights_points += 1
elif question1 == "B":
    Fear_of_Spiders_points += 1
    Fear_of_enclosed_spaces += 1
elif question1 == "C":
    Fear_of_Hights_points += 1
    Fear_of_Spiders_points += 1
elif question1 == "":
    ("Please type your answer and A, B or C")

question4 = input("")
if question1 == "A": 
    Fear_of_enclosed_spaces += 1
    Fear_of_Hights_points += 1
elif question1 == "B":
    Fear_of_Spiders_points += 1
    Fear_of_enclosed_spaces += 1
elif question1 == "C":
    Fear_of_Hights_points += 1
    Fear_of_Spiders_points += 1
elif question1 == "":
    ("Please type your answer and A, B or C")

question4 = input("")
if question1 == "A": 
    Fear_of_Spiders_points += 1
    Fear_of_Hights_points += 1
elif question1 == "B":
    Fear_of_enclosed_spaces += 1
    Fear_of_Hights_points
elif question1 == "C":
    Fear_of_enclosed_spaces += 1
    Fear_of_Spiders_points += 1
elif question1 == "":
    ("Please type your answer and A, B or C")

question5 = input("")
if question1 == "A": 
    Fear_of_Spiders_points += 1
    Fear_of_Hights_points += 1
elif question1 == "B":
    Fear_of_enclosed_spaces += 1
    Fear_of_Hights_points
elif question1 == "C":
    Fear_of_enclosed_spaces += 1
    Fear_of_Spiders_points += 1
elif question1 == "":
    ("Please type your answer and A, B or C")

if Fear_of_Spiders_points > Fear_of_Hights_points and Fear_of_Spiders_points > Fear_of_enclosed_spaces:
    print("")
elif Fear_of_Hights_points > Fear_of_Spiders_points and Fear_of_Hights_points > Fear_of_enclosed_spaces:
    print("")
elif Fear_of_enclosed_spaces > Fear_of_Spiders_points and Fear_of_enclosed_spaces > Fear_of_Hights_points:
    print("")
elif Fear_of_Spiders_points == Fear_of_Hights_points and Fear_of_Spiders_points > Fear_of_enclosed_spaces:
    print("")
elif Fear_of_enclosed_spaces == Fear_of_Spiders_points and Fear_of_enclosed_spaces > Fear_of_Hights_points:
    print("")
elif Fear_of_Hights_points == Fear_of_enclosed_spaces and Fear_of_Hights_points > Fear_of_Spiders_points:
    print("")
elif Fear_of_Spiders_points == Fear_of_Hights_points == Fear_of_enclosed_spaces:
    print("")

