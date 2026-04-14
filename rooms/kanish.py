import time
first = int(input("are you ready, 1 is yes and 2 is no"))
if first == 1:
  print("you have been kidnapped and overheard that you will be transported elseware in 12 hours. you are in a safehouse in the other side of town. you must escape before the time and inform the cops of this.")
  time.sleep(2)
  second = input("you have a pocket knife(1), some firecrackers(2), and a hairpin(3). the door has two locks and one only uses a pin number. you are really good at engineering and made a number generator to crack these locks. what do you do.  A - try to break the window that randomly spawned or B - try to break a lock")
  if second == "A":
    print("you broke out, but you were coaught by gaurds and were transported")
  elif second == "B":
    print("you could not break out, so you kick the door down. it was only secured on one hinge. you find a phone and call 911. you make it out alive and are sent home through attack helicopter. btw you are the president of AMERICA.")
    escaped = True