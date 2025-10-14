# value : int = int(input("Enter any whole number: \n"))

# if value % 2 == 0:
#   print(f"{value} is an even number")
# else:
#   print(f"{value} is an odd number")


print("Welcome to the Ticket Calculator")

height : int = int(input("Enter your height(in centimeters): "))
bill = 0

if height >= 120:
  print("You can go on this ride")
  age : int = int(input("Enter your age: "))
  if age < 12:
    bill = 5
    print("Your ticket costs $5")
  elif age >= 12 and age <= 18:
    bill = 7
    print("Your ticket costs $7")
  elif age > 18:
    bill = 12
    print("Your ticket costs $12")
  photo_taken = input("Do you want a photo taken? [y/n]")
  if photo_taken == "Y":
    bill += 3
    print(f"Your ticket now costs ${bill}")
  else:
    print("Enjoy the ride!")
else:
  print("You can't ride")

