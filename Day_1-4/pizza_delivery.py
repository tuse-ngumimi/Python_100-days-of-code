#Version 1
print("Welcome to Python Pizza Delivery")

size : int = input("What pizza size would you like to order? [S / M / L] ")
pepperoni : int = input("Do you want pepperoni on your pizza? [Y / N] ")
extra_cheese : int = input("Would you like extra cheese? [Y / N] ")

bill = 0

if size == "S":
  bill = 15
  if pepperoni == "Y":
    bill += 2
    if extra_cheese == "Y":
      bill += 1
      print(f"You ordered a small pizza with pepperoni and extra chesse. Your total bill is ${bill}")
    elif extra_cheese == "N":
      print(f"You ordered a small pizza with pepperoni. Your total bill is ${bill}")
  elif pepperoni == "N":
    print(f"You ordered a small pizza withot pepperoni. Your total bill is ${bill} ")
elif size == "M":
  bill = 20
  if pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1
      print(f"You ordered a medium pizza with pepperoni and extra chesse. Your total bill is ${bill}")
    elif extra_cheese == "N":
      print(f"You ordered a medium pizza with pepperoni. Your total bill is ${bill}")
  elif pepperoni == "N":
    print(f"You ordered a medium pizza withot pepperoni. Your total bill is ${bill} ")
elif size == "L":
  bill = 25
  if pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1
      print(f"You ordered a large pizza with pepperoni and extra chesse. Your total bill is ${bill}")
    elif extra_cheese == "N":
      print(f"You ordered a large pizza with pepperoni. Your total bill is ${bill}")
  elif pepperoni == "N":
    print(f"You ordered a large pizza withot pepperoni. Your total bill is ${bill} ")


#Version 2
print("Welcome to Python Pizza Delivery")

size = input("What pizza size would you like to order? [S / M / L] ").upper()
pepperoni = input("Do you want pepperoni on your pizza? [Y / N] ").upper()
extra_cheese = input("Would you like extra cheese? [Y / N] ").upper()

bill = 0

# Base price
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size selected.")
    exit()

# Add-ons
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
