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
PRINT "Enter number of additional toppings: "
INPUT additional_toppings_num
SET toppings_cost = additional_toppings_num

#delivery distance
PRINT "Enter delivery distance (miles): "
INPUT delivery_distance_miles
IF delivery_distance <= 5 THEN
    SET delivery_cost = 2
ELSE 
    SET delivery cost = 2 + (delivery_distance - 5)
ENDIF

#calculate total cost
SET total_cost = pizza_price + toppings_cost + delivery_cost

#print message of total cost
PRINT f"Your total is ${total_cost}."


