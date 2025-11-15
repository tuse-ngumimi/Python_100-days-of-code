import random
from menu import atm_menu   

ACCOUNT_NUMBER_DIGITS = 11

def create_acc():
    name = input("Enter your full name: ").title()
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are not old enough. Account holder must be 18 or older.")
        return None

    acc_type = input("Select account type:\n1. Current Account\n2. Savings Account\n")
    while acc_type not in ["1", "2"]:
        acc_type = input("Error! Select 1 (Current) or 2 (Savings): ")

    account_info = {
        "name": name,
        "age": age,
        "account_type": "Current" if acc_type == "1" else "Savings"
    }
    print(f"\nAccount created successfully!\n{account_info}")
    return account_info


def create_pin() -> str:
    while True:
        pin = input("Create a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            if pin in ["0000", "1234"]:
                print("This PIN cannot be used for security reasons.")
            else:
                print("PIN successfully created!")
                return pin
        else:
            print("Invalid PIN. It must be exactly 4 digits.")


def account_num() -> str:
    acc_num = "10" + str(random.randint(10**(ACCOUNT_NUMBER_DIGITS-3), 10**(ACCOUNT_NUMBER_DIGITS-2) - 1))
    print(f"Your account number is: {acc_num}")
    return acc_num


if __name__ == "__main__":
    user = create_acc()
    if user:
        pin = create_pin()
        account_num()
        print("\nRedirecting you to ATM menu...\n")
        atm_menu()   
