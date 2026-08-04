# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
import requests
import re
import numpy

response = requests.get('https://api.thecatapi.com/v1/breeds')
data = response.json()
#Minimum
regex_min_weight = r"^([0-9]+)"
min_weight = []
for breed in data:
    min_weight.extend(re.findall(regex_min_weight, breed["weight"]["metric"]))
min_weight = [int(weight) for weight in min_weight]
#print(min(min_weight))

#Maximum
regex_max_weight = r"([0-9]+)$"
max_weight = []
for breed in data:
    max_weight.extend(re.findall(regex_max_weight, breed["weight"]["metric"]))
max_weight = [int(weight) for weight in max_weight]
#print(max(max_weight))

#Mean
min_and_max = max_weight + min_weight
#print(numpy.mean(min_and_max))

#median
#print(numpy.median(min_and_max))

#standard deviation
print(numpy.std(min_and_max))
