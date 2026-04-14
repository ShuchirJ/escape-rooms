inventory=[("pink pony", "makes you fly"),("red dog toy","makes random noises")]
escaped= True # player gets through
escaped= False # player is stuck
print("===The abondaned classroom===")
print("all the lights are out exepet one dim light in the corner")
print("there is a math problem on the black board")
print("you hear little cries of childern in the corners")
answer=input("what is 3210987654321+2314567892=?")
if answer=="3.2133022e+12":
    escaped=True
    print()
if escaped:
    print("The door unlocks.YOU ARE FREEEEEEEEEEE")
else:
    print("The little kids come out of the corners.YOU HAVE BECOME ONE OF THE KIDS")