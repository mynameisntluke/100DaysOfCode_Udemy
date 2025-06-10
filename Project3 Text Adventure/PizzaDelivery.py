print("Welcome to Python Pizza Deliveries!")

# Set initial pizza price
pizza_cost = 0
size = input("What size pizza do you want? S, M or L: ")  # $15, $20 or $25

# TOPPINGS
pepperoni = input("Do you want pepperoni? Y or N: ")  # $2 for S, $3 for M and L
extra_cheese = input("Do you want extra cheese? Y or N: ")  # $1

# GET PRICE
# Assumes user has correctly input their size
if size == "S":
    if pepperoni == "Y":
        pizza_cost = 17
    else:
        pizza_cost = 15
elif size == "M":
    if pepperoni == "Y":
        pizza_cost = 23
    else:
        pizza_cost = 20
else:
    if pepperoni == "Y":
        pizza_cost = 28
    else:
        pizza_cost = 25

if extra_cheese == "Y":
    pizza_cost += 1

print("\n")
print("....................................")
print("Thank you for using Python Pizza Deliveries")
print(f"Your pizza today will cost a sizzling ${pizza_cost}")
