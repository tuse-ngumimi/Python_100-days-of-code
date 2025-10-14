# from menu import OPERATIONS

# def input_num(prompt: str, max_trials: int = 5) -> int:
#     """
#     Prompts a user to enter a number and returns the response if valid.
#     """
#     for _ in range(max_trials):
#         response: str = input(prompt)
#         if response.isdigit():
#             return int(response)
#         else:
#             print("User response is not valid. Please try again")

#     print(f"User failed to enter a valid input after {max_trials} trials")
#     exit()


# def input_operation(prompt: str, max_trials: int = 5) -> tuple[int, str]:
#     """
#     Prompts a user to choose an operation from OPERATIONS by entering a number.
#     Returns (index, operation) if valid.
#     """
#     for _ in range(max_trials):
#         response: int = input_num(prompt)
#         if response <= 0:
#             print("Invalid input. Please enter a positive number")
#         elif response <= len(OPERATIONS):
#             idx: int = response - 1
#             return idx, OPERATIONS[idx]
#         else:
#             print("Invalid input. Please enter a valid number")

#     print(f"User failed to enter a valid input after {max_trials} trials")
#     exit()


# def input_float(prompt: str, max_trials: int = 5) -> float:
#     """
#     Prompts a user for a float input (supports commas, negatives, and decimals).
#     """
#     for _ in range(max_trials):
#         response: str = input(prompt)
#         response = response.replace(",", "")   # remove commas
#         response_raw: str = response.replace(".", "").replace("-", "")

#         if response_raw.isdigit():
#             return float(response)
#         else:
#             print("Invalid value format. Please try again.")

#     print(f"User failed to enter a valid float after {max_trials} trials")
#     exit()


# if __name__ == "__main__":
#     value = input_operation("Choose an operation: ")
#     print("You chose:", value)


from menu import OPERATIONS


def input_num(prompt: str, max_trials: int = 5) -> int:
    """
    `input_num` prompts a user to enter a number and returns the user response if it is valid.

    Args:
        prompt: (str) - The message displayed to the user before requesting user input

        max_trials: (int, optional) - The number of times the program will attempt user input. If the number of trials exceeds this value, the program stops. Defaults to 5.

    Returns:
        (int) - The user response as an integer.
    """
    for _ in range(max_trials):
        response: str = input(prompt)
        if response.isdigit():
            return int(response)
        else:
            print("User response is not valid. Please try again")
        # if not response.isdigit():
        #     print("User response is not valid. Please try again")
        #     continue
        # return int(response)
    print(f"User failed to enter a valid input after {max_trials} trials")
    exit()


def input_operation(max_trials: int = 5) -> tuple[int, str]:
    """
    `input_operation` prompts the user to enter a matching operation number to the list of operations. Returns the matched operation index and the operation itself as a tuple if the user response is valid.

    Args:
        max_trials: (int, optional) - The maximum number of times the program will prompt the user to enter an operation number. Defaults to 5.

    Returns:
        (tuple[int, str]) - a tuple containing the index of the matched operation and the value of the matched operation.
    """
    for _ in range(max_trials):
        response: int = input_num("Enter an operation number: ")
        if 1 <= response <= len(OPERATIONS):
            idx: int = response - 1
            return idx, OPERATIONS[idx]
        else:
            print(
                f"User response is not valid. Expected a response between 1 - {len(OPERATIONS)}. Please try again"
            )
    print(f"User failed to enter a valid input after {max_trials} trials")
    exit()

def input_float(prompt: str, max_trials: int = 5) -> float:
    for _ in range(max_trials):
        response: str = input(prompt)
        # response = "100,000.20"
        response = response.replace(",", "")
        # response = "100000.20"
        response_raw: str = response.replace(".", "").replace("-", "")
        # response_raw = "10000020"
        if response_raw.isdigit():
            return float(response)
        else:
            print("User response is not valid. Please try again.")
    
    exit()


if __name__ == "__main__":
    value = input_float("Enter a number: ")
    print(value)
    print(type(value))
