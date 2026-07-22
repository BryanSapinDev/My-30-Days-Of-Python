# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add("Twitter")
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["SpaceX","Mistral"])
# Remove one of the companies from the set it_companies
it_companies.remove("SpaceX")
# What is the difference between remove and discard
#Remove raise an exception if the item is not found, unlike discard

# Join A and B
aJoinB = A | B
# Find A intersection B
aIntersectionB = A & B
# Is A subset of B
A.issubset(B)
# Are A and B disjoint sets
A.isdisjoint(B)
# Join A with B and B with A
A.union(B)
B.union(A)
# What is the symmetric difference between A and B
A.symmetric_difference(B)
# Delete the sets completely
del A
del B

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ageSet = set(age)
print("len(age) : {} / len(ageSet) : {}".format(len(age), len(ageSet)))
# Explain the difference between the following data types: string, list, tuple and set
#A string is one or more character, could be a letter or a sentence
#A list is an ordered collection which is mutable
#A tuple is an ordered collection which is immutable 
#A set is an unordered collection which is mutable but don't allow duplicates
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
splited = "I am a teacher and I love to inspire and teach people.".split()
splitedSet = set(splited)
print(len(splitedSet))