amount : float = 0.00  

def atm_menu():
    global amount

    while True:
        option = input("\nWhat would you like to do today?\n"
                        "1. Check balance\n"
                        "2. Deposit\n"
                        "3. Withdraw\n"
                        "4. Exit\n")

        if option == "1":
            check_balance()
        elif option == "2":
            deposit()
        elif option == "3":
            withdraw()
        elif option == "4":
            print("Thank you for using our ATM services. Goodbye!")
            break
        else:
            print("Invalid option! Please select 1, 2, 3, or 4.")


def check_balance():
    print(f"Your balance is ₦{amount:.2f}")


def deposit():
    global amount
    try:
        deposit_amount = float(input("Enter amount to deposit: ₦"))
        if deposit_amount >= 50:
            amount += deposit_amount
            print(f"₦{deposit_amount:.2f} deposited successfully! New balance: ₦{amount:.2f}")
        else:
            print("Minimum deposit is ₦50.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def withdraw():
    global amount
    try:
        withdraw_amount = float(input("Enter amount to withdraw: ₦"))
        if withdraw_amount > amount:
            print("Insufficient balance.")
        elif withdraw_amount <= 49.99:
            print("Withdrawal amount must not be less than 50 naira.")
        else:
            amount -= withdraw_amount
            print(f"₦{withdraw_amount:.2f} withdrawn successfully! New balance: ₦{amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")
