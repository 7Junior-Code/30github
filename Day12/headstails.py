
import time
import random
from asciiart import world, football_ball

spin = random.randint(1, 2)
print(world, "\n"*10, football_ball)
print("---HEADS OR TAILS GAME---")

if spin == 1:
    time.sleep(4)
    print("-----HEADS-----")
    print(world)

elif spin == 2:
    time.sleep(4)
    print(football_ball)
    print("-----TAILS-----")