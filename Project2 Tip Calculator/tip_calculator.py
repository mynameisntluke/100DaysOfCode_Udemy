print("\n")
print("\n")
print("=======================")
print("Welcome to the Tip Calculator! v0.1")

total_bill = input("What was the total bill? £")
# Check value is valid (i.e. float)
total_bill = float(total_bill)

tip_percentage = input("How much would you like to tip? 10%, 12% or 15%? ")
# Check answer is one of three possibilities
tip_percentage = float(tip_percentage)
tip_multiplier = 1 + (tip_percentage/100)

people = input("How many people will split the bill? ")
people = float(people)
# Check answer is integer

# DO MAGIC
amount_per_person = total_bill * tip_multiplier / people
amount_per_person = round(amount_per_person, 2)
print(f"Each person should pay: £ {str(amount_per_person)}")
print("=======================")
