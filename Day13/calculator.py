
import asciiart

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
}

def calculator():
    print(asciiart.l_calculator)
    continue_calculate = True

    first_n = float(input("Enter your first number: "))

    while continue_calculate:
        for symbol in operations:
            print(symbol)
        operation = input("Enter an operation: ")
        second_n = float(input("Enter your second number: "))

        answer = operations[f"{operation}"](first_n, second_n)
        print(f"{first_n} {operation} {second_n} = {answer}")

        continue_opt = input("Enter (Y) to continue calculating and (N) to make a new calculation: ").upper()
        if continue_opt == "Y":
            first_n = answer
        else:
            continue_calculate = False
            print("\n" * 40)
            calculator()


calculator()
