
import random
import time
import pygame

s_defeat = "Game over.wav"
s_winner = "cheering.wav"

words = ("apple",
         "rock",
         "stars",
         "palace",
         "python",
         "magic",
         "hotel",
         "bed",
         "tv",
         "animal",
         "officer",
         "clown",
         "trap",
         "presents",
         "winter",
         "vacation")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def defeat_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(s_defeat)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def winner_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(s_winner)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def display_man(wrong_guesses):
    print("######")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("######")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("Letter already guessed")
            continue

        guessed_letters.add(guess)

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            print("\n")
            display_man(wrong_guesses)
            display_answer(answer)
            print("🪢🐥YOU WIN 🏆🎉")
            winner_sound()
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("GAME OVER")
            defeat_sound()
            is_running = False


if __name__ == '__main__':
    main()