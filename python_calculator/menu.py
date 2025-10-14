OPERATIONS = [
  "Addition \n",
  "Subtraction \n",
  "Multiplication \n",
  "Division \n",
  "Floor Division \n",
  "Modulus \n",
  "Logarithm \n",
  "Exponent \n",
  "Power \n",
  "Root"
]

print(OPERATIONS)

def print_menu() -> None:
  print("WELCOME TO THE SIMPLE ARITHMETIC CALCULATOR")
  print("Select an operation from the following")
  for i in range(10):
    count : int = i + 1
    operation = OPERATIONS[i] #the indexing begins from i i.e 0 and not num which will begin with i+1 
    print(f"{count}. {operation}")
  print()

if __name__ == "__main__":
  print_menu() # this line of code catches the func call so that this call won't run
                #in any other python program it is imported in. It also prevents demo/test code for running where it is imported to.

# OPERATIONS: list[str] = [
#     "Addition",
#     "Subtraction",
#     "Multiplication",
#     "Division",
#     "Floor Division",
#     "Modulus",
#     "Logarithm",
#     "Exponent",
#     "Power",
#     "Root",
# ]


# def print_menu() -> None:
#     print("Welcome to the Calculator.")
#     print("Select an operation from the following")
#     print()
#     # range(start, stop, step)
#     # range(start, stop) step = 1
#     # range(stop) start = 0, step = 1
#     # start = 0, stop = 10, step = 1
#     for i in range(10):
#         num: int = i + 1
#         operation = OPERATIONS[i]
#         print(f"{num}. {operation}")
#     print()

# # This function is for Sodiq
# def slap() -> None:
#     print("Capon slapped Sodiq")

# # Guard any tests that you write in the menu.py
# # So that it is not run when you import stuff
# # from it
# if __name__ == "__main__":
#     print_menu()
#     slap()

# # print_menu()
# # slap()