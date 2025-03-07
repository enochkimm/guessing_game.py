#welcome message
print("Welcome to Enoch's Pizza!")

#input pizza size
while True:
    pizza_size = input("Enter pizza size (small or large): ").lower()
    if pizza_size in ["small", "large"]:
        break
    print("Please enter a valid pizza size.")

PRINT "Enter pizza size (small or large): "
INPUT pizza_size
SET pizza_size = LOWERCASE(pizza_size)
WHILE pizza_size != "small" and "pizza_size" != "large"

#determine pizza base price and seeing if size is valid
IF pizza_size == "small" THEN
    SET pizza_price = 8
ELSE pizza_slice == "large" THEN
    SET pizza_price = 12
ENDIF

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


