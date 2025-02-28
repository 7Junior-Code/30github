
import random

print("Python challenge answers:")
print("Challenge 1:")
print(sum(range(1, 101)))

print("Challenge 2:")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")