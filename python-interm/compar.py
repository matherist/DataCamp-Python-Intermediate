# Comparison of booleans

True == False
# Comparison of integers

-5*15 != 75
# Comparison of strings
"pyscript" == "PyScript"

# Compare a boolean with an integer
True == 1



# Comparison of integers
x = -3 * 6

x >= -10
# Comparison of strings
y = "test"
'test' <= y

# Comparison of booleans
True > False



# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18

print(my_house >= 18)
# my_house less than your_house
print(my_house < your_house)



# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# Check if my_kitchen is between 10 and 18
print(10 < my_kitchen and my_kitchen< 18)

# Check if my_kitchen is less than 14 or greater than 17
print(my_kitchen < 14 or my_kitchen > 17)

# Check if double the area of my_kitchen is less than triple the area of your_kitchen
print(2 * my_kitchen < 3 * your_kitchen)


# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10

print(np.logical_or(my_house > 18.5, my_house < 10))
# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))