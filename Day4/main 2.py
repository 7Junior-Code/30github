import math
print("My math Lucky number is", round(math.pi,3))
print('''                     Welcome to
                 FAST and THE MOST ACCURATE

_________      ______            ______      _____              
__  ____/_____ ___  /_________  ____  /_____ __  /______________
_  /    _  __ `/_  /_  ___/  / / /_  /_  __ `/  __/  __ \_  ___/
/ /___  / /_/ /_  / / /__ / /_/ /_  / / /_/ // /_ / /_/ /  /    
\____/  \__,_/ /_/  \___/ \__,_/ /_/  \__,_/ \__/ \____//_/ 
'''*2)
ope_tor = input('Enter an operator ("+" "-" "x" "/" "**")')
if ope_tor == "/":
  print("A Perfect Calculator with remainders shown!!!")
  dividant = (float(input("Enter the dividant: ")))
  divisor = (float(input("Enter the divisor: ")))
  print(math.floor (dividant/divisor), "r.", dividant%divisor)
  print("Solved Succesfully!🙋")
elif ope_tor == "+":
  print("Welcome to Addition Calculator")
  num1 = (float(input("Enter the number: ")))
  num2 = (float(input("Enter the number: ")))
  print(round(num1 + num2,3))
  print("Solved Succesfully!🙋")
elif ope_tor == "x":
  print("Welcome to Multiplication Calculator")
  num1 = (float(input("Enter the number: ")))
  num2 = (float(input("Enter the number: ")))
  print(round(num1 * num2,3))
  print("Solved Succesfully!🙋")
elif ope_tor == "**":
  print("Perfect Calculator with perfect answer!")
  num1 = (float(input("Enter the main number: ")))
  num2 = (float(input("Enter the small number on top right corner: ")))
  print(num1**num2)
  print("Solved Succesfully!🙋")
elif ope_tor == "-":
  print("Welcome to Subtraction Calculator!")
  num1 = (float(input("Enter the number: ")))
  num2 = (float(input("Enter the number: ")))
  print(num1 - num2)
  print("Solved Succesfully!🙋")
else:
  print("Error py.math Wrong Number or wrong operator")