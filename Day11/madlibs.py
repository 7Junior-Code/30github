
import random
import pygame
import time

s_winner = "cheering.wav"
def game_finished_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(s_winner)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

print("----------MAD LIBS GAME----------")
one = input("Enter a noun (Person, thing or place): ")
two = input("Enter an adjective (describing the noun): ")
three = input("Enter an adjective (describing the noun): ")
four = input("Enter a noun (Person, thing or place): ")
five = input("Enter a verb (an action): ")
six = input("Enter a verb (an action): ")
seven = input("Enter an adjective (describing the noun): ")
eight = input("Enter an adjective (describing the noun): ")
print("\n" * 50)

def the_trip(one, two, three, four, five, six, seven, eight):
    print("            The  Trip                 ")
    print(f"Today I went to {one} with my friends.")
    print(f"It was {two} and {three}.")
    print(f"There I saw {four}.")
    print(f"I asked if he was {five}")
    print(f"He was {six} and {seven}.")
    print(f"I felt {eight} that day!")
    game_finished_sound()

def the_adventure(one, two, three, four, five, six, seven, eight):
    print("          The Adventure              ")
    print(
        f"A {one} walked through the {two} forest, looking for a {three} {four}."
        f" It decided to {five} over to a {six}ing {seven}, hoping"
        f" to find something {eight} inside.")
    game_finished_sound()

text = random.randint(1, 2)

if text == 1:
    the_trip(one, two, three, four, five, six, seven, eight)
else:
    the_adventure(one, two, three, four, five, six, seven, eight)