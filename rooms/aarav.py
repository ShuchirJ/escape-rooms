print ("Welcome to Aarav’s  Escape room")
print ("you will probably fail")
print ("type everything in lowercase")
escaped = False
inventory = ["rusty key", "shovel", "human finger", "morse code sheet 1", "morse code sheet 2"
,  "morse code sheet 3", "uv light"]


print ("You have",inventory)

print ("To power the flashlight to see, you have to burn two morse code sheets")
morse = input("which Sheet are you keeping")
if "morse" == 1:
    del inventory[4:6]
if "morse" == 2:
    del inventory[3:3]
    del inventory[5:5]
if "morse" == 3:
    del inventory[3:3]
    del inventory[4:4]
finger = input("you walk to the door but find out that you need a fingerprint. What do you do?")
if finger == "i use the human finger":
    del inventory [2:2]
else:
   print ("you failed")
   print ("You stay there for 3 days and die")
   exit(1)
print ("you opened the door")
print ("You encounter a dead end made of dirt.")
dig = input("What do you do")
if dig == "i use the shovel to remove the dirt":
    print ("You dig until you see a manhole cover. You have to leave the shovel")
    del inventory [1:1]
else:
   print ("you failed")
   print ("You stay there for 3 days and die")
   exit(1)
blackroom = input("You find a dark room. What do you do")
if blackroom == "i use the uv light":
   print ("You see the words, I will play morse code now.")
else:
   print ("you failed")
   print ("You stay there for 3 days and die")
   exit(1)


   if inventory.includes ("morse code sheet 3"):
        print ("you have chosen the correct morse code sheet so now you can decode the message")
   else:
      print ("you failed")
      print ("You stay there for 3 days and die")
      exit(1)

print ("You decode the message and you go to the third door")
key = input("what do you do?")
if key == "use the key":
   print ("You open the door and escape")
else:
   print ("you failed")
   print ("You stay there for 3 days and die")
   exit(1)


escaped = True
if escaped == True: 
   print ("You have completed the entire escape room")
   

