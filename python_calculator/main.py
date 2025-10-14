from menu import print_menu
from inputs import input_operation, input_float
from math import log, exp

def calculator() -> None:
    print_menu()
    (choice, operation) = input_operation()
    print(f"\nYou have selected {operation}\n")
    if choice == 0:
        num1: float = input_float("Enter num1: ")
        num2: float = input_float("Enter num2: ")
        result: float = num1 + num2
        print(f"Result is {result:.3f}")
    elif choice == 1:
        num1 = input_float("Enter num1: ")
        num2 = input_float("Enter num2: ")
        result = num1 - num2
        print(f"Result is {result:.3f}")
    elif choice == 2:
        num1 = input_float("Enter num1: ")
        num2 = input_float("Enter num2: ")
        result = num1 * num2
        print(f"Result is {result:.3f}")
    elif choice == 3:
        num1 = input_float("Enter num1: ")
        num2 = input_float("Enter num2: ")
        result = num1 / num2
        print(f"Result is {result:.3f}")
    elif choice == 4:
        num1 = input_float("Enter num1: ")
        num2 = input_float("Enter num2: ")
        result = num1 // num2
        print(f"Result is {result:.3f}")
    elif choice == 5:
        num1 = input_float("Enter num1: ")
        num2 = input_float("Enter num2: ")
        result = num1 % num2
        print(f"Result is {result:.3f}")
    elif choice == 6:
        base: float = input_float("Enter base: ")
        num: float = input_float("Enter num: ")
        result = log(num, base)
        print(f"Result = {result:.3f}")
    elif choice == 7:
        num = input_float("Enter num: ")
        result = exp(num)
        print(f"Result = {result:.3f}")
    elif choice == 8:
        base = input_float("Enter base: ")
        num = input_float("Enter num: ")
        result = num ** base
        print(f"Result = {result:.3f}")
    else:
        base = input_float("Enter base: ")
        num = input_float("Enter num: ")
        result = num ** (1/base)
        print(f"Result = {result:.3f}")

def main() -> None:
    while True:
        calculator()
        response: str = input("Do you wish to perform another calculation: ['yes']/['no']: ")
        response = response.lower()
        if response == 'yes' or response == 'ye' or response == 'y':
            continue
        break
    
    # return None
    # return


# a code snippet that makes python
# run a main function in the same
# manner as a statically typed language
if __name__ == "__main__":
    main()