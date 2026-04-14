print("You woke up in a locked room. In front of you is a book of riddles. Answer the 5 riddle toescape.")
peom1=input("What is the land animal that does not normally walk, and carries its family with it?")
if peom1=="kangaroo":
    peom2=input("Congrats! What word becomes shorter when you add 2 letters?")
    if peom2=="short":
        peom3=input("Congrats! What happens once a minute, twice a moment, but never in a million years?")
        if peom3=="M":
            peom4=input("Congrats!What gets shorter the older it gets?")
            if peom4=="candle":
                peom5=input("What is something you can catch but not throw?")
                if peom5=="a cold":
                    print("Good job! You solved all 5 riddles!!!")

if peom1!="kangaroo":
    print("Oops! Restart. You might have capitalized the first letter. Don't add a space!")
    exit(1)
if peom2!="short":
    print("Oops! Restart. You might have capitalized the first letter. Don't add a space!")
    exit(1)
if peom3!="M":
    print("Oops! Restart. You might have not capitalized the first letter. Don't add a space!")
    exit(1)
if peom4!="candle":
    print("Oops! Restart. You might have capitalized the first letter. Don't add a space!")
    exit(1)
if peom5!="a cold":
    print("Oops! Restart. You might have capitalized the first letter.")
    exit(1)