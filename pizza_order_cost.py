#welcome message
print("Welcome to Enoch's Pizza!")

#input pizza size
while True:
    pizza_size = input("Enter pizza size (small or large): ").lower()
    if pizza_size in ["small", "large"]:
        break
    print("Please enter a valid pizza size.")

#determine pizza base price
if pizza_size == "small":
    pizza_price = 8
else:
    pizza_price = 12

#get # of toppings
additional_toppings_num = int(input("Enter number of additional toppings: "))
toppings_cost = additional_toppings_num

#delivery distance
delivery_distance_miles = int(input("Enter delivery distance (miles): "))
if delivery_distance_miles <= 5:
    delivery_cost = 2
else:
    delivery_cost = 2 + (delivery_distance_miles - 5)

#calculate total cost
SET total_cost = pizza_price + toppings_cost + delivery_cost

#print message of total cost
PRINT f"Your total is ${total_cost}."


