
import pygame
import time

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
           ("A. Antarctic", "B. North pole", "C. Australia"),
           ("A. Dogs", "B. Cats", "C. Flies"))

answers = ("C", "C", "B", "A", "C", "A", "B", "A", "B")
guesses = []
score = 0
question_num = 0

s_correct = "cheering.wav"
s_wrong = "Game Over.wav"

def correct_sound(duration):
    pygame.mixer.init()
    pygame.mixer.music.load(s_correct)
    pygame.mixer.music.play(duration)
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def wrong_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(s_wrong)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

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
        correct_sound(1)

    else:
        print("-----INCORRECT!-----")
        print(f"{answers[question_num]} is the correct answer")
        wrong_sound()

    question_num += 1
print("Finished")
print(f"Your Score: {score}/9")
correct_sound(1)