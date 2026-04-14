
print("solve this riddle: my sister cannot be with me, and my home is deep within the earth.")
#answer is lava
escaped=0
x=input("answer: ")
if x == "lava":
    escaped=escaped+1
elif x!= "": 
    print("you lose!")
    exit(1)
    
if (escaped == 1):
    print("x^2+1=0")
    q2 = input("answer: ")    
        
else:
    print("you lose!")
    exit(1)
if (q2 == "i"):
    print("who won the 戦国時代")
    q3 = input("answer: ")
if (q3 == "Tokugawa"):
    print("In a 256 bit block of data using hamming codes for error correction, how many hamming")
    print("bits will be used?")
    q4 = input("answer: ")
if (int(q4) == 8):
    print("For how long was Firework #1 on the Pointercrate Demonlist?")
    q5 = input("answer: ")
if(q5 == "18 seconds"):
        print("what number am I thinking of right now?")
        q6=input("answer: ")
if(q6 == "π"):
    print("you win!")