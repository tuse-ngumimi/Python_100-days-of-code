# print("WELCOME TO THE BAND NAME GENERATOR")
# pet_name = input("What is the name of your chilhood pet? \n")
# city = input("What is the name of the city you grew up in? \n")

# print("Your band name is " + pet_name + " " + city + "!")

print("WELCOME TO THE TIP CALCULATOR")

amount_paid : int =  float(input("How much did you pay? \n"))
print(f"You paid ${amount_paid}")

tip : int = int(input("""How much would you like to tip?
10, 15, or 20
"""))

num_of_people : int = int(input("How many people are splitting the bill? "))

tip_as_percentage : int = tip / 100

total_tip_amount = amount_paid * tip_as_percentage

bill_per_person = amount_paid / num_of_people

final_amount = round(bill_per_person, 2)

print(f"Your tip is ${final_amount} per person(s)")



