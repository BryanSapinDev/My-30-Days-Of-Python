# Create an empty tuple
empty = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother = ("George", "Kevin")
sister = ("Camille", "Sophie")
# Join brothers and sisters tuples and assign it to siblings
siblings = brother + sister
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("Father")
siblings.append("Mother")
family_members = tuple(siblings)
# Unpack siblings and parents from family_members
siblings = family_members[0:4]
parents = family_members[4:]
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("tomato", "apple", "pear")
vegetables = ("carrot", "zucchini")
animal_product = ("chicken breast", "ribeye") 
food_stuff_tp = fruits + vegetables + animal_product
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp[len(food_stuff_tp)//2]
# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[0:3], food_stuff_lt[-3:])
# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)