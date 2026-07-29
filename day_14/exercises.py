# Explain the difference between map, filter, and reduce.
# Map call a function on every item of the iterable and return an iterable
# Filter add the item on the new list only if the function called return True
# Reduce call a function several times to end up with a result

# Explain the difference between higher order function, closure and decorator
# A function is a higher order function if it take a function as argument ou return a function (or both)
# Closures allows a nested function to access the outer scope of the enclosing function
# Decorators is a design pattern that add new functionality to an existing object, without modifying its structure

#Define a call function before map, filter or reduce, see examples.
def carre (x):
    return x**2

def is_even (x):
    if x % 2 == 0:
        return True
    return False

def a_b_sum (a, b):
    return a + b 

lst = [1, 2, 3, 4, 5]
result_lst = list(map(carre, lst))

result_lst = list(filter(is_even, lst))

from functools import reduce
result_lst = reduce(a_b_sum, lst)

#Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in countries:
    #print(i)

# for i in names:
#     print(i)

# for i in numbers:
#     print(i)

# Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = list(map(lambda x : x.upper(), countries))

# Use map to create a new list by changing each number to its square in the numbers list
square_numbers = list(map(lambda x : x**2, numbers))

# Use filter to filter out countries containing 'land'.
contain_land = list(filter(lambda x : "land" in x, countries))

# Use filter to filter out countries having exactly six characters.
six_len = list(filter(lambda x : len(x) == 6, countries))

# Use filter to filter out countries containing six letters and more in the country list.
six_or_more_len = list(filter(lambda x : len(x) >= 6, countries))

# Use filter to filter out countries starting with an 'E'
start_e = list(filter(lambda x : x[0] == "E", countries))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
even_sum = reduce(a_b_sum, list(filter(is_even, numbers)))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists (lst):
    result_lst = list(filter(lambda x : type(x) == str, lst))
    return result_lst
#print(get_string_lists([1, "a", True, 5.4, "abc"]))

# Use reduce to sum all the numbers in the numbers list.
sum_numbers = reduce(a_b_sum, numbers)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
all_countries = reduce(lambda a, b : f"{a}, {b}" if b != countries[-1] else f"{a} and {b} are north European countries", countries)

# Declare a function called categorize_countries that returns a list of countries with some common pattern
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries as lst_countries
def categorize_countries (lst, pattern):
    return list(filter(lambda country : pattern in country, lst))
#print(categorize_countries(lst_countries, "land"))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def first_letter_countries ():
    every_first_letter = set()
    for country in lst_countries:
        every_first_letter.add(country[0])

    result_dict = dict()
    for letter in every_first_letter:
        result_dict[letter] = 0
    for country in lst_countries:
        result_dict[country[0]] += 1

    return result_dict
#print(first_letter_countries())

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries ():
    return lst_countries[:10]

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries ():
    return lst_countries[-10:]

print(get_last_ten_countries())