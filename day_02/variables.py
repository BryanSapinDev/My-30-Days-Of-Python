# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
first_name = "Bryan"
# Declare a last name variable and assign a value to it
last_name = "Sapin"
# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
print(full_name)
# Declare a country variable and assign a value to it
country = "France"
# Declare a city variable and assign a value to it
city = "Béziers"
# Declare an age variable and assign a value to it
age = 24
# Declare a year variable and assign a value to it
year = 2026
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variable on one line
first_name, last_name, age = "Bryan", "Sapin", 24
print(first_name, last_name, age)

# Exercises: Level 2
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print(len(first_name) == len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * 30 ** 2
print(area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 30 * 3.14
# Take radius as user input and calculate the area.
radius = float(input("Radius : "))
area = 3.14 * radius ** 2
print("The area of the circle is :", area)
# Use the built-in input function to get first name, last name, country and age from a user
# and store the value to their corresponding variable names
first_name, last_name, country, age = ( 
    input("First name : "), input("Last name : "), input("Country : "), int(input("Age : "))
)
print(first_name, last_name, country, age)
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords