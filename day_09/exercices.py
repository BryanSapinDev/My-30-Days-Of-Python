#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.

"""age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need {} more years to learn to drive.".format(18 - age))"""


#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age.
""" my_age = 24
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if your_age - 1 == my_age:
        print("You are 1 year older than me")
    else:
        print("You are {} years older than me".format(your_age - my_age))
elif your_age < my_age:
    if your_age == my_age - 1:
        print("You are 1 year younger than me")
    else:
        print("You are {} years younger than me".format(my_age - your_age))
else:
    print("We have the same age !") """

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b.
"""a = float(input("Enter a : "))
b = float(input("Enter b : "))
if a < b:
    print("a < b")
elif b < a:
    print("a > b")
else:
    print("a == b")"""

#Write a code which gives grade to students according to theirs scores:
'''your_score = float(input("Enter your score : "))
if 100 >= your_score and your_score >= 90:
    grade = "A"
elif 89 >= your_score and your_score >= 80:
    grade = "B"
elif 79 >= your_score and your_score >= 70:
    grade = "C"
elif 69 >= your_score and your_score >= 60:
    grade = "D"
elif 59 >= your_score and your_score >= 0:
    grade = "F"
else:
    grade = "Need to be between 0 and 100"
print("Your grade is :", grade)'''

#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
'''birth_month = input("In what month where you born : ")
if birth_month == "September" or birth_month == "October" or birth_month == "November":
    print("You where born in the Autumn")
elif birth_month == "December" or birth_month == "January" or birth_month == "February":
    print("You where born in the Winter")
elif birth_month == "March" or birth_month == "April" or birth_month == "May":
    print("You where born in the Spring")
elif birth_month == "June" or birth_month == "July" or birth_month == "August":
    print("You where born in the Summer")
else:
    print("Month error")'''

#The following list contains some fruits:
'''fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_add = input("Enter the fruit to add to the list : ")
if fruit_add in fruits:
    print("This fruit is already in the list")
else:
    fruits.append(fruit_add)
    print(fruits)'''

#Here we have a person dictionary.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
'''if "skills" in person.keys():
    print(person["skills"][2])'''
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
'''if "skills" in person.keys():
    if "Python" in person["skills"]:
        print("This person have Python skills")
    else:
        print("This person don't have Python skills")'''

# * If the person is married and if he lives in Finland, print the information in the following format:
print("{} lives in {}. He is {}".format(person['first_name'], person["country"], "married" if person['is_married'] else "not married"))
