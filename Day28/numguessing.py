""" Number Guessing game"""

""" We make our imports"""
import random
import pygame
import time
import art

""" Put our sound files"""
s_defeat = "Game over.wav"
s_winner = "cheering.wav"

""" Create functions to play those sounds"""
def game_won():
    pygame.mixer.init()
    pygame.mixer.music.load(s_winner)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def game_lost():
    pygame.mixer.init()
    pygame.mixer.music.load(s_defeat)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)



""" Function for the whole game with other functions inside it."""
def number_guessing():
    """ Global variable comes into the act"""
    lives = 1

    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5
    else:
        print("Error")


    def choose_random_num():
        """ This comment is inside a function.
         Here it chooses a random number between the range of (1-100)
         At the end it returns the number."""
        number = random.randint(1, 100)
        return number

    def user_guessings(lives):
        """ This function where we are inside.
         It is the rest of the game where user should guess the number."""
        """ We get the return from the choose_random_num function and 
         store it in a variable for later use."""
        answer = choose_random_num()


        """ Next we create a boolean and set it to be true and
         while it's true it's gonna follow the sequence of code in it till it's false."""
        not_guessed = True

        while not_guessed:
            user_guess = int(input("Enter a number (1-100): "))

            if user_guess != answer:

                if user_guess in range(1, 101):

                    if user_guess < answer:
                        print("  Too low\nTry Again")
                        lives -= 1
                        if lives == 0:
                            print("Game Over")
                            game_lost()

                    else:
                        print("  Too High \nTry Again")
                        lives -= 1
                        if lives == 0:
                            print("Game Over")
                            print(f"The answer was: {answer}")
                            game_lost()
                            not_guessed = False
                    print("    "*2, f"{lives}{art.life}")

                else:
                    print("Number out of range please try again:")

            else:
                print("You Won")
                game_won()
                not_guessed = False

    """ Make variable lives available in the function we are calling"""
    user_guessings(lives)

""" Program starts here: """
if __name__ == '__main__':
    """ User chooses level then goes to our game function."""
    level = input("Welcome to number guessing game choose a level please. (EASY | HARD): ").lower()
    number_guessing()
