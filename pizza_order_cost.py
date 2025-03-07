PRINT "Welcome to Enoch's Pizza!"

#input pizza size
PRINT "Enter pizza size (small or large): "
INPUT pizza_size

PRINT "Enter number of additional toppings: "
INPUT additional_topics_num

PRINT "Enter delivery distance (miles): "
INPUT delivery_distance_miles

#determine pizza base price and seeing if size is valid
IF pizza_size == "small" THEN
    SET pizza_price = 8
ELIF pizza_slice == "large" THEN
    SET pizza_price = 12
ELSE
    PRINT "Please enter a valid pizza size."

