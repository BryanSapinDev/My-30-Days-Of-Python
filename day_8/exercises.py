# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Toutou"
dog["color"] = "black"
dog["breed"] = "pitbull"
dog["age"] = 4
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name" : "Bryan", 
           "last_name" : "Sapin", 
           "gender" : "Male", 
           "age" : 24, 
           "marital_status" : "single", 
           "skills" : ["Java", "SQL", "Python"], 
           "country" : "France"
           }
# Get the length of the student dictionary
len(student)
# Get the value of skills and check the data type, it should be a list
print(student["skills"], type(student["skills"]))
# Modify the skills values by adding one or two skills
student["skills"].append("JavaScript")
# Get the dictionary keys as a list
student.keys()
# Get the dictionary values as a list
student.values()
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.pop("country")
# Delete one of the dictionaries
del student
print(student)