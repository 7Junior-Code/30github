
def balance():
    print(f"Your balance: {balance}")


def income():
	print("**************************")
	amount = float(input("Enter your income: $"))
	print("**************************")
	
	if amount < 0:
	    print("That's NOT a valid amount")
	    return 0
	else:
	    return amount
def outcome():
    print("**************************")
    amount = float(input("Enter your outcome: $"))
    print("**************************")
    
    if amount < 0:
        print("That's NOT a valid amount")
        return 0
    else:
        return amount
    
    


is_running = True

balance = float(input("Enter your amount now: "))
while is_running:
    print("**************************")
    print("   COIN COUNTER Program   ")
    print("**************************")
    
    print("1. Show Balance")
    print("2. Income")
    print("3. Outcome")
    print("4. Exit")
    menu = input("Choose an option (1-4): ")
    
    if menu == "1":
        print(f"Your current balance is: ${balance:.2f}")
        
    elif menu == "2":
        balance += income()
        
    elif menu == "3":
        balance -= outcome()
    
    elif menu == "4":
        print("Have a good day! Bye")
        
    else:
        print("**************************")
        print("   COIN COUNTER Program   ")
        print("**************************")
        
        print("1. Show Balance")
        print("2. Income")
        print("3. Outcome")
        print("4. Exit")
        menu = input("Please choose an option (1-4): ")