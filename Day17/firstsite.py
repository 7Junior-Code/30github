import random
import time

name = input("\n Hello, what's your name: ")
name = name.capitalize()
print(f"Hello {name} \n")

center = input(
    f"What do you want {name} (Write only the options Example: A )?: \n A) Calculator B) Cart C) Timer D) Quiz E) Games: ").upper()

if center == "A":

    import math

    print("\n \n My math Lucky number is", round(math.pi, 3))
    print('''                     Welcome to
                     FAST and THE MOST ACCURATE

    _________      ______            ______      _____              
    __  ____/_____ ___  /_________  ____  /_____ __  /______________
    _  /    _  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/
    / /___  / /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /    
    \____/  \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/ 
    ''')

    ope_tor = input('Enter an operator ("+" "-" "x" "/" "**") ')
    if ope_tor == "/":
        print("A Perfect Calculator with remainders shown!!!")
        dividant = (float(input("Enter the dividant: ")))
        divisor = (float(input("Enter the divisor: ")))
        print(math.floor(dividant / divisor), "r.", dividant % divisor)
        print("Solved Succesfully!🙋")
    elif ope_tor == "+":
        print("Welcome to Addition Calculator")
        num1 = (float(input("Enter the number: ")))
        num2 = (float(input("Enter the number: ")))
        print(round(num1 + num2, 3))
        print("Solved Succesfully!🙋")
    elif ope_tor == "x":
        print("Welcome to Multiplication Calculator")
        num1 = (float(input("Enter the number: ")))
        num2 = (float(input("Enter the number: ")))
        print(round(num1 * num2, 3))
        print("Solved Succesfully!🙋")
    elif ope_tor == "**":
        print("Perfect Calculator with perfect answer!")
        num1 = (float(input("Enter the main number: ")))
        num2 = (float(input("Enter the small number on top right corner: ")))
        print(num1 ** num2)
        print("Solved Succesfully!🙋")
    elif ope_tor == "-":
        print("Welcome to Subtraction Calculator!")
        num1 = (float(input("Enter the number: ")))
        num2 = (float(input("Enter the number: ")))
        print(num1 - num2)
        print("Solved Succesfully!🙋")
    else:
        print("                             😵   ")
        print("                         Error 404")
        print("            Error py.math Wrong Number or wrong operator")

elif center == "B":
    import time

    items = []
    prices = []

    new = input("\n Welcome to A+ Shopping Cart!(q to quit, any answer to continue)")

    while True:
        if new.lower() == "q":
            for x in reversed(range(1, 10, 2)):
                print("        ___")
                time.sleep(2)
                print(f"       |_{x}_|", end=" ")
                print()
            time.sleep(1)
            print()
            print("                          🙋!Bye!🙋")
            print()
            print("                        See You Soon!")
            break

        item = input("Enter an item to buy (c for going to  cashier and q to quit): ")
        if item.lower() == "q":

            for x in reversed(range(1, 10, 2)):
                print("        ___")
                time.sleep(2)
                print(f"       |_{x}_|", end=" ")
                print()
            time.sleep(1)
            print()
            print("                          🙋!Bye!🙋")
            print()
            print("                        See You Soon!")
            break
        elif item.lower() == "c":
            print()
            print("Going and waiting for the cashier line.  ")
            time.sleep(1)
            print()
            print("Going and waiting for the cashier line . ")
            time.sleep(1)
            print()
            print("Going and waiting for the cashier line  .")
            time.sleep(1)
            print()
            print("Going and waiting for the cashier line.  ")
            time.sleep(1)
            print()
            review = print("Check-cart before the casheer step:")
            time.sleep(1)
            print(f"You have {total_i} items in your cart")
            print(f"They cost ${total_p} in total")
            time.sleep(2)
            end = input("Would you like to buy the items? (Y/N)")
            if end.lower() == "y":
                for x in reversed(range(1, 10, 2)):
                    print("        ___")
                    time.sleep(2)
                    print(f"       |_{x}_|", end=" ")
                    print()
                time.sleep(1)
                print()
                print("                          🙋!Bye!🙋")
                print()
                print("                        See You Soon!")
                break
            else:
                continue

        else:
            price = float(input(f"Enter the price of a/an {item}: $"))
            items.append(item)
            prices.append(price)
            total_i = len(items)
            total_p = sum(prices)

elif center == "C":
    import time

    print('''   Welcome to Universe Spark
     _______              
    /_  __(_)_ _  ___ ____
     / / / /  ' \/ -_) __/
    /_/ /_/_/_/_/\__/_/   
                          ''')

    set_time = int(input("Enter the time in seconds: "))
    set_time = set_time + 1
    for flash in reversed(range(1, set_time)):
        secs = flash % 60
        mins = int(flash / 60) % 60
        hours = int(flash / 3600)

        print(f"{hours:02}:{mins:02}:{secs:02}")
        time.sleep(1)
    for x in reversed(range(1, 17)):
        print("TIME'S UP!", end="         ")
    for slashed in range(1, 11):
        print(() * 3)
        print(slashed, end=" ")

elif center == "D":
    questions = ("What is my favorite collour?",
                 "What is my favourite planet after Earth?",
                 "What country am I from?",
                 "The biggest country in the whole continent of America is:",
                 "The smallest country in the world is:",
                 "What is the longest lasting country in the world?",
                 "What is the longest lasting country flag in the world?",
                 "What is the only region that doesn't have bees?",
                 "The pet with the fastest reaction time?")

    options = (("A. Black", "B. Green", "C. Blue"),
               ("A. Neptune", "B. Jupiter", "C. Mars"),
               ("A. Kazakhstan", "B. Kyrgyzstan", "C. China"),
               ("A. Canada", "B. USA", "C. Brazil"),
               ("A. San-Marino", "B. Vaticans", "C. Vatican City"),
               ("A. Japan", "B. Republic of China", "C. Italy"),
               ("A. Switzerland", "B. Denmark", "C. Saudi Arabia"),
               ("A.Antarctic", "B. North pole", "C. Australia"),
               ("A. Dogs", "B. Cats", "C. Flies"))

    answers = ("C", "C", "B", "A", "C", "A", "B", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------------------------------------------")
        print(f"Question {question_num}/8")
        print(f"Your Score: {score}/{question_num}")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("-----CORRECT!-----")
        else:

            print("-----INCORRECT!-----")
            print(f"{answers[question_num]} is the correct answer")

        question_num += 1
    print("Finished")
    print(f"Your Score: {score}/9")

elif center == "E":
    gm = input("What Unknown game do you choose: (A) (B) (C): ").upper()
    options = ["A", "B", "C", "D"]

    if gm == "A":
        print("----------MAD LIBS GAME----------")
        one = input("Enter a noun (Person, thing or place): ")
        two = input("Enter an adjective (describing the noun): ")
        three = input("Enter an adjective (describing the noun): ")
        four = input("Enter a noun (Person, thing or place): ")
        five = input("Enter a verb (an action): ")
        six = input("Enter a verb (an action): ")
        seven = input("Enter an adjective (describing the noun): ")
        eight = input("Enter an adjective (describing the noun): ")

        text = random.randint(1, 2)
        if text == 1:
            print("            The  Trip                 ")
            print(f"Today I went to {one} with my friends.")
            print(f"It was {two} and {three}.")
            print(f"There I saw {four}.")
            print(f"I asked if he was {five}")
            print(f"He was {six} and {seven}.")
            print(f"I felt {eight} that day!")
        else:
            print("          The Adventure              ")
            print(
                f"A {one} walked through the {two} forest, looking for a {three} {four}. It decided to {five} over to a {six}ing {seven}, hoping to find something {eight} inside.")

    elif gm == "B":
        print("\n The options are the words which have all their letters capitalized.  ")
        print("----------Treasure Island Game----------")
        print("--Your Mission is to find the TREASURE--")
        treasure = '''
            _________________________
          /                         /|
         /_________________________/ |
        |   ___________________    | |
        |  |                   |   | |
        |  |   o o o o o o o   |   | |
        |  |  o o o o o o o o  |   | |
        |  | o o o o o o o o o |   | |
        |  | o o o o o o o o o |   |/
        |  |___________________|   /
        |_________________________/ ________
        /   o o o o o o o o o o  / 00000000/
       /   o o o o o o o o o o  / 00000000/
      /   o o o o o o o o o o  / 00000000/
     /   o o o o o o o o o o  / 00000000/
    /   o o o o o o o o o o  /o0o0o0o0/
   |_________________________|        /
   | o o o o o o o o o o o o|        /
   | o o o o o o o o o o o o|       /
   | o o o o o o o o o o o o|      /
    \_______________________/ ____/
       o    o     o  o      o      
    o      o  o       o  o    o    
      o o       o o   o       o    
   o      o   o       o  o     o   
      o o      o    o    o  o      
   o    o   o     o      o '''

        game_over = '''
      |         O      O         |
       |          \____/          |
        |       /          \       |
       |      /            \      |
     |      \   X    X   /      |
    |        \__________/       | '''

        i = input("You are at a crosspath which way will you go LEFT or RIGHT: ").lower()

        if i == "right":
            o = input("There you see an island will you SWIM or WAIT for the boat: ").lower()

            if o == "wait":
                x = input(
                    "You enter a house there there are three rooms which one do you choose? RED or YELLOW or BLUE: ").lower()

                if x == "yellow":
                    print("\n ----------YOU WON---------- \n")
                    print(treasure)

                elif x == "red":
                    print("----------YOU LOST-----------")
                    print("The house was full of fire")
                    print(game_over)
                    print("\n ----------GAME OVER----------")

                elif x == "blue":
                    print("----------YOU LOST-----------")
                    print("--The house was full of ice--")
                    print(game_over)
                    print("\n ----------GAME OVER----------")

                else:
                    print("-------INVALID-------")

            if o == "swim":
                print("----------YOU LOST-----------")
                print(" --There was a shark nearby--")
                print(game_over)
                print("\n ----------GAME OVER----------")

            else:
                print("-------INVALID-------")

        elif x == "left":
            print("----------YOU LOST-----------")
            print("There was an angry toddler there.")
            print(game_over)
            print("\n ----------GAME OVER----------")

        else:
            print("-------INVALID-------")

    elif gm == "C":
        spin = random.randint(1, 2)
        print("---HEADS OR TAILS GAME---")

        if spin == 1:
            time.sleep(4)
            print("-----HEADS-----")

        elif spin == 2:
            time.sleep(4)
            print("-----TAILS-----")

    else:
        while gm not in options:
            gm = input("What Unknown game do you choose: (A) (B) (C) : ").upper()
else:
    center = input(
        f"What do you want {name} (Write only the options Example: A )?: \n A) Calculator B) Cart C) Timer D) Quiz E) Games: ").upper()


