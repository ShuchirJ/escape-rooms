print("~~ANIKA'S ESCAPE ROOM~~")
print("You are trapped in a room full of doors.")
inventory = [("flashlight", "lights the way", "useless map", "leads you in the wrong direction")]

answer = input("What has a tongue but no mouth?")
if answer == "shoe":
    escaped = True
    answer = input("Correct! What type of room has no doors nor windows? ")
    if answer == "mushroom":
        escaped = True
        answer = input("Hooray! You escaped this escape room!")
    if answer != "mushroom":
        escaped = False
        answer = input("Sorry, no. You looked around you and you were amazed to see the world of dinosaurs (u died")
if answer != "shoe":
    escaped = False
    answer = input("Nope, you are suroounded by alligators now. You gonna trick them? (Yes/No)")
    if answer == "Yes":
        escaped = True
        answer = input("Hooray! You escaped this escape room!")
    if answer != "Yes":
        escaped = False
        answer = input("Sry, you died!")
      
